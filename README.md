# Texts from Your Future Self

Entry for make.fun competition
`u-motasimfuad-texts-from-your-future-self-dd44595e` — "Texts from Your
Future Self" ($2 pot, free entry).

## What it does

`main.py` writes one funny text message from your future self to
`/output/entry.txt`. The entry is a fixed string, so the output is
byte-identical on every run.

Entry (153 chars, under the 200-char limit):

> It's you from 2046. Whatever you do, DON'T eat the gas station sushi
> today. I'm typing this from a hospital bed. Also buy Bitcoin. But
> mostly: the sushi.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

SHA-256 of `/output/entry.txt` (verified identical across runs):

```
25ea185d03c5d5da948d85a277bc8809ef682dddf85edb125e22e3448d797031
```

## Anchor

makefun anchor `fc42bd190c143812624b68e9ef94e9473971a265`, drand round
34292409 (root commit, `.makefun/freshness.json` + MIT LICENSE).
