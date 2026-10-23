#!/usr/bin/env python3
"""Score work sets for the Three Target Method. Standard library only, Python 3.8+.

Usage:
  python scripts/score.py 190 7 --last 185 8 [--best W R]
  python scripts/score.py --log training-log.csv [--holds "Plank,Side Plank"] [--write]
  python scripts/score.py --log training-log.csv --add 2026-10-12,A,Incline DB Flys,40,13

score = weight * reps * 0.0333 + weight (full precision; rounded only for display).
Holds (--holds names or a `hold` column of yes): PR = more seconds at the same
weight; more weight = "weight added", no score.
"""
import argparse
import csv
import sys


def score(w, r):
    return w * r * 0.0333 + w


def full(x):
    return ("%.3f" % x).rstrip("0").rstrip(".")


def f1(x):
    return "%.1f" % x


def pct_s(p):
    s = f1(p)
    return "%.3f" % p if s in ("0.0", "-0.0") and p != 0 else s


def num(text, what):
    try:
        return float(str(text).strip())
    except ValueError:
        sys.exit("error: %s must be a number, got %r" % (what, text))


def compare(s, ref):
    p = (s - ref) / ref * 100
    return p, s > ref


def quick(args):
    w, r = num(args.nums[0], "weight"), num(args.nums[1], "reps")
    s = score(w, r)
    print("score %s x %s = %s (display %s)" % (args.nums[0], args.nums[1], full(s), f1(s)))
    for label, ref in (("last", args.last), ("best", args.best)):
        if ref:
            rs = score(num(ref[0], label + " weight"), num(ref[1], label + " reps"))
            p, pr = compare(s, rs)
            print("%s score %s -> change %s%%, PR vs %s: %s" % (label, full(rs), pct_s(p), label, "yes" if pr else "no"))


def is_hold(row, holds):
    return row["exercise"].strip().lower() in holds or str(row.get("hold") or "").strip().lower() in ("yes", "y", "true")


def process(rows, holds):
    """Fill row['score'], row['pct_change_vs_last']; return a result note per row."""
    state, notes = {}, []
    for i, row in enumerate(rows, 2):
        w = num(row["weight"], "weight (row %d)" % i)
        r = num(row["reps"], "reps (row %d)" % i)
        ex = row["exercise"].strip()
        prev = state.get(ex)
        if is_hold(row, holds):
            row["score"], row["pct_change_vs_last"] = "", ""
            if prev is None:
                note = "start"
            elif w > prev["w"]:
                note = "weight added"
            else:
                best = prev["best"].get(w, 0)
                note = "PR" if w == prev["w"] and r > best else "no PR"
            st = prev or {"best": {}}
            st["best"][w] = max(st["best"].get(w, 0), r)
            st["w"] = w
            state[ex] = st
        else:
            s = score(w, r)
            if prev is None or "last" not in prev:
                row["pct_change_vs_last"], note = "", "start"
                state[ex] = {"last": s, "best": s}
            else:
                p, _ = compare(s, prev["last"])
                row["pct_change_vs_last"] = pct_s(p)
                note = "PR" if s > prev["best"] else "no PR"
                prev["last"], prev["best"] = s, max(prev["best"], s)
            row["score"] = f1(s)
        notes.append(note)
    return notes


def show(row, note):
    return "%-10s %-2s %-22s %6s x %-4s score %-6s chg %-7s %s" % (
        row["date"], row["workout"], row["exercise"], row["weight"], row["reps"],
        row.get("score") or "-", row.get("pct_change_vs_last") or "-", note)


def logmode(args):
    holds = {h.strip().lower() for h in (args.holds or "").split(",") if h.strip()}
    rows, fields = [], ["date", "workout", "exercise", "weight", "reps", "score", "pct_change_vs_last"]
    try:
        with open(args.log, newline="", encoding="utf-8-sig") as fh:
            rd = csv.DictReader(fh)
            if rd.fieldnames:
                missing = [c for c in fields[:5] if c not in rd.fieldnames]
                if missing:
                    sys.exit("error: %s is missing column(s): %s" % (args.log, ", ".join(missing)))
                fields = list(rd.fieldnames) + [c for c in fields[5:] if c not in rd.fieldnames]
            rows = list(rd)
    except FileNotFoundError:
        if not args.add:
            sys.exit("error: file not found: %s" % args.log)
    if args.add:
        parts = [p.strip() for p in args.add.split(",")]
        if len(parts) != 5:
            sys.exit("error: --add needs date,workout,exercise,weight,reps")
        rows.append(dict(zip(fields[:5], parts)))
    for row in rows:
        for c in fields:
            row.setdefault(c, "")
    notes = process(rows, holds)
    if args.add:
        print(show(rows[-1], notes[-1]))
    else:
        for row, note in zip(rows, notes):
            print(show(row, note))
    if args.write or args.add:
        with open(args.log, "w", newline="", encoding="utf-8") as fh:
            wr = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
            wr.writeheader()
            wr.writerows(rows)
        print("wrote %s" % args.log)


def main():
    ap = argparse.ArgumentParser(description="Three Target Method scorer")
    ap.add_argument("nums", nargs="*", help="WEIGHT REPS")
    ap.add_argument("--last", nargs=2, metavar=("W", "R"))
    ap.add_argument("--best", nargs=2, metavar=("W", "R"))
    ap.add_argument("--log")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--add")
    ap.add_argument("--holds")
    args = ap.parse_args()
    if args.log:
        logmode(args)
    elif len(args.nums) == 2:
        quick(args)
    else:
        ap.error("give WEIGHT REPS, or --log FILE")


if __name__ == "__main__":
    main()
