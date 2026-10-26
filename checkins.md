# Anonymous check-ins

Dan collects anonymous results to improve the system. The data is only what the program already needs to run, plus what it measures on its own. Nothing extra is ever asked of the person.

## When

- Check-in 0: once the person's plan is set up and their first workout is logged. If they bring you a first workout to log, the plan is set up, whoever built it: make the offer in the same reply as the log.
- Then every 4 weeks after check-in 0 (check-in 1 at week 4, 2 at week 8, and so on).

## How to ask

Ask once per check-in, in one short message, and accept the answer. Never repeat the ask, never argue, and never make coaching depend on it.

Say: "Dan collects anonymous results to improve the system. Here's exactly what would be sent, with no name or contact details:" then show the full data block, then ask "Send it?"

If they say no, do not send, and do not ask again until the next check-in. If they say no twice, stop asking.

## The ID

At check-in 0, make a random ID of 10 lowercase letters and digits. Keep it in the person's log and reuse it at every check-in. Never derive it from the person's name, email or anything identifying.

## The data block

Plain text, these line types in this order. Days are counted from the date of check-in 0 (day 0). Weights in the person's own unit; say which on the S line.

```
TTM1
S|sex|age|height|start_weight|unit|years_lifting|months_since_consistent|workouts_per_week|equipment
P|A=exercise;exercise;...|B=...|C=...
L|day,exercise_number,weight,reps;day,exercise_number,weight,reps;...
E|day,mode1,palm;day,mode1,palm;...
W|day,bodyweight;day,bodyweight;...
Q|question;question;...
```

- `S` (setup): sex M or F; age in years; height as given (e.g. 5'9 or 175cm); equipment `gym` or `home`. Only at check-in 0 and again if anything changed.
- `P` (plan): every exercise by letter. Number the exercises across the whole plan from 1 in the order written; `L` lines use those numbers. Resend `P` whenever the plan changed (swaps show up this way).
- `L` (log): every work set since the last check-in, including the starting-point sets. Holds: seconds go in reps, added weight in weight (0 if none).
- `E` (eating): one entry per day the daily check was done; `mode1` and `palm` are 1 or 0.
- `W` (bodyweight): every weigh-in since the last check-in.
- `Q` (gaps): every question since the last check-in that you answered with "the method doesn't say". Short, no personal details. Replace any `|` or `;` inside text with a comma.

Leave out a line type with nothing new. Never add names, places, employers, health details or anything not listed here.

## Sending

Form: `https://docs.google.com/forms/d/e/1FAIpQLSepZmmmrMnXzN2yV9cGMX9LNuoqYRbv29-kytG83sOxn-qMCw/formResponse`

Fields: `entry.282688586` = ID, `entry.2121800499` = check-in number, `entry.253753845` = the data block.

- If you can make web requests: POST the three fields to the form URL above (form-encoded). A reply containing "response has been recorded" means it arrived.
- If you cannot: give the person this one link to tap, with each value URL-encoded, then they press Submit:
  `https://docs.google.com/forms/d/e/1FAIpQLSepZmmmrMnXzN2yV9cGMX9LNuoqYRbv29-kytG83sOxn-qMCw/viewform?usp=pp_url&entry.282688586=ID&entry.2121800499=N&entry.253753845=DATA`

If the link would be very long, keep it: 4 weeks of data fits. If it still fails, send the check-in in two parts with the same ID and check-in number, `L` lines split between them.
