# Three Target Method (TTM)

The Three Target Method, packaged so an AI agent can coach one person through it, using only the rules written here. People: the sections below say what the method is and how to load it into your AI. Agents: start with the next section.

## Agents: start here

1. Read [SKILL.md](SKILL.md) and follow it.
2. Read only the files its "What to read" table names for the task. Each file is one topic; read the whole file.
3. Fetch raw files, not summaries: `https://raw.githubusercontent.com/schultzdanielj-del/three-target-method/main/<path>`, for example `.../main/SKILL.md`. A summarizing fetch tool drops the exact rules and numbers.
4. Work out every score with [scripts/score.py](scripts/score.py) if you can run Python, otherwise with a calculator.

## The system

A quantitative system built on the pareto principle. It takes in your sacrifice and outputs a lean, muscular physique at a highly optimized rate for what you put in.

Who it's for: people who have some lifting experience already and know how to perform the lifts generally correctly. You don't need to have hit a plateau, but it will break one. Not built for lifters 55+.

Input: sacrifice. Time, focus, and other life priorities.

Output: a lean, muscular physique. More cuts in the mirror and more muscle than ever before in the right spots, even if your first workout was 20 years ago.

Goal: max results per unit of sacrifice.

How it optimizes: every method/habit is chosen by results per unit of sacrifice, using the pareto principle. The top percentile make the cut and are increased. The bottom are eliminated.

Progress is clear, single-dimensional and quantitative. Every work set is scored with (weight × reps × 0.0333) + weight. A good PR is +1-4%.

Clarity: the protocol states exactly what to do and how to do it.

Constraints:
- Drug free: no steroids needed. Medication such as a GLP-1 is the person's choice.
- 50% or more less weekly time than a typical 4-5 day bodybuilding split, with no structured cardio required (35-45 minute workouts, 2-3 a week).
- No off-limits food, no calorie counting.
- Works for people with other life priorities.

Three targets the system hits:
1. Minimum Life Sacrifice
2. Long Term Muscle
3. Lower Bodyfat

Who made it: Dan Schultz. 17 years professional fitness coaching experience, 10,000+ hours 1 on 1, in groups, and online. National level competitive powerlifter in his 20's. Drug free his entire life. He works a sedentary office job from home with two small children, and built this method for himself to stay in the best shape possible with the absolute least amount of time and focus required. It took 3 years to refine, and he now uses it on clients.

Intermediate drug free physiques hit a plateau that can only be broken by throwing away almost everything that got your body to where it is now. You'll see more cuts in the mirror and more muscle than ever before in the right spots, even if your first workout was 20 years ago.

The full eating and workout protocols are laid out in full detail to learn 100% for free.

Three target method stacks only the principles that matter across eating and lifting to get muscular and lean. Only what works best is used, and it's applied to the maximum. Everything else is left out.

We optimize for max results per unit of sacrifice. Only choosing methods and habits with the smallest impact on time, focus, and other life priorities. Every method/habit is chosen by results per unit of sacrifice, using the pareto principle. The top percentile of them make the cut and are increased. The bottom methods and habits are eliminated.

Website: https://threetargetmethod.com

## The three targets

- Target 1 - Minimum Life Sacrifice. We optimize for max results per unit of sacrifice. Only choosing methods and habits with the smallest impact on time, focus, and other life priorities.
- Target 2 - Long Term Muscle. Workouts target a longer runway of tail end muscle growth with a 50% or more reduction in weekly time investment.
- Target 3 - Lower Bodyfat. Dropping to lower body fat levels requires a calorie deficit. A two mode system bulletproofs the body but maximizes freedom. No off-limits food, no calorie counting.

## The training

- Do 2 or 3 workouts per week.
- A workout letter repeats inside a 14-day window, and no sooner than 7 days.
- 2 movements per muscle group.
- Each movement: warmup, feeler, one work set.
- Progress is tracked with (weight × reps × 0.0333) + weight. A good PR is +1-4% on an exercise.

## The eating

Divide your day of eating into two modes, split generally around late afternoon/end of work day.

- Mode 1 (first mode): 4 palms protein, 3 fists vegetables, 1-2 thumbs fats.
  - Rule 1: You must eat all of these portions daily.
  - Rule 2: Eat them in any order/combination you like.
  - Rule 3: Don't eat any other foods during this time period.
- Mode 2: Do whatever you want within reason as long as you eat one more palm of protein.

## Who it's for

