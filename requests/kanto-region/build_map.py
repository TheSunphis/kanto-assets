"""Build the Kanto region map: an accurate layout, painted with the AI sprite and texture library.

Coordinates are the bot's own (bot/world.py KANTO_TOWNS), so every town sits where the game says it
sits. Nothing here is invented by an image model: the geometry is code, the art is sprites.
"""
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path("/home/user/Pokebot")
sys.path.insert(0, str(ROOT / "bot"))
import world  # noqa: E402

HERE = Path("/home/user/kanto-work")
SPR = HERE / "atlas" / "sprites"
TEX = HERE / "atlas"

# ---------------------------------------------------------------- canvas and scale
U = 128                      # pixels per map unit at working resolution
K = U // 64                  # every hand-tuned pixel constant below was measured at U = 64
OX, OY = 256, 116            # where map unit (0, 0) lands
GW, GH = 1488, 1256          # working canvas
UP = 2                       # nearest-neighbour scale for the finished picture

TOWNS = {k: (v[2], v[3]) for k, v in world.KANTO_TOWNS.items()}
ROUTES = world.KANTO_ROUTES

# ---------------------------------------------------------------- accurate land shape
LAND = [
    (0.10, 1.30), (0.30, 0.85), (0.75, 0.62), (1.30, 0.48), (2.05, 0.42), (2.70, 0.55),
    (3.30, 0.72), (3.95, 0.60), (4.60, 0.50), (5.25, 0.55), (5.90, 0.42), (6.45, 0.30),
    (7.05, 0.48), (7.60, 0.72), (8.05, 1.05), (8.35, 1.55),
    (8.62, 2.10), (8.80, 2.75), (8.86, 3.35), (8.72, 3.95), (8.55, 4.45), (8.60, 4.95),
    (8.45, 5.45), (8.25, 5.95), (8.05, 6.45), (7.75, 6.95), (7.30, 7.32),
    (6.80, 7.50), (6.25, 7.55), (5.70, 7.48), (5.15, 7.35), (4.60, 7.30), (4.15, 7.15),
    (3.75, 6.95), (3.35, 6.72), (2.95, 6.55), (2.55, 6.45),
    (2.28, 6.60), (2.05, 6.74), (1.80, 6.60), (1.62, 6.30),
    (1.48, 5.95), (1.40, 5.50), (1.36, 5.05), (1.34, 4.62),
    (1.30, 3.60), (1.10, 2.60), (0.92, 1.90),
]
# The land continues west toward Johto: Routes 26/27/28 have to run off the map, not into the sea.
WEST = [(-2.60, 2.90), (-1.30, 3.05), (-0.20, 3.30), (0.80, 3.90), (1.34, 4.40), (1.36, 4.95),
        (0.60, 5.15), (-0.60, 5.25), (-2.60, 5.20)]
# Cinnabar's own island, off the south coast
CINNABAR_ISLAND = [(1.52, 8.02), (1.62, 7.72), (1.90, 7.55), (2.30, 7.52), (2.62, 7.62),
                   (2.78, 7.86), (2.72, 8.14), (2.42, 8.30), (2.02, 8.32), (1.68, 8.22)]
# Seafoam Islands, in the mouth of the bay
SEAFOAM = [(3.28, 7.98, 0.20), (3.70, 7.86, 0.17), (4.14, 8.02, 0.18)]
ISLETS = [[(6.98, 7.72), (7.22, 7.72), (7.22, 7.94), (6.98, 7.94)],
          [(8.30, 7.40), (8.62, 7.40), (8.62, 7.62), (8.30, 7.62)]]
# Water cut into the land: Vermilion's harbour, the central bay, and the inlet Silence Bridge spans
HARBOUR = [(5.80, 5.60), (6.68, 5.60), (6.72, 6.42), (6.56, 7.02), (6.20, 7.36),
           (6.00, 7.02), (5.92, 6.42)]
BAY = [(3.36, 4.30), (3.72, 4.12), (4.08, 4.26), (4.32, 4.76), (4.50, 5.34), (4.58, 5.96),
       (4.50, 6.58), (4.36, 7.06), (4.16, 7.40), (3.26, 7.42), (3.22, 6.55), (3.24, 5.72),
       (3.28, 4.95)]
INLET = [(7.74, 4.32), (9.70, 4.32), (9.70, 4.60), (7.74, 4.60)]
LAKES = [(1.95, 3.95, 0.20, 0.13, "Viridian pond"), (6.15, 1.55, 0.26, 0.16, "Cerulean lake west"),
         (6.85, 1.62, 0.20, 0.13, "Cerulean lake east"), (5.05, 6.28, 0.16, 0.11, "Safari pond"),
         (4.62, 2.62, 0.20, 0.12, "Pond")]
