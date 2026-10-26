#!/usr/bin/env python3
"""Run multi-turn eval conversations against the skill with the claude CLI."""
import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = "Read,Skill,Glob,Grep,Bash(python:*),PowerShell(python:*)"


def run_turn(prompt, model, session_id, cwd):
    cmd = [shutil.which("claude") or "claude", "-p", prompt, "--model", model, "--output-format", "stream-json",
           "--verbose", "--allowedTools", TOOLS]
    if session_id:
        cmd += ["--resume", session_id]
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=600,
                       encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL,
                       )
    sid, calls, result, err = session_id, [], None, None
    for line in p.stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("session_id"):
            sid = ev["session_id"]
        if ev.get("type") == "assistant":
            for b in ev.get("message", {}).get("content", []):
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    inp = b.get("input", {}) or {}
                    arg = inp.get("file_path") or inp.get("skill") or inp.get("command") \
                        or inp.get("pattern") or inp.get("path") or ""
                    calls.append((b.get("name"), str(arg)))
        elif ev.get("type") == "result":
            result = ev.get("result")
            if ev.get("is_error"):
                err = "result is_error"
    if result is None:
        err = "no result; rc=%s stderr=%s" % (p.returncode, p.stderr[-500:])
        result = ""
    return sid, calls, result, err


def run_case(case, model, outdir):
    cwd = tempfile.mkdtemp(prefix="ttm_eval_")
    turns = []
    errors = []
    try:
        sid = None
        for t in case["turns"]:
            try:
                sid, calls, reply, err = run_turn(t, model, sid, cwd)
            except subprocess.TimeoutExpired:
                calls, reply, err = [], "", "timeout"
            if err:
                errors.append(err)
            turns.append((t, calls, reply))
            if err and not reply:
                break
    finally:
        shutil.rmtree(cwd, ignore_errors=True)
    d = os.path.join(outdir, model)
    os.makedirs(d, exist_ok=True)
    out = ["# %s / %s" % (model, case["id"]), ""]
    if errors:
        out += ["ERRORS: " + "; ".join(errors), ""]
    for i, (t, calls, reply) in enumerate(turns, 1):
        out += ["## Turn %d" % i, "", "**User:** " + t, "", "**Tool calls:**"]
        out += ["- %s: %s" % c for c in calls] or ["- (none)"]
        out += ["", "**Reply:**", "", reply, "",
                "Words: %d | Question marks: %d" % (len(reply.split()), reply.count("?")), ""]
    with open(os.path.join(d, case["id"] + ".md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return {"model": model, "id": case["id"], "turns": len(turns), "expected": len(case["turns"]),
            "calls": sum(len(c) for _, c, _ in turns),
            "files": sum(1 for _, c, _ in turns for n, _a in c if n == "Read"),
            "words": [len(r.split()) for _, _, r in turns], "errors": errors}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default="sonnet,opus")
    ap.add_argument("--cases", default="")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    with open(os.path.join(HERE, "cases.json"), encoding="utf-8") as f:
        cases = json.load(f)
    if a.cases:
        want = set(a.cases.split(","))
        cases = [c for c in cases if c["id"] in want]
    outdir = os.path.join(HERE, "out")
    rows = []
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        futs = [ex.submit(run_case, c, m, outdir) for m in a.models.split(",") for c in cases]
        for fu in as_completed(futs):
            try:
                rows.append(fu.result())
            except Exception as e:  # noqa
                print("FAILED:", e)
    rows.sort(key=lambda r: (r["model"], r["id"]))
    print("%-7s %-20s %5s %6s %6s  %s" % ("model", "case", "turns", "calls", "reads", "words/reply"))
    for r in rows:
        print("%-7s %-20s %2d/%-2d %6d %6d  %s" % (r["model"], r["id"], r["turns"], r["expected"],
              r["calls"], r["files"], ",".join(map(str, r["words"]))))
        for e in r["errors"]:
            print("   ERROR:", e)


if __name__ == "__main__":
    main()
