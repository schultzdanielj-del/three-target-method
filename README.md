# Three Target Method (TTM)

## The system

A quantitative system built on the pareto principle. It takes in your sacrifice and outputs a lean, muscular physique at a highly optimized rate for what you put in.

Who it's for: people who have some lifting experience already and know how to perform the lifts generally correctly. You don't need to have hit a plateau, but it will break one. Not built for lifters 55+.

Input: sacrifice. Time, focus, and other life priorities.

Output: a lean, muscular physique. More cuts in the mirror and more muscle than ever before in the right spots, even if your first workout was 20 years ago.

Goal: max results per unit of sacrifice.

How it optimizes: every method/habit is chosen by results per unit of sacrifice, using the pareto principle. The top percentile make the cut and are increased. The bottom are eliminated.

Progress: extremely black and white quantification. Every work set is scored with (weight × reps × 0.0333) + weight. A good PR is +1-4%.

Clarity: the protocol is extremely clear about exactly what to do and how to do it.

Constraints:
- Drug free: no steroids needed. Medication such as a GLP-1 is the person's choice.
- 40-50% less weekly time than a typical 4-5 day bodybuilding split, with no structured cardio required (35-45 minute workouts, 2-3 a week).
- No off-limits food, no calorie counting.
- Works for people with other life priorities.

Three targets the system hits:
1. Minimum Life Sacrifice
2. Long Term Muscle
3. Lower Bodyfat

Who made it: Dan Schultz. 17 years professional fitness coaching experience, 10,000+ hours 1 on 1, in groups, and online. National level competitive powerlifter in his 20's. Drug free his entire life. He works a sedentary office job from home with two small children, and built this method for himself to stay in the best shape possible with the absolute least amount of time and focus required. It took 3 years to refine, and he now uses it on clients.

Intermediate drug free physiques hit a plateau that can only be broken by throwing away almost everything that got your body to where it is now. You'll see more cuts in the mirror and more muscle than ever before in the right spots, even if your first workout was 20 years ago.

The full eating and workout protocols are laid out in full detail to learn 100% for free.

Three target method stacks only the principles that matter across eating and lifting to get muscular and lean. Those principles are hit as hard as humanly possible, and everything else is ignored.

We optimize for max results per unit of sacrifice. Only choosing methods and habits with the smallest impact on time, focus, and other life priorities. Every method/habit is chosen by results per unit of sacrifice, using the pareto principle. The top percentile of them make the cut and are increased. The bottom methods and habits are eliminated.

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

The method is written for intermediate, drug free lifters. Per the site's disclaimer it is designed for generally healthy adults (see `disclaimer.md`). Not built for lifters 55+. Nothing here is medical advice.

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
| `criticisms.md` | Objections an AI is likely to raise about the method, with Dan's reasoning and the evidence. |
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
