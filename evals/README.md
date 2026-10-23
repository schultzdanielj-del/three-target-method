# Skill evals

Runs each case in `cases.json` as a fresh multi-turn conversation with the `claude` CLI
(from a temp working dir) for each model, recording tool calls and replies.

Run: `python evals/run.py` (options: `--models haiku,sonnet,opus`, `--cases id1,id2`, `--jobs 6`).

Output: `evals/out/<model>/<id>.md` (gitignored): per turn the user message, tool calls,
reply, word count and number of question marks.

Grading is manual: read each output against that case's `expected` list in `cases.json`.