RIVER = [(6.05, 0.10), (6.05, 1.35), (6.55, 1.90), (6.60, 2.60)]     # Cerulean's river, Nugget Bridge over it


def P(x, y):
    return x * U + OX, y * U + OY


def poly(points):
    return [P(*c) for c in points]


# ---------------------------------------------------------------- terrain
def land_mask():
    m = Image.new("L", (GW, GH), 0)
    d = ImageDraw.Draw(m)
    d.polygon(poly(LAND), fill=255)
    d.polygon(poly(WEST), fill=255)
    for isle in ISLETS:
        d.polygon(poly(isle), fill=255)
    d.polygon(poly(CINNABAR_ISLAND), fill=255)
    for x, y, r in SEAFOAM:
        cx, cy = P(x, y)
        r = r * U
        d.ellipse((cx - r, cy - r * 0.8, cx + r, cy + r * 0.8), fill=255)
    # town ground, so a town never straddles a cut
    for key, (x, y) in TOWNS.items():
        cx, cy = P(x, y)
        r = (0.46 if key == "indigo-plateau" else 0.62) * U
        d.rectangle((cx - r, cy - r * 0.8, cx + r, cy + r * 0.8), fill=255)
    # route corridors keep the roads on land
    for a, b, name, corners in ROUTES:
        if name.startswith(("Routes 19", "Route 21")):
            continue
        d.line(route_points(a, b, corners), fill=255, width=int(0.60 * U), joint="curve")
    for line in EXTRA_ROADS:
        d.line(poly(line), fill=255, width=int(0.55 * U), joint="curve")
    # the bay and the harbour are water again, whatever the roads did
    for cut in (BAY, HARBOUR, INLET):
        d.polygon(poly(cut), fill=0)
    return m


EXTRA_ROADS = [
    [(6.0, 1.0), (6.0, -0.30), (7.3, -0.30)],          # Routes 24/25 north to Sea Cottage
    [(0.5, 4.0), (-1.9, 4.0)],                          # Route 28 west
    [(0.5, 4.0), (0.5, 5.3), (-1.9, 5.3)],              # Routes 26/27 west past Tohjo Falls
]


SEA_ROUTE_NAMES = ("Routes 19", "Route 21")


def route_points(a, b, corners):
    """Manhattan path from a to b through each corner in turn."""
    pts = [TOWNS[a]]
    for c in corners:
        pts.append(c)
    pts.append(TOWNS[b])
    out = [P(*pts[0])]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if abs(x0 - x1) > 1e-6 and abs(y0 - y1) > 1e-6:
            out.append(P(x1, y0))          # step across, then down: routes bend at right angles
        out.append(P(x1, y1))
    return out


def tile(texture, size):
    t = Image.open(texture).convert("RGB").resize((96, 96), Image.LANCZOS)
    out = Image.new("RGB", size)
    for y in range(0, size[1], 96):
        for x in range(0, size[0], 96):
            out.paste(t, (x, y))
    return out


def terrain(mask):
    img = tile(TEX / "tex-sea2.png", (GW, GH))
    land = mask
    shallow = land.filter(ImageFilter.MaxFilter(9 * K + 1)).filter(ImageFilter.GaussianBlur(2 * K))
    beach = land.filter(ImageFilter.MaxFilter(5 * K + 1)).filter(ImageFilter.GaussianBlur(1 * K))
    sea_tint = Image.new("RGB", (GW, GH), (120, 205, 235))
    img = Image.composite(sea_tint, img, shallow.point(lambda v: 120 if v > 0 else 0))
    img.paste(tile(TEX / "tex-sand.png", (GW, GH)), mask=beach)
    img.paste(tile(TEX / "tex-grass.png", (GW, GH)), mask=land)
    return img, land


def draw_path(d, points, wide=12, colour=(226, 208, 158), edge=(178, 150, 100)):
    wide = int(round(wide * K))
    for pts, col, w in ((points, edge, wide + 4 * K), (points, colour, wide)):
        d.line(pts, fill=col, width=w, joint="curve")
        for x, y in (pts[0], pts[-1]):
            r = w / 2
            d.ellipse((x - r, y - r, x + r, y + r), fill=col)


# ---------------------------------------------------------------- sprites
_cache = {}


