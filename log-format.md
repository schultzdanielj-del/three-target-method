# Log format

Two logs, kept by the agent for the one person it is helping.

The site says to "Log your work set weight x reps for each exercise, nothing else" (`protocol/training.md`, section 4). The date, workout letter and exercise name identify which set it is. The score and percent columns are computed by the agent from weight and reps, so the person only ever supplies weight and reps.

## Training log: one row per work set

One row per exercise per workout, for the work set only. Warmup sets, feeler sets, quality sets and the unlogged second work set are not rows.

### CSV

File: `training-log.csv`

```
date,workout,exercise,weight,reps,score,pct_change_vs_last
2026-10-05,A,Incline DB Flys,40,12,56.0,
2026-10-12,A,Incline DB Flys,40,13,57.3,2.4
```

### Columns

| Column | Meaning |
| --- | --- |
| `date` | Date of the workout, `YYYY-MM-DD`. |
| `workout` | Workout letter from the person's plan (A, B, C or D). |
| `exercise` | Name of the exercise, written the same way every time so rows can be compared. |
| `weight` | Work set weight. |
| `reps` | Reps completed in the work set. |
| `score` | `(weight × reps × 0.0333) + weight`, from `protocol/training.md`. Rounded to 1 decimal place for display, as the site does (100 × 13 reps = 143.3). |
| `pct_change_vs_last` | `(score − previous score for the same exercise) ÷ previous score × 100`, rounded to 1 decimal place. Blank on the first row for an exercise. Site example: 140 to 143.3 is "2.4% more". |

### Computing

Use the formula as written, at full precision, and round only for display.

```
score = (weight * reps * 0.0333) + weight
pct_change_vs_last = (score - last_score) / last_score * 100
is_pr = score > best_score_so_far_for_exercise
```

Check against the site's example: 100 × 12 reps gives 139.96, which the site shows as 140. 100 × 13 reps gives 143.29, shown as 143.3. The change is 2.4%, which is the number the site gives.

### JSON example

```json
{
  "date": "2026-10-12",
  "workout": "A",
  "exercise": "Incline DB Flys",
  "weight": 40,
  "reps": 13,
  "score": 57.3,
  "pct_change_vs_last": 2.4,
  "is_pr": true
}
```

A whole log can be an array of these objects in `training-log.json`.

## Daily eating check: one row per day

### CSV

File: `eating-log.csv`

```
date,mode1_hit,mode2_extra_palm_protein
2026-10-12,y,y
2026-10-13,y,n
```

### Columns

| Column | Meaning |
| --- | --- |
| `date` | `YYYY-MM-DD`. |
| `mode1_hit` | `y` if all Mode 1 portions were eaten that day (4 palms protein, 3 fists vegetables, 1-2 thumbs fats, with at least one cruciferous vegetable serving) and no other foods were eaten during Mode 1. `n` otherwise. Source: `protocol/eating.md`, Mode 1 rules 1-3. |
| `mode2_extra_palm_protein` | `y` if the one extra palm of protein was eaten in Mode 2. `n` otherwise. Source: `protocol/eating.md`, Mode 2. |

### JSON example

```json
{
  "date": "2026-10-12",
  "mode1_hit": true,
  "mode2_extra_palm_protein": true
}
```

Calories and macros are not logged. The method does not use them (`faq/eating.md`: "I want to count calories").

### Optional bodyweight column

File: `eating-log.csv`. Add an optional `bodyweight` column. The person chooses how often to fill it in; leave it blank on other days. It feeds the current-weight to cruise-weight-range path in `criticisms.md`.

```
date,mode1_hit,mode2_extra_palm_protein,bodyweight
2026-10-12,y,y,182
2026-10-13,y,n,
```
