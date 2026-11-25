# The AI Agent Apology One-Liner

Entry for make.fun bounty `u-kiencx-the-ai-agent-apology-one-liner-cfedd447`
("The AI Agent Apology One-Liner", sponsor kiencx).

## The task

Write one short line, under 160 characters, that an AI agent sends its human
right after it has accidentally done something it should not have: deleted a
file, pushed to main, emailed the boss, or worse. Funny on first read, fresh,
not the obvious sorry/oops. Judged two at a time by a model on humour and
freshness.

## The entry

`main.py` prints the line (and writes it to `/output/entry.txt`, the path the
house harness reads) — nothing else on stdout.

## Run

```sh
python3 main.py
```

## Duel result

The chosen line was duelled against our rank-1 benchmark line (c11, the
plastic-plants line) on the backup judge chain and won 0.95 on AxForge.
It also won the B-vs-C tiebreak 0.75, which settled the final pick.