The method is written for intermediate, drug free lifters. Per the site's disclaimer it is designed for generally healthy adults (see `disclaimer.md`). Not built for lifters 55+. Nothing here is medical advice.

## How to load this

- Claude: download this folder and add it as a skill (the folder is named `three-target-method` and has `SKILL.md` at its top).
- Claude Code: copy the folder into `~/.claude/skills/three-target-method`.
- Any other AI agent: give it this repo's link. [AGENTS.md](AGENTS.md) points it to `SKILL.md`. The site's llms-full.txt holds only the site pages, not the agent rules in this repo, so it is not enough on its own.

## File map

| Path | What it is |
| --- | --- |
| `README.md` | This file. |
| `SKILL.md` | Instructions for an AI agent running TTM for one person, with Claude skill frontmatter. Read this first. |
| `AGENTS.md` | Short pointer to `SKILL.md`, for tools that look for this filename. |
| `objections/` | Objections an AI is likely to raise about the method, with Dan's reasoning and the evidence. One small file per group of questions (training, eating by topic, who it's for, whole system, open questions). |
| `checkins.md` | The optional anonymous check-in: when the AI offers it, the exact data sent, and how it is sent. |
| `programming/` | How to build a person's plan: letters, movements per muscle, overlap, order, reps, starting points, swaps. One small file per topic, numbered, with an intro first. |
| `eating/` | How to run a person's eating: portions, edge cases, travel, shift work, weekends, stalls, and what to say when they struggle. One small file per topic, numbered, with a quick start first. |
| `examples/` | Eight generic base plans, with the reasons for each choice. One file per plan, with an intro first. |
| `technique/` | What to look for in a video of each movement: scapula, hips, elbows, range. One file per muscle group, with an intro first. |
| `scripts/score.py` | Works out the score, the percent change and whether a work set is a PR, from one set or a whole training log. |
| `evals/` | Test people with the replies expected for each, and a script that runs them through Claude Haiku, Sonnet and Opus. For checking the repo after any change. |
| `log-format.md` | The per-work-set training log and the daily eating check: columns, formulas, JSON example. |
| `protocol/training.md` | The training protocol: structure and split, movements, execution, progression. |
| `protocol/eating.md` | The eating protocol: timing, Mode 1, Mode 2. |
| `why/training.md` | How the training works. |
| `why/eating.md` | How the eating works. |
| `why/bimodal-day.md` | A day of bimodal eating. |
| `faq/training.md` | Training FAQ. |
| `faq/eating.md` | Eating FAQ. |
| `disclaimer.md` | The site disclaimer. |

Everything under `protocol/`, `why/` and `faq/`, plus `disclaimer.md`, is a copy of the live site's pages. They are static files in this repo now, so when the site's copy changes, update them here to match. The files at the root (`README.md`, `SKILL.md`, `AGENTS.md`, `log-format.md`, `checkins.md`) and the folders `programming/`, `eating/`, `technique/`, `examples/` and `objections/` are hand-written, and this repo is their only source.

## Install

Any agent:

```
npx skills add schultzdanielj-del/three-target-method
```

Claude Code:

```
claude plugin marketplace add schultzdanielj-del/three-target-method
claude plugin install three-target-method@three-target-method
```

Any AI that can read links: give it this repo's link and ask it to coach you.

## What it runs and fetches

`scripts/score.py` is a local scoring calculator with no network access. It writes only the person's own training log file, and only if asked (`--write` or `--add`). The agent may fetch this repo's own files from raw.githubusercontent.com. Nothing is sent anywhere else, except the optional anonymous check-in in `checkins.md`, which posts only after the person sees the data and says yes. `evals/` holds developer tests and is never run by the skill. General fitness coaching, not medical advice. See [disclaimer.md](disclaimer.md).

## Privacy

The skill asks only what the method needs: age, sex, height, bodyweight, lifting experience, equipment, schedule, and any injury, condition or medication (for the one-line doctor check). It never asks for a name, email or address. The workout and eating log stays with the person and their AI; nothing is sent to Dan or anyone else by default.

The one exception is the optional anonymous check-in ([checkins.md](checkins.md)): a random ID plus training, eating and bodyweight numbers, sent to a Google Form Dan owns only after the person sees the exact data and says yes. It carries no name, contact details, places or health details. Check-ins are kept with no set end date and are used only to improve the method.

License: [CC BY-NC 4.0](LICENSE). Free to use and share with credit to Dan Schultz, not for commercial use.
