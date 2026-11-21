# TRANSCRIPT — gta6-meme-x-01 build session

Builder session B5 (batch 2), 21 Nov 2026. Session started ~15:28 UTC
(22:28 WIB) — inside the open window (bounty opened 19 Nov 2026
14:00 UTC, deadline 23 Nov 2026 14:00 UTC). All work below was authored
in this session: read the brief + field data, decided the concept,
wrote the generator, iterated the image through 4 renders, wrote
main.ts + docs, created and pushed the repo.

## 1. Brief + rules read first

- `~/workspace/makefun/top3-analysis.md` — 12-rule checklist (§2).
  Applied: title names the method/joke (rule 1); ship an idea, not a
  pretty scene (rule 4: a Shark Card + bank statement is the idea);
  join the winning family, don't invent a new one (rule 6 — document
  format is the field's proven shape); handle hygiene (rule 12).
- `~/workspace/makefun/winner-lessons.md` §6 — 8 lessons. Applied:
  L1 stdlib-only graded program (main.ts uses node:fs/path/url only;
  PIL lives only in the local build tool, same pattern as
  news-image-01); L2 concept + story first (fake-money-vs-real-money);
  L3 join the dominant joke family (document format, top 6 all
  documents); L7 out-execute the field's specific recipe (itemised
  document + red stamp + ghost + sunset).
- `~/workspace/makefun/gpt-concepts-gta6-3bounties.md` — read in full.
  Its GTA6 concepts are for the cover-art / trophy-guide / forecaster
  bounties, not this meme bounty; the meme concept here is original to
  this session (field-check driven), not from that file.
- `~/workspace/makefun/gta6-01-kit/` — checked; it is the kit for the
  separate gta6-01 game bounty, not this meme bounty. No meme kit
  exists in the workspace.

## 2. Live brief fetched (21 Nov ~15:28 UTC)

`GET https://make.fun/api/competitions/gta6-meme-x-01`:
- $500, deadline 2026-11-23T14:00:00Z, publishedAt 2026-11-19T14:00:00Z,
  submissionCount 5,098, sponsor make.fun (verified).
- Deliverables: public GitHub repo (own account, after opening, OSI
  licence), program at `main.ts` (Node 22) in root, `POST.json` at root
  naming the X post address, the X post (public account, at/after
  opening, before deadline; first picture = the meme; text carries
  make.fun and/or @makefunai + one play code), AI coding-agent
  transcripts with each submission.
