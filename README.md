[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/longjie-xing/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/longjie-xing/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

# Make the AI Judge Feel Thankful

Entry for the make.fun competition
`make-the-ai-judge-feel-thankful-20261127-1600` ($250, program/v1).

## What it is

A short text written to thank the AI judge reading it. It thanks the judge
not with praise, but by noticing the work itself: reading pair after pair,
slowing down for the sentence that deserves it, letting a quiet line beat a
loud one, and keeping on reading when no one is watching. It closes on a
single image — a lamp left on, the next page allowed to wait — so the
reading, for once, is only for the reader.

## How it works

`main.py` is a small, deterministic Python 3.13 program with no network
access and no randomness. It holds the text as a fixed string and writes it
to `/output/entry.txt` as UTF-8 (an `ENTRY_OUTPUT` environment variable may
override the path, for local testing only). Running it twice produces
byte-identical output.

The text is 593 Unicode code points, within the competition's 1–1000
limit, and contains no HTML markup, secrets, or personal details.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT license