def sprite(name, height):
    """A sprite at working resolution, bottom-anchored later, with a soft shadow baked under it."""
    if (name, height) in _cache:
        return _cache[(name, height)]
    height = int(round(height * K))
    im = Image.open(SPR / f"{name}.png").convert("RGBA")
    w = max(1, round(im.width * height / im.height))
    im = im.resize((w, height), Image.LANCZOS)
    _cache[(name, height)] = im
    return im


def place(img, name, gx, gy, height, anchor="foot", shadow=True):
    s = sprite(name, height)
    x, y = P(gx, gy)
    if anchor == "centre":
        box = (int(x - s.width / 2), int(y - s.height / 2))
    else:
        box = (int(x - s.width / 2), int(y - s.height))
    if shadow:
        d = ImageDraw.Draw(img)
        rx, ry = s.width * 0.42, max(2, s.width * 0.14)
        cx, cy = box[0] + s.width / 2, box[1] + s.height - ry * 0.6
        d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=(30, 60, 40))
    img.paste(s, box, s)
    return box


def mountain_wall(img, runs, height=46, step=0.20, jitter=0.03, rnd=None):
    """A ridge of peaks along a polyline; each peak flipped and re-sized so the range breathes."""
    for (x0, y0), (x1, y1) in runs:
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for i in range(n + 1):
            t = i / n
            gx = x0 + (x1 - x0) * t
            gy = y0 + (y1 - y0) * t
            h = (height + (rnd.randint(-6, 5) if rnd else 0))
            gy += (rnd.uniform(-0.02, 0.02) if rnd else 0)
            s = sprite("landmarks-02", int(h))
            if rnd and rnd.random() < 0.5:
                s = s.transpose(Image.FLIP_LEFT_RIGHT)
            x, y = P(gx, gy)
            img.paste(s, (int(x - s.width / 2), int(y - s.height)), s)


def scatter(img, mask, props, count, rnd, avoid):
    """Trees, bushes, boulders and flowers on open ground."""
    w, h = mask.size
    mp = mask.load()
    placed = 0
    tries = 0
    while placed < count and tries < count * 30:
        tries += 1
        x, y = rnd.randrange(w), rnd.randrange(h)
        if not mp[x, y]:
            continue
        if any((x - ax) ** 2 + (y - ay) ** 2 < ar * ar for ax, ay, ar in avoid):
            continue
        name, height = props[rnd.randrange(len(props))]
        place(img, name, (x - OX) / U, (y - OY) / U, height, shadow=False)
        placed += 1


# ---------------------------------------------------------------- buildings
HOUSE_RED, HOUSE_BLUE, HOUSE_GREEN = "buildings-01", "buildings-02", "buildings-03"
CENTER, MART, GYM = "buildings-04", "buildings-06", "buildings-07"
TOWER, DEPT, MUSEUM, PT = "buildings-05", "buildings-08", "buildings-09", "buildings-10"
LAB, MANSION = "buildings-11", "buildings-12"

# town -> [(sprite, dx, dy, height px)] with dx/dy in working pixels from the town centre
TOWN_PLAN = {
    "pallet-town": [(HOUSE_RED, -13, -3, 22), (HOUSE_BLUE, 14, -4, 22), (LAB, 1, 17, 26)],
    "viridian-city": [(CENTER, -15, -8, 20), (MART, 15, -8, 20), (GYM, -15, 12, 22), (HOUSE_GREEN, 15, 12, 22)],
    "pewter-city": [(MUSEUM, -16, -7, 26), (GYM, 15, -7, 22), (CENTER, -15, 13, 20), (MART, 15, 13, 20)],
    "cerulean-city": [(GYM, -16, -8, 22), (HOUSE_BLUE, 15, -8, 22), (CENTER, -15, 12, 20), (MART, 15, 12, 20)],
    "vermilion-city": [(CENTER, -16, -9, 20), (MART, 15, -9, 20), (GYM, -15, 11, 22), (HOUSE_RED, 15, 11, 22)],
    "lavender-town": [(PT, -16, -12, 32), (CENTER, 14, -9, 20), (MART, 14, 11, 20), (HOUSE_GREEN, -16, 10, 22)],
    "celadon-city": [(DEPT, -17, -13, 30), (GYM, 15, -12, 22), (CENTER, -16, 11, 20), (MART, 15, 11, 20), (MANSION, 0, -22, 22)],
    "saffron-city": [(TOWER, -4, -16, 40), (GYM, 15, -9, 22), (CENTER, -16, 9, 20), (MART, 13, 14, 20), (DEPT, 17, 18, 24)],
    "fuchsia-city": [(CENTER, -15, -7, 20), (MART, 15, -7, 20), (GYM, -15, 13, 22), (HOUSE_RED, 15, 13, 22)],
    "cinnabar-island": [(MANSION, -12, -6, 24), (GYM, 13, -7, 22), (LAB, -13, 14, 22), (CENTER, 13, 13, 20)],
    "indigo-plateau": [(DEPT, -4, -9, 30), (CENTER, 16, 8, 20)],
    "sea-cottage": [(HOUSE_BLUE, 0, 0, 22)],
}
PLAZA = {  # town -> half width, half height in px
    "indigo-plateau": (30 * K, 20 * K), "sea-cottage": (16 * K, 13 * K),
}