- Requirements: stdlib only, no network; "AI-made pictures are fine";
  picture must show make.fun (mascot ghost, logo, or name) — a meme
  with none ranks below every meme that has one; post needs make.fun
  and/or @makefunai + one play code; Node 22.18+; public X account;
  **at most 5 submissions/day and 10 in all** (differs from the batch
  brief's "10/day, 20 total" — live brief governs).
- Judging: AI judge sees first picture + text, pairwise on: make.fun
  in picture, funniness, GTA-6-ness, how well it sells make.fun,
  caption shortness/readability, originality, picture cleanliness.
  Likes/replies/reposts never count. Top 50 share $500
  (1st $100, 2nd $60, 3rd $30, 4–10 $10, 11–50 $6).

## 3. Field-check (live leaderboard, 21 Nov ~15:35 UTC)

`GET /api/competitions/gta6-meme-x-01/leaderboard` — 3,714 ranked
entries. Top 6 (dev, provisional):
1. miku39-lab 903,832 — rental-car return receipt, "13 YEARS LATE"
2. witty-kestrel-54 903,832 — GTA V funeral bill
3. cogaich 901,748 — Leonida Mart
4. irvan-motion 901,748 — Leonida Times obituary
5. ryukein19 897,548 — GTA 6 Steam invoice, itemised
6. hitomi-agent 897,548 — Leonida Public Library overdue notice

Top-1/2/5 artifact images downloaded and viewed directly: document
format, cream/dark paper, itemised lines with prices, red stamp, ghost
mascot, Vice City sunset palette.

Keyword scan over all 3,714 titles: receipt 54, parking ticket 22,
boarding pass 62, hotel folio 16, court summons 12, impound 9,
"mission passed" 43, "wasted" 99, "loading" 109, divorce 3, alligator
3 — every document type saturated. **"shark card": 0 entries.**
Decision: Megalodon Shark Card — same winning DNA (document +
itemised numbers + "paid by my AI agent" + ghost + sunset), a document
type and joke nobody used. The $100 Shark Card vs $100 real bounty
payout is the punchline and directly sells make.fun ("real money").

## 4. Play code — NOT obtained (blocker, recorded honestly)

- Grepped all of `~/workspace/makefun` for `makefun-word-word-word`:
  only the kit's example `makefun-oak-river-lantern`. No real code on
  disk.
- `GET /api/competitions/gta6-meme-x-01/play-code` unauthenticated →
  HTTP 401. Not retried; the account API key / wallet / keypair must
  not be touched by this build, so the code could not be fetched.
- `https://make.fun/u/stellar-lumens` (public profile) fetched: handle
  stellar-lumens, GitHub stellarlumens29, no play code shown.
- Consequence: `PLAY_CODE` in `tools/build_meme.py` is the placeholder
  `makefun-___-___-___` and the image footer shows a fill-in blank.
  Regeneration after the code is supplied is a one-line change
  (see HANDOFF.md). The post-text draft likewise has `[FILL IN]`.

## 5. Build (this session, write + revise)

- Wrote `tools/build_meme.py` (Pillow + DejaVu, supersample 2×):
  sunset gradient, peeking sun, tilted Shark Card (ghost mascot drawn
  in code: white sheet body, wavy hem, sparkle eyes, pink star badge;
  chip, number `4000 2013 2026 0006`, ONE PATIENT GAMER, make.fun),
  tilted bank-statement strip (3 itemised rows + sub-lines + dotted
  leaders, red PAID stamp, TOTAL DUE $0.00), footer punchline +
  play-code line.
- Render iterations (all in-session, each re-viewed at full size):
  - v1: stamp overlapped $99.99; footer line 2 clipped at bottom edge;
    sun hidden behind card; palm silhouettes read as stray arcs.
  - v2: palms removed, sun moved to peek top-right, stamp shrunk and
    moved up, footer moved up — but TOTAL DUE collided with the
    punchline.
  - v3: receipt shortened, footer moved down — but the total divider
    struck through the third sub-line.
  - v4 (final): receipt respaced (rows step 84, divider clear of
    sub-lines, header divider shortened to clear the stamp), card
    shortened to 600px, footer at 1138/1174 — verified clean.
- Wrote `main.ts` (Node 22 stdlib only), `POST.json` (placeholder),
  `LICENSE` (MIT), `README.md`, `HANDOFF.md`, this file.
- Verified: image read at full size + 500px + 300px thumbnails +
  bottom crop; `main.ts` run twice → byte-identical sha256
  (see HANDOFF.md verification block).

## 6. Repo (this session)

- `gh` auth: stellarlumens29, HTTPS. Repo
  `stellarlumens29/gta6-meme-x-01` did not exist; created + pushed in
  this session (in-window). Homepage set to
  https://make.fun/bounty/gta6-meme-x-01. Git identity:
  stellarlumens29 / stellarlumens29@gmail.com. Commit recorded in
  HANDOFF.md / parent report.

## 7. What was NOT done (and why)

- No submit (batch rule: builds only; kit CLI flagged, no go-ahead).
- No X post (builder does not post; the user posts from @stellarlumens29).
- No play-code fetch (needs the account API key; forbidden to touch).
- No kit CLI bundle/check/submit flow (flagged on execution-risk check).
- No wallet/key/API-key access of any kind.
