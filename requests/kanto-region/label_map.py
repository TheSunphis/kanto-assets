"""Label the composed Kantine map. Every position comes from build_map's own geometry, so a label
can only ever sit on the thing it names."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "/home/user/kanto-work")
import build_map as bm  # noqa: E402

F = "/home/user/Pokebot/bot/fonts/Jersey15-Regular.ttf"
INK, GOLD, CREAM = (14, 18, 34), (255, 203, 5), (255, 250, 235)

TOWNS = [  # key, label side
    ("indigo-plateau", "above"), ("pewter-city", "above"), ("cerulean-city", "above"),
    ("sea-cottage", "above"), ("celadon-city", "above"), ("saffron-city", "below"),
    ("lavender-town", "right"), ("vermilion-city", "right"), ("viridian-city", "left"),
    ("fuchsia-city", "below"), ("pallet-town", "left"), ("cinnabar-island", "below"),
]
SPOTS = [
    ("Viridian Forest", 2.05, 2.60, "left"), ("Mt. Moon", 4.02, 1.06, "below"),
    ("Rock Tunnel", 8.00, 1.68, "below"), ("Victory Road", 0.50, 1.95, "right"),
    ("Power Plant", 7.42, 1.86, "below"), ("Nugget Bridge", 6.02, -0.06, "above"),
    ("Cerulean Cave", 5.20, 0.42, "left"), ("Underground Path", 6.00, 3.74, "right"),
    ("Diglett's Cave", 2.42, 1.66, "left"), ("Diglett's Cave", 6.90, 4.72, "below"),
    ("Cycling Road", 3.26, 5.55, "left"), ("Silence Bridge", 8.00, 4.46, "right"),
    ("Safari Zone", 5.04, 6.20, "above"), ("Vermilion Harbour", 6.20, 6.55, "below"),
    ("Seafoam Islands", 3.70, 7.86, "below"), ("Volcano", 1.78, 7.90, "left"),
    ("Tohjo Falls", -0.95, 4.92, "below"),
]
ROUTE_PLATES = {1: (2.0, 5.0), 2: (2.0, 2.95), 3: (3.0, 1.0), 4: (5.4, 1.0), 5: (6.0, 2.0),
                6: (6.0, 4.0), 7: (5.0, 3.0), 8: (7.0, 3.0), 9: (7.0, 1.0), 10: (8.0, 1.35),
                11: (7.5, 5.0), 12: (8.0, 3.9), 13: (8.0, 6.3), 14: (7.3, 7.0), 15: (5.95, 7.0),
                16: (3.2, 3.35), 17: (3.26, 5.35), 18: (3.9, 7.0), 19: (5.0, 7.85),
                20: (4.2, 8.05), 21: (2.0, 6.9), 22: (1.3, 4.0), 23: (0.5, 3.3),
                24: (6.0, 0.2), 25: (6.65, -0.30), 26: (0.5, 4.75), 27: (-0.2, 5.3),
                28: (-1.1, 4.0)}


def plate(d, text, x, y, fnt, pad=6, box=INK, edge=GOLD, fill=CREAM):
    l, t, r, b = d.textbbox((x, y), text, font=fnt, anchor="mm")
    d.rounded_rectangle((l - pad, t - pad - 1, r + pad, b + pad + 1), 5, fill=box, outline=edge, width=2)
    d.text((x, y), text, font=fnt, fill=fill, anchor="mm")


def put(d, text, gx, gy, side, fnt, sx, sy, ox, oy):
    x = (gx * bm.U + ox) * bm.UP * sx
    y = (gy * bm.U + oy) * bm.UP * sy
    w = d.textlength(text, font=fnt)
    gap = 16
    pos = {"above": (x, y - gap - 12), "below": (x, y + gap + 12),
           "left": (x - gap - w / 2 - 6, y), "right": (x + gap + w / 2 + 6, y)}[side]
    plate(d, text, pos[0], pos[1], fnt)


def marker(d, x, y, scale=1.0):
    for r, col in ((17 * scale, INK), (13 * scale, (226, 54, 54)), (6 * scale, CREAM)):
        d.ellipse((x - r, y - r, x + r, y + r), fill=col)


def frame(img):
    d = ImageDraw.Draw(img)
    w, h = img.size
    d.rectangle((0, 0, w - 1, h - 1), outline=INK, width=16)
    d.rectangle((16, 16, w - 17, h - 17), outline=GOLD, width=4)


def overview(master, out_w=1536, towns=True, spots=True, routes=False, mark=None):
    sx = out_w / master.width
    img = master.resize((out_w, round(master.height * sx)), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    ft, fs, fr = ImageFont.truetype(F, 24), ImageFont.truetype(F, 17), ImageFont.truetype(F, 16)
    if routes:
        for n, (gx, gy) in ROUTE_PLATES.items():
            x = (gx * bm.U + bm.OX) * bm.UP * sx
            y = (gy * bm.U + bm.OY) * bm.UP * sx
            plate(d, str(n), x, y, fr, pad=5, box=(16, 30, 58), edge=(120, 190, 255), fill=(226, 240, 255))
    if spots:
        for name, gx, gy, side in SPOTS:
            put(d, name, gx, gy, side, fs, sx, sx, bm.OX, bm.OY)
    if towns:
        for key, side in TOWNS:
            name = bm.world.KANTO_TOWNS[key][0]
            put(d, name, *bm.TOWNS[key], side, ft, sx, sx, bm.OX, bm.OY)
    if mark:
        gx, gy = bm.TOWNS[mark]
        marker(d, (gx * bm.U + bm.OX) * bm.UP * sx, (gy * bm.U + bm.OY) * bm.UP * sx, 1.4)
    frame(img)
    return img


if __name__ == "__main__":
    out = Path("/home/user/kanto-work/map")
    out.mkdir(exist_ok=True)
    (out / "review").mkdir(exist_ok=True)
    master = bm.finish(bm.compose())
    master.save(out / "_master.png")
    overview(master).save(out / "kanto-map.jpg", quality=90)
    overview(master, routes=True).save(out / "review/labels-and-routes.jpg", quality=88)
    print("overview done", master.size)


def window(master, key, w=1280, h=940):
    gx, gy = bm.TOWNS[key]
    cx = (gx * bm.U + bm.OX) * bm.UP
    cy = (gy * bm.U + bm.OY) * bm.UP
    x0 = min(max(int(cx - w / 2), 0), master.width - w)
    y0 = min(max(int(cy - h / 2), 0), master.height - h)
    img = master.crop((x0, y0, x0 + w, y0 + h)).copy()
    d = ImageDraw.Draw(img)
    name = bm.world.KANTO_TOWNS[key][0]
    marker(d, cx - x0, cy - y0, 1.35)
    fnt = ImageFont.truetype(F, 46)
    tw = d.textlength(name, font=fnt)
    l, t = 40, h - 104
    d.rounded_rectangle((l, t, l + tw + 44, t + 64), 10, fill=INK, outline=GOLD, width=3)
    d.text((l + 22, t + 9), name, font=fnt, fill=GOLD)
    frame(img)
    return img


if __name__ == "__main__":
    master = Image.open(Path("/home/user/kanto-work/map/_master.png")).convert("RGB")
    out = Path("/home/user/kanto-work/map")
    for key, _ in TOWNS:
        window(master, key).save(out / f"kanto-{key}.jpg", quality=90)
        overview(master, mark=key).save(out / f"kanto-map-{key}.jpg", quality=90)
    print("written", len(list(out.glob("kanto-*.jpg"))))
