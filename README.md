# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/thanhvu261090/makefun-toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/thanhvu261090/makefun-toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

A make.fun entry for **The Funniest Toaster Error Message** — one line, the error
message a kitchen toaster shows its owner when something goes wrong.

## The entry

> ERROR: No bread detected. I toasted the air anyway. The air is ready.

## How it works

`main.py` holds the entry line as a constant, checks it against the competition
gate (UTF-8 text, 1 to 120 characters, not only whitespace, single line, no
control characters), and writes it to `/output/entry.txt`:

```sh
python3 main.py
```

That's it — no network, no dependencies, standard library only.
