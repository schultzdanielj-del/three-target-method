# Three Target Method (TTM)

Intermediate drug free physiques hit a plateau that can only be broken by throwing away almost everything that got your body to where it is now. You'll see more cuts in the mirror and more muscle than ever before in the right spots, even if your first workout was 20 years ago.

The full eating and workout protocols are laid out in full detail to learn 100% for free.

Three target method stacks only the principles that matter across eating and lifting to get muscular and lean. Those principles are hit as hard as humanly possible, and everything else is ignored.

We optimize for max results per unit of sacrifice. Only choosing methods and habits with the smallest impact on time, focus, and other life priorities. Every method/habit is measured by results per unit of sacrifice using the pareto principle. The top percentile of them make the cut and are increased. The bottom methods and habits are eliminated.

Website: https://threetargetmethod.com

## The three targets

- Target 1 - Minimum Life Sacrifice. We optimize for max results per unit of sacrifice. Only choosing methods and habits with the smallest impact on time, focus, and other life priorities.
- Target 2 - Long Term Muscle. Workouts target a longer runway of tail end muscle growth with a 40-50% reduction in weekly time investment.
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

The method is written for intermediate, drug free lifters. Per the site's disclaimer it is designed for generally healthy adults (see `disclaimer.md`). Nothing here is medical advice.

## Using this repo with an AI agent

Point the agent at this repo and have it read `SKILL.md` first (`AGENTS.md` points there). The agent helps one person run the method: tracking their workouts and eating against the rules written on the site. It does not coach beyond those rules.

## How to load this

- Claude: download this folder and add it as a skill (the folder is named `three-target-method` and has `SKILL.md` at its top).
- Claude Code: copy the folder into `~/.claude/skills/three-target-method`.
- Any other AI: give it the repo link, or https://threetargetmethod.com/llms-full.txt.

## File map

| Path | What it is |
| --- | --- |
| `README.md` | This file. |
| `SKILL.md` | Instructions for an AI agent running TTM for one person, with Claude skill frontmatter. Read this first. |
| `AGENTS.md` | Short pointer to `SKILL.md`, for tools that look for this filename. |
| `log-format.md` | The per-work-set training log and the daily eating check: columns, formulas, JSON example. |
| `protocol/training.md` | The training protocol: structure and split, movements, execution, progression. |
| `protocol/eating.md` | The eating protocol: timing, Mode 1, Mode 2. |
| `why/training.md` | How the training works. |
| `why/eating.md` | How the eating works. |
| `why/bimodal-day.md` | A day of bimodal eating. |
| `faq/training.md` | Training FAQ. |
| `faq/eating.md` | Eating FAQ. |
| `disclaimer.md` | The site disclaimer. |

Everything under `protocol/`, `why/` and `faq/`, plus `disclaimer.md`, is generated from the live site's pages, so it matches the site exactly. Do not edit those files by hand. The files at the root (`README.md`, `SKILL.md`, `AGENTS.md`, `log-format.md`) are hand-written.
