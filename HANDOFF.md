# HANDOFF — gta6-meme-x-01 (Megalodon Shark Card)

Built 21 Nov 2026, in-window (bounty opened 19 Nov 14:00 UTC, deadline
23 Nov 21:00 WIB / 14:00 UTC). Repo pushed, image verified. **Do NOT
submit yet — two blockers below.**

## What is done

- Meme image: `assets/entry.png`, 1200×1200, drawn in code
  (`tools/build_meme.py`, Pillow + DejaVu). Visually verified at full
  size and at 500px / 300px thumbnails: joke lands, make.fun legible
  (ghost + wordmark ×4), no text clip/overlap, no watermark.
- `main.ts`: Node 22 stdlib only (`node:fs`, `node:path`, `node:url`),
  copies `assets/entry.png` + `POST.json` to `$MAKEFUN_OUTPUT_DIR`.
  Two runs → byte-identical (sha256 verified, see below).
- Repo: https://github.com/stellarlumens29/gta6-meme-x-01 (public, MIT,
  homepage https://make.fun/bounty/gta6-meme-x-01). Commit recorded in
  the parent report / below after push.
- Field-check done (21 Nov ~15:35 UTC): 3,714 ranked entries; "shark
  card" = 0 entries — the differentiator. Top-1/2/5 images viewed.

## BLOCKER 1 — play code (needed before posting)

The image renders the play-code line as `makefun-___-___-___` (a blank)
and the post-text draft has `[FILL IN]`. The real code was NOT
available to this build: `GET /api/competitions/gta6-meme-x-01/play-code`
returns 401 without auth, and this build must not touch the account API
key / wallet / keypair. No play code exists anywhere in the workspace
(grepped all of `~/workspace/makefun` — only the kit's example
`makefun-oak-river-lantern`).

**Fix (2 minutes, needs the code from the user's make.fun account):**

1. Get one of the account's play codes (`makefun-word-word-word`).
2. In `tools/build_meme.py`, set `PLAY_CODE = "<the code>"`.
3. `python3 tools/build_meme.py` (regenerates `assets/entry.png`).
4. Re-verify the image (footer line must show the real code, legible).
5. Commit + push (same repo, new commit).

A follow-up session can do this the moment the code is supplied.

## BLOCKER 2 — post on X, then fill POST.json

The post itself is the entry: the house reads it from X. This build
does NOT post to X.

1. Post `assets/entry.png` (the regenerated one, with the real play
   code) from the public X account `@stellarlumens29`, with the text in
   README.md (play code filled in), **before 23 Nov 21:00 WIB**.
2. Copy the post URL, e.g.
   `https://x.com/stellarlumens29/status/<id>`.
3. Replace `POST.json` contents with `{"url": "<post URL>"}`.
4. Commit + push.
5. Submit that commit (repo + transcripts incl. this TRANSCRIPT.md).
   Live brief: max **5 submissions/day, 10 total** (not 10/20).

## Suggested submit title

"Megalodon Shark Card — $100 of fake money, or one real GTA VI paid by
my AI agent's make.fun bounty"

## Verification log (this session)

- `python3 tools/build_meme.py` → `assets/entry.png` 537,603 bytes,
  1200×1200 RGB. 4 render iterations (v1: stamp overlapped $99.99,
  footer clipped, sun hidden, stray palm arcs; v2: total row collided
  with footer; v3: sub-line struck by divider; v4: clean).
- Visual check v4: full size + 500px + 300px + bottom crop — all text
  legible, no overlaps, no clipping, ghost + make.fun clear.
- `main.ts` run twice → identical sha256 (recorded at push time below).
- `grep -E "^(import|from)" main.ts` → only `node:fs`, `node:path`,
  `node:url` (stdlib). No PIL/numpy in the graded program (PIL is only
  in the local build tool, same pattern as news-image-01).

## Verification (fill at push time)

- main.ts run 1 sha256: 22b9059bb7e08f4cadde1168b6f14d7e57954786a69e15fe1276ab2fcc21671a
- main.ts run 2 sha256: 22b9059bb7e08f4cadde1168b6f14d7e57954786a69e15fe1276ab2fcc21671a
  (identical; also equals assets/entry.png sha256)
- Repo HEAD commit: ___
- Repo created at (UTC): ___ (must be after 19 Nov 14:00 UTC)
