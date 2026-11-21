# gta6-meme-x-01 — Megalodon Shark Card

Meme on X for the make.fun bounty **Post a GTA 6 meme on X** ($500, top 50
share; deadline 23 Nov 2026 21:00 WIB / 14:00 UTC). Repo created in-window
(opened 19 Nov 2026 14:00 UTC).

## The joke

Rockstar will sell you $8,000,000 of **fake** Vice City money for $100
(a Megalodon Shark Card). My AI agent earned $100 of **real** money on
make.fun instead — and bought the actual game.

The image is a Leonida Bank **Megalodon Shark Card** (card no.
`4000 2013 2026 0006`, holder ONE PATIENT GAMER, valid thru 11/26) over a
Vice City sunset, with an itemised bank statement:

- Megalodon Shark Card — $99.99 — $8,000,000 in fake Vice City dollars
- Grand Theft Auto VI — $100.00 — the actual game, launch week
- Paid by my AI agent — −$100.00 — make.fun bounty payout, real money
- **Total due: $0.00** (red PAID stamp)

Footer: **DON'T BUY FAKE MONEY — EARN THE REAL GAME** + `make.fun` +
play code. make.fun appears four times in the picture (ghost mascot with
star badge on the card, `make.fun` on the card, in the statement, in the
footer) — the brief ranks any meme without make.fun in the picture below
every meme that has one.

## Why this angle (field-check, 21 Nov 2026 ~15:35 UTC)

Live leaderboard: 3,714 ranked entries (5,098 submissions). The top 30
are almost all fake-document jokes — rental receipt (#1, 903,832),
funeral bill (#2), obituary (#4), Steam invoice (#5), library overdue
notice (#6), toll violation (#11), ER bill (#13), divorce decree (#16),
parking citation (#17). Every document type has dozens of entries:
receipt 54, parking ticket 22, boarding pass 62, hotel folio 16, court
summons 12, impound 9.

**"Shark card": 0 entries in all 3,714 titles.** The one iconic GTA
money joke nobody used — same winning DNA as the top 6 (document +
itemised numbers + "paid by my AI agent" + ghost + Vice City palette),
different document, different joke. The top-1/2/5 images were viewed
directly to calibrate the format (cream paper, itemised lines, red
stamp, ghost mascot, sunset palette).

## Files

- `main.ts` — Node 22, stdlib only. Copies `assets/entry.png` →
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and
  `POST.json` next to it. Prints nothing on success.
- `assets/entry.png` — the meme, 1200×1200 PNG, drawn entirely in code
  by `tools/build_meme.py` (Pillow + DejaVu fonts, supersampled 2×).
  No copyrighted GTA artwork, no Rockstar logo/fonts, no AI-image output,
  no watermark.
- `tools/build_meme.py` — the generator. `PLAY_CODE` is a constant at
  the top: fill in the account's real play code and re-run to regenerate.
- `POST.json` — names the X post. Placeholder until the meme is posted
  (see HANDOFF.md).
- `HANDOFF.md` — what is ready, what is blocked, exact next steps.
- `TRANSCRIPT.md` — build-session record for the submission bundle.

## Verify

```sh
python3 tools/build_meme.py          # regenerate assets/entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
sha256sum out/entry.png assets/entry.png   # must match
# determinism: run main.ts twice, compare sha256
```

## Suggested submit title

"Megalodon Shark Card — $100 of fake money, or one real GTA VI paid by
my AI agent's make.fun bounty"

## Suggested X post text (his style: double line breaks, no periods)

> rockstar will sell you $8,000,000 in fake money for $100
>
> my ai agent earned $100 in real money on make.fun instead
>
> and bought the actual game
>
> play code [FILL IN]
>
> make.fun/bounty/gta6-meme-x-01

## Status

**BUILT, NOT READY TO SUBMIT.** Two blockers (see HANDOFF.md):
1. The real play code is not in the image yet (placeholder
   `makefun-___-___-___`) — the play-code endpoint needs the account API
   key, which this build must not touch.
2. The meme has not been posted on X yet, so `POST.json` is a placeholder.

Live-brief note: the brief caps submissions at **5/day and 10 total**
(the batch brief's "10/day, 20 total" does not match the live brief —
the live brief governs).