def draw_towns(img, mask):
    d = ImageDraw.Draw(img)
    for key, plan in TOWN_PLAN.items():
        cx, cy = P(*TOWNS[key])
        hw, hh = PLAZA.get(key, (31 * K, 21 * K))
        d.rounded_rectangle((cx - hw, cy - hh, cx + hw, cy + hh), 8,
                            fill=(226, 214, 184), outline=(186, 168, 128), width=2)
        for name, dx, dy, height in plan:
            s = sprite(name, height)
            box = (int(cx + dx * K - s.width / 2), int(cy + dy * K - s.height))
            d.ellipse((box[0] + s.width * 0.12, box[1] + s.height - 5,
                       box[0] + s.width * 0.88, box[1] + s.height + 3), fill=(196, 182, 150))
            img.paste(s, box, s)


# ---------------------------------------------------------------- features
def louvre(*_):
    pass


def features(img, mask, rnd):
    d = ImageDraw.Draw(img)

    # ---- woods: Viridian Forest, the Route 12/13 pines, the scrub south of Fuchsia
    for (cx, cy), rx, ry, n in [((2.05, 2.65), 0.52, 0.62, 150), ((8.25, 5.35), 0.30, 0.55, 60),
                              ((7.60, 6.45), 0.35, 0.30, 40), ((4.05, 6.95), 0.28, 0.22, 26),
                              ((6.60, 2.20), 0.34, 0.26, 34)]:
        for _ in range(n):
            gx = cx + rnd.uniform(-rx, rx)
            gy = cy + rnd.uniform(-ry, ry)
            place(img, "props-02", gx, gy, rnd.randint(17, 23), shadow=False)
    for _ in range(0):
        pass
    for _ in range(0):
        pass

    # ---- the northern range, Mt. Moon's wall, Victory Road and Rock Tunnel
    mountain_wall(img, [((-1.9, 0.55), (9.5, 0.45))], height=44, step=0.18, rnd=rnd)
    mountain_wall(img, [((3.30, 0.92), (4.72, 0.92))], height=40, step=0.16, rnd=rnd)
    mountain_wall(img, [((0.28, 1.45), (0.75, 2.75))], height=38, step=0.16, rnd=rnd)
    mountain_wall(img, [((7.72, 1.45), (8.30, 2.28))], height=38, step=0.16, rnd=rnd)

    # ---- lakes and the Cerulean river
    for gx, gy, rx, ry, _ in LAKES:
        cx, cy = P(gx, gy)
        d.ellipse((cx - rx * U - 3 * K, cy - ry * U - 3 * K, cx + rx * U + 3 * K, cy + ry * U + 3 * K), fill=(226, 198, 138))
        d.ellipse((cx - rx * U, cy - ry * U, cx + rx * U, cy + ry * U), fill=(70, 150, 214))
        d.ellipse((cx - rx * U * 0.6, cy - ry * U * 0.5, cx + rx * U * 0.2, cy + ry * U * 0.1), fill=(104, 178, 232))
    rp = poly(RIVER)
    d.line(rp, fill=(226, 198, 138), width=18 * K, joint="curve")
    d.line(rp, fill=(70, 150, 214), width=12 * K, joint="curve")

    # ---- roads: land routes, then the sea lanes
    for a, b, name, corners in ROUTES:
        if name.startswith(SEA_ROUTE_NAMES):
            continue
        draw_path(d, route_points(a, b, corners), wide=11)
    for line in EXTRA_ROADS:
        draw_path(d, poly(line), wide=10)

    # ---- sea lanes: Route 21 up to Pallet, Routes 19/20 west past the Seafoam Islands
    for a, b, name, corners in ROUTES:
        if name not in SEA_ROUTE_NAMES:
            continue
        pts = route_points(a, b, corners)
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(2, int(math.hypot(x1 - x0, y1 - y0) / (16 * K)))
            for i in range(0, n, 2):
                t0, t1 = i / n, (i + 1) / n
                d.line([(x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0),
                        (x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1)], fill=(226, 240, 250), width=2 * K)

    # ---- Indigo Plateau's rocky shelf, and the ledge country south of it
    for gx, gy, r in [(0.62, 0.86, 0.62), (0.30, 1.40, 0.34)]:
        cx, cy = P(gx, gy)
        rr = r * U
        d.ellipse((cx - rr, cy - rr * 0.72, cx + rr, cy + rr * 0.72), fill=(176, 168, 156))
        d.ellipse((cx - rr * 0.9, cy - rr * 0.62, cx + rr * 0.9, cy + rr * 0.5), fill=(196, 190, 178))

    # ---- towns on top of their roads
    draw_towns(img, mask)

    # ---- landmarks
    for gx, gy in [(3.55, 1.02), (4.45, 1.02), (8.0, 1.62), (0.5, 1.55), (2.42, 1.66), (6.9, 4.72),
                   (5.20, 0.42)]:
        place(img, "landmarks-01", gx, gy, 26, shadow=False)
    for gx, gy in [(6.0, 2.02), (6.0, 3.74), (5.0, 3.02), (7.0, 3.02)]:      # Underground Path huts
        cx, cy = P(gx, gy)
        d.rounded_rectangle((cx - 9 * K, cy - 12 * K, cx + 9 * K, cy), 3 * K, fill=(210, 200, 176), outline=(120, 110, 92), width=2 * K)
        d.rectangle((cx - 4 * K, cy - 6 * K, cx + 4 * K, cy), fill=(70, 60, 54))

    # Nugget Bridge over the Cerulean river
    nx, ny = P(6.02, -0.06)
    bridge = sprite("landmarks-03", 22)
    img.paste(bridge, (int(nx - bridge.width / 2), int(ny - bridge.height / 2)), bridge)

    # Silence Bridge across the inlet on Route 12
    rot = sprite("landmarks-03", 26).rotate(90, expand=True)
    sx, sy = P(8.0, 4.46)
    img.paste(rot, (int(sx - rot.width / 2), int(sy - rot.height / 2)), rot)

    # Cycling Road: the concrete span across the bay, north to south
    span = sprite("landmarks-04", 34)
    for i in range(8):
        gx, gy = 3.26, 4.32 + i * 0.36
        cx, cy = P(gx, gy)
        img.paste(span, (int(cx - span.width / 2), int(cy - span.height / 2)), span)

    # Vermilion: harbour wall, pier, ferry
    place(img, "landmarks-05", 6.30, 6.06, 24, shadow=False)
    place(img, "landmarks-06", 6.22, 6.48, 28, shadow=False)
    place(img, "landmarks-07", 5.96, 6.72, 18, shadow=False)

    # Power Plant, next to Rock Tunnel, reached by surfing the river beside it
    place(img, "buildings-11", 7.42, 1.88, 30)

    # Safari Zone: fenced reserve north of Fuchsia, with its gate, ponds and scattered trees
    x0, y0, x1, y1 = 4.56, 5.86, 5.52, 6.56
    (ax, ay), (bx, by) = P(x0, y0), P(x1, y1)
    for x in range(int(ax), int(bx), 8 * K):
        d.line([(x, ay), (x, ay + 8 * K)], fill=(150, 120, 80), width=2 * K)
        d.line([(x, by - 8 * K), (x, by)], fill=(150, 120, 80), width=2 * K)
    for y in range(int(ay), int(by), 8 * K):
        d.line([(ax, y), (ax, y + 8 * K)], fill=(150, 120, 80), width=2 * K)
        d.line([(bx - 2 * K, y), (bx - 2 * K, y + 8 * K)], fill=(150, 120, 80), width=2 * K)
    d.line([(ax, ay), (bx, ay)], fill=(120, 96, 64), width=2 * K)
    d.line([(ax, by), (bx, by)], fill=(120, 96, 64), width=2 * K)
    d.line([(ax, ay), (ax, by)], fill=(120, 96, 64), width=2 * K)
    d.line([(bx, ay), (bx, by)], fill=(120, 96, 64), width=2 * K)
    mid = P((x0 + x1) / 2, y1)
    d.rectangle((mid[0] - 9 * K, mid[1] - 10 * K, mid[0] + 9 * K, mid[1]), fill=(226, 214, 184), outline=(120, 96, 64), width=2 * K)
    for gx, gy in [(4.72, 6.10), (5.34, 6.02), (4.86, 6.40), (5.36, 6.38)]:
        place(img, "props-01", gx, gy, 20, shadow=False)
    cx, cy = P(4.98, 6.22)
    d.ellipse((cx - 14 * K, cy - 9 * K, cx + 14 * K, cy + 9 * K), fill=(70, 150, 214))
    d.ellipse((cx - 11 * K, cy - 7 * K, cx + 11 * K, cy + 7 * K), fill=(96, 172, 228))

    # Cinnabar: volcano, harbour
    place(img, "landmarks-08", 1.78, 7.84, 44, shadow=False)
    place(img, "landmarks-05", 2.46, 8.12, 16, shadow=False)

    # Tohjo Falls, where the west road leaves Kanto
    place(img, "landmarks-09", -0.95, 4.92, 34, shadow=False)

    # boats on the open water
    for gx, gy in [(1.30, 7.10), (2.95, 8.55), (7.60, 8.30), (8.90, 6.30), (0.30, 6.10), (4.90, 8.60)]:
        place(img, "landmarks-07", gx, gy, 18, shadow=False)

    # ---- ground cover, kept off the roads, towns and water
    avoid = [(P(*TOWNS[k])[0], P(*TOWNS[k])[1], 58 * K) for k in TOWNS]
    avoid += [(P(*c)[0], P(*c)[1], 16 * K) for c in [(3.55, 1.02), (4.45, 1.02), (8.0, 1.62), (0.5, 1.55),
                                                 (2.42, 1.66), (6.9, 4.72), (7.42, 1.88), (5.28, 6.18), (-0.52, 5.30)]]
    road_mask = Image.new("L", (GW, GH), 0)
    rd = ImageDraw.Draw(road_mask)
    for a, b, name, corners in ROUTES:
        if name.startswith(SEA_ROUTE_NAMES):
            continue
        rd.line(route_points(a, b, corners), fill=255, width=22 * K, joint="curve")
    for line in EXTRA_ROADS:
        rd.line(poly(line), fill=255, width=22 * K, joint="curve")
    free = Image.composite(Image.new("L", (GW, GH), 0), mask, Image.eval(road_mask, lambda v: 255 - v))
    free = free.point(lambda v: 255 if v > 0 else 0)
    scatter(img, free, [("props-01", 20), ("props-01", 24), ("props-02", 22), ("props-08", 14),
                        ("props-05", 12), ("props-09", 10), ("props-06", 14), ("props-10", 10)], 420, rnd, avoid)
    for a, b, name, corners in ROUTES:                       # tall grass hugging every land route
        if name.startswith(SEA_ROUTE_NAMES):
            continue
        pts = route_points(a, b, corners)
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(1, int(math.hypot(x1 - x0, y1 - y0) / (26 * K)))
            for i in range(n):
                t = (i + rnd.random()) / max(1, n)
                bx, by = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                for side in (-1, 1):
                    off = rnd.uniform(12, 26) * K * side
                    nx, ny = (by - y0), -(bx - x0)
                    norm = math.hypot(nx, ny) or 1
                    gx = (bx + nx / norm * off - OX) / U
                    gy = (by + ny / norm * off - OY) / U
                    px_, py_ = P(gx, gy)
                    if 0 <= px_ < GW and 0 <= py_ < GH and free.getpixel((int(px_), int(py_))):
                        place(img, "props-03" if rnd.random() < 0.75 else "props-04",
                              gx, gy, rnd.randint(10, 13), shadow=False)
    scatter(img, free, [("props-04", 10), ("props-03", 12)], 60, rnd, avoid)


# ---------------------------------------------------------------- assembly
def compose(seed=11):
    rnd = random.Random(seed)
    mask = land_mask()
    img, land = terrain(mask)
    features(img, land, rnd)
    return img


def finish(img):
    """Nearest-neighbour upscale and a shared 64-colour palette, so it sits with the other art."""
    big = img.resize((GW * UP, GH * UP), Image.NEAREST)
    q = big.quantize(96, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGB")
    return q


if __name__ == "__main__":
    img = compose()
    if "--preview" in sys.argv:
        img.resize((GW * 2, GH * 2), Image.NEAREST).save("/tmp/preview.png")
        print("preview written", img.size)
    else:
        out = HERE / "map"
        out.mkdir(exist_ok=True)
        master = finish(img)
        master.save("/tmp/master.png")
        print("master", master.size)
