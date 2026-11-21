/**
 * gta6-meme-x-01 entry (Node 22, standard library only).
 *
 * Writes the Megalodon Shark Card meme to $MAKEFUN_OUTPUT_DIR/entry.png
 * (default /output/entry.png) and copies POST.json next to it.
 *
 * The picture lives in this repository at assets/entry.png and is copied
 * verbatim: the entry program draws nothing and fetches nothing, so the
 * output is deterministic by construction — no randomness, no clock, no
 * network, and two runs write the same bytes. The picture itself was drawn
 * in code with tools/build_meme.py (Pillow, DejaVu fonts): a Leonida Bank
 * Megalodon Shark Card over a Vice City sunset, with an itemised bank
 * statement (Shark Card $99.99 for $8,000,000 of fake money; GTA VI
 * $100.00, the actual game; paid by my AI agent's make.fun bounty payout;
 * total due $0.00) and the punchline "DON'T BUY FAKE MONEY — EARN THE
 * REAL GAME" plus make.fun and the play code.
 *
 * POST.json names the X post carrying the meme. It is a placeholder until
 * the meme is posted (see HANDOFF.md); the program copies whatever is
 * there, so fill it in before submitting.
 */

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)));
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

function main(): void {
  mkdirSync(OUTPUT_DIR, { recursive: true });
  copyFileSync(join(ROOT, "assets", "entry.png"), join(OUTPUT_DIR, "entry.png"));
  copyFileSync(join(ROOT, "POST.json"), join(OUTPUT_DIR, "POST.json"));
}

main();
