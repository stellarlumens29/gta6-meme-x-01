"""Build script for gta6-meme-x-01: the Megalodon Shark Card meme.

Draws a 1200x1200 meme with Pillow + DejaVu fonts (supersampled 2x, then
downscaled). The picture itself is drawn entirely in code here; main.ts
(Node 22, stdlib only) just copies the bundled PNG verbatim, so the graded
program is deterministic by construction.

Concept (chosen after a live field-check of the 3,714-entry leaderboard,
21 Nov 2026 ~15:35 UTC): the field is saturated with fake-document jokes
(receipts, obituaries, invoices, overdue notices, parking tickets,
boarding passes, hotel folios, court summons — every document type has
dozens of entries). The ONE iconic GTA money joke nobody used: the Shark
Card (0 entries for "shark card" in all 3,714 titles). A Megalodon Shark
Card mockup + an itemised bank statement: Rockstar sells $8,000,000 of
fake money for $100; my AI agent earned $100 of REAL money on make.fun
and bought the actual game. Same winning DNA as the top 6 (document +
itemised numbers + "paid by my AI agent" + make.fun ghost + Vice City
sunset palette), different document, different joke.

Layout (1200x1200):
  - Vice City sunset background (purple -> magenta -> orange), sun, two
    palm silhouettes
  - Big "LEONIDA BANK — MEGALODON SHARK CARD" credit card (the hero)
  - Cream bank-statement strip, itemised, with a small red PAID stamp
  - One-line punchline footer with make.fun + play code

PLAY_CODE: fill in the account's real play code (makefun-word-word-word)
before posting. It is NOT in this session (the play-code endpoint needs
the account API key, which this build must not touch). Regenerate with:
    python3 tools/build_meme.py
and re-push. Until then the image renders the code as a fill-in blank.

Deterministic: fixed constants only, no randomness, no time, no network.
Run: python3 tools/build_meme.py  ->  assets/entry.png
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "entry.png"

SIZE = 1200
SS = 2  # supersample


def s(v):
    return v * SS


# ---------------------------------------------------------------- constants
# PLAY CODE -- FILL IN before posting (see module docstring). Rendered as a
# blank until then; the build is otherwise final.
PLAY_CODE = "makefun-___-___-___"

# Palette
NAVY_CARD = (16, 28, 63)
PINK = (255, 64, 160)
PINK_SOFT = (255, 120, 190)
GOLD = (232, 196, 96)
GOLD_DARK = (176, 138, 48)
CREAM = (255, 248, 231)
CREAM_EDGE = (232, 214, 178)
INK = (26, 22, 40)
INK_SOFT = (88, 80, 110)
RED = (198, 32, 40)
WHITE = (255, 255, 255)
SUNSET_TOP = (26, 11, 46)
SUNSET_MID = (122, 32, 96)
SUNSET_LOW = (232, 96, 61)
SUNSET_HORIZON = (255, 196, 107)
PALM = (28, 11, 51)
GHOST_WHITE = (255, 255, 255)
GHOST_OUTLINE = (20, 20, 40)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, s(size))


def star4(cx, cy, r):
    """4-point sparkle star polygon points (scaled coords)."""
    k = 0.30
    return [
        (cx, cy - r), (cx + r * k, cy - r * k),
        (cx + r, cy), (cx + r * k, cy + r * k),
        (cx, cy + r), (cx - r * k, cy + r * k),
        (cx - r, cy), (cx - r * k, cy - r * k),
    ]


def star5(cx, cy, r_out, r_in):
    """5-point star polygon points (scaled coords)."""
    pts = []
    for i in range(10):
        r = r_out if i % 2 == 0 else r_in
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_ghost(d, cx, cy, w, h):
    """make.fun-style sheet ghost: white body, wavy hem, sparkle eyes,
    pink star badge. (cx, cy) = body centre, w/h in UNSCALED px."""
    x0, x1 = s(cx - w / 2), s(cx + w / 2)
    top = s(cy - h / 2)
    dome_cy = top + s(w) / 2
    bottom = s(cy + h / 2)
    pts = []
    # Dome: top half of the circle, left -> top -> right.
    for deg in range(180, 361, 6):
        a = math.radians(deg)
        pts.append((s(cx) + s(w) / 2 * math.cos(a),
                    dome_cy + s(w) / 2 * math.sin(a)))
    # Wavy hem: right -> left, 3 waves.
    n_wave = 90
    for i in range(n_wave + 1):
        x = x1 - (x1 - x0) * i / n_wave
        y = bottom - s(16) * (0.5 + 0.5 * math.sin(i / n_wave * math.pi * 6))
        pts.append((x, y))
    d.polygon(pts, fill=GHOST_WHITE, outline=GHOST_OUTLINE, width=s(5))
    # Sparkle eyes.
    eye_y = dome_cy + s(h) * 0.10
    eye_dx = s(w) * 0.22
    eye_r = s(w) * 0.085
    d.polygon(star4(s(cx) - eye_dx, eye_y, eye_r), fill=(18, 18, 34))
    d.polygon(star4(s(cx) + eye_dx, eye_y, eye_r), fill=(18, 18, 34))
    # Pink badge with white star, lower right of the body.
    bx, by = s(cx) + s(w) * 0.26, dome_cy + s(h) * 0.26
    br = s(w) * 0.16
    d.ellipse([bx - br, by - br, bx + br, by + br], fill=PINK,
              outline=GHOST_OUTLINE, width=s(3))
    d.polygon(star5(bx, by, br * 0.62, br * 0.26), fill=WHITE)


def vgrad(img, top, mid, low, horizon):
    """Vertical sunset gradient across the whole image."""
    w, h = img.size
    px = img.load()
    stops = [(0.0, top), (0.38, mid), (0.68, low), (1.0, horizon)]
    for y in range(h):
        t = y / (h - 1)
        col = stops[-1][1]
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i + 1]
            if t0 <= t <= t1:
                f = (t - t0) / (t1 - t0) if t1 > t0 else 0
                col = tuple(int(c0[k] + (c1[k] - c0[k]) * f) for k in range(3))
                break
        for x in range(w):
            px[x, y] = col


def dotted_leader(d, x0, x1, y, fill, step=14, r=3):
    """Dotted leader between label and price (unscaled coords)."""
    x = x0
    while x <= x1:
        d.ellipse([s(x), s(y - r), s(x + r * 2), s(y + r)], fill=fill)
        x += step


def build_card():
    """The Shark Card on its own layer (so it can be tilted)."""
    cw, ch = 1060, 600
    layer = Image.new("RGBA", (s(cw + 80), s(ch + 80)), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    ox, oy = s(40), s(40)
    d.rounded_rectangle([ox - s(10), oy - s(6), ox + s(cw) + s(10), oy + s(ch) + s(6)],
                        radius=s(36), fill=(255, 64, 160, 90))
    d.rounded_rectangle([ox, oy, ox + s(cw), oy + s(ch)], radius=s(30),
                        fill=NAVY_CARD + (255,), outline=(255, 120, 190, 255), width=s(4))
    d.rounded_rectangle([ox + s(16), oy + s(16), ox + s(cw) - s(16), oy + s(ch) - s(16)],
                        radius=s(22), outline=(120, 140, 200, 160), width=s(2))
    f_small = font(FONT_BOLD, 30)
    d.text((ox + s(44), oy + s(36)), "LEONIDA BANK", font=f_small,
           fill=(170, 180, 215, 255))
    d.text((ox + s(cw) - s(44), oy + s(36)), "V  →  VI", font=f_small,
           fill=PINK_SOFT + (255,), anchor="ra")
    f_big = font(FONT_BOLD, 96)
    d.text((ox + s(44), oy + s(96)), "MEGALODON", font=f_big, fill=WHITE + (255,))
    f_mid = font(FONT_BOLD, 58)
    d.text((ox + s(46), oy + s(196)), "S H A R K   C A R D", font=f_mid,
           fill=PINK_SOFT + (255,))
    # Chip, left.
    chip_x, chip_y = ox + s(44), oy + s(300)
    d.rounded_rectangle([chip_x, chip_y, chip_x + s(128), chip_y + s(96)],
                        radius=s(14), fill=GOLD + (255,), outline=GOLD_DARK + (255,),
                        width=s(3))
    d.line([chip_x + s(64), chip_y, chip_x + s(64), chip_y + s(96)],
           fill=GOLD_DARK + (255,), width=s(3))
    d.line([chip_x, chip_y + s(48), chip_x + s(128), chip_y + s(48)],
           fill=GOLD_DARK + (255,), width=s(3))
    d.line([chip_x + s(24), chip_y, chip_x + s(24), chip_y + s(48)],
           fill=GOLD_DARK + (255,), width=s(2))
    d.line([chip_x + s(104), chip_y + s(48), chip_x + s(104), chip_y + s(96)],
           fill=GOLD_DARK + (255,), width=s(2))
    # Ghost on the card, right side (unscaled coords in the layer).
    draw_ghost(d, 950, 370, 210, 250)
    # Card number.
    f_num = font(FONT_MONO, 46)
    d.text((ox + s(44), oy + s(424)), "4000  2013  2026  0006", font=f_num,
           fill=WHITE + (255,))
    # Bottom row.
    f_bot = font(FONT_BOLD, 30)
    d.text((ox + s(44), oy + s(512)), "ONE PATIENT GAMER", font=f_bot,
           fill=(200, 208, 235, 255))
    d.text((ox + s(44), oy + s(552)), "VALID THRU  11 / 26", font=f_bot,
           fill=(150, 160, 200, 255))
    d.text((ox + s(cw) - s(44), oy + s(512)), "make.fun", font=f_bot,
           fill=PINK_SOFT + (255,), anchor="ra")
    d.text((ox + s(cw) - s(44), oy + s(552)), "REAL MONEY, NOT FAKE", font=f_bot,
           fill=(150, 160, 200, 255), anchor="ra")
    return layer


def build_receipt():
    """Itemised bank-statement strip on its own layer (slight tilt)."""
    rw, rh = 1060, 400
    layer = Image.new("RGBA", (s(rw + 80), s(rh + 80)), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    ox, oy = s(40), s(40)
    d.rounded_rectangle([ox - s(8), oy - s(4), ox + s(rw) + s(8), oy + s(rh) + s(4)],
                        radius=s(24), fill=(0, 0, 0, 70))
    d.rounded_rectangle([ox, oy, ox + s(rw), oy + s(rh)], radius=s(20),
                        fill=CREAM + (255,), outline=CREAM_EDGE + (255,), width=s(3))
    f_head = font(FONT_BOLD, 26)
    d.text((ox + s(40), oy + s(16)), "LEONIDA BANK  —  STATEMENT", font=f_head,
           fill=INK_SOFT + (255,))
    # Mini PAID stamp, header right (drawn on its own rotated layer).
    stamp = Image.new("RGBA", (s(200), s(70)), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sf = font(FONT_BOLD, 34)
    sd.rounded_rectangle([s(6), s(6), s(194), s(64)], radius=s(10),
                         outline=RED + (255,), width=s(5))
    sd.text((s(100), s(35)), "PAID", font=sf, fill=RED + (255,), anchor="mm")
    stamp = stamp.rotate(-8, expand=True, resample=Image.BICUBIC)
    layer.alpha_composite(stamp, (ox + s(rw) - s(230), oy + s(2)))
    d.line([ox + s(40), oy + s(58), ox + s(rw) - s(280), oy + s(58)],
           fill=CREAM_EDGE + (255,), width=s(2))
    rows = [
        ("MEGALODON SHARK CARD", "$99.99", "$8,000,000 in fake Vice City dollars"),
        ("GRAND THEFT AUTO VI", "$100.00", "the actual game, launch week"),
        ("PAID BY MY AI AGENT", "-$100.00", "make.fun bounty payout — real money"),
    ]
    f_row = font(FONT_MONO, 34)
    f_sub = font(FONT_REG, 24)
    y = oy + s(78)
    for label, price, sub in rows:
        d.text((ox + s(40), y), label, font=f_row, fill=INK + (255,))
        pw = d.textlength(price, font=f_row)
        d.text((ox + s(rw) - s(40), y), price, font=f_row, fill=INK + (255,),
               anchor="ra")
        lx = (ox + s(40) + d.textlength(label, font=f_row) + s(18)) / SS
        rx = (ox + s(rw) - s(40) - pw - s(18)) / SS
        dotted_leader(d, lx, rx, (y + s(22)) / SS, (150, 140, 120, 255))
        d.text((ox + s(40), y + s(36)), sub, font=f_sub, fill=INK_SOFT + (255,))
        y += s(84)
    d.line([ox + s(40), y - s(12), ox + s(rw) - s(40), y - s(12)],
           fill=INK + (255,), width=s(3))
    f_tot = font(FONT_BOLD, 40)
    d.text((ox + s(40), y), "TOTAL DUE", font=f_tot, fill=INK + (255,))
    d.text((ox + s(rw) - s(40), y), "$0.00", font=f_tot, fill=RED + (255,),
           anchor="ra")
    return layer


def main():
    W = s(SIZE)
    img = Image.new("RGB", (W, W))
    vgrad(img, SUNSET_TOP, SUNSET_MID, SUNSET_LOW, SUNSET_HORIZON)
    base = img.convert("RGBA")

    # Small sun peeking above the card's top-right corner.
    glow = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    sun_cx, sun_cy, sun_r = s(1080), s(45), s(60)
    for mult, alpha in ((1.6, 50), (1.25, 90)):
        r = sun_r * mult
        gd.ellipse([sun_cx - r, sun_cy - r, sun_cx + r, sun_cy + r],
                   fill=(255, 214, 130, alpha))
    gd.ellipse([sun_cx - sun_r, sun_cy - sun_r, sun_cx + sun_r, sun_cy + sun_r],
               fill=(255, 236, 190, 255))
    base = Image.alpha_composite(base, glow)

    # Shark Card, tilted -2 degrees. Layer is 1140x720 unscaled.
    card = build_card().rotate(-2, expand=True, resample=Image.BICUBIC)
    base.alpha_composite(card, (s(20), s(40)))

    # Receipt strip, tilted +1 degree. Layer is 1140x470 unscaled.
    receipt = build_receipt().rotate(1, expand=True, resample=Image.BICUBIC)
    base.alpha_composite(receipt, (s(30), s(660)))

    # Footer punchline.
    d = ImageDraw.Draw(base)
    f_foot = font(FONT_BOLD, 36)
    d.text((s(600), s(1138)), "DON'T BUY FAKE MONEY — EARN THE REAL GAME",
           font=f_foot, fill=WHITE, anchor="mm",
           stroke_width=s(2), stroke_fill=(20, 8, 40))
    f_code = font(FONT_BOLD, 26)
    d.text((s(600), s(1174)), f"make.fun  ·  play code: {PLAY_CODE}",
           font=f_code, fill=(255, 205, 230), anchor="mm",
           stroke_width=s(2), stroke_fill=(20, 8, 40))

    out = base.convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.save(OUT, format="PNG")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
