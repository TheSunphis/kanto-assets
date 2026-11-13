# Route 2 & Viridian Forest — asset request (Kanto)

Route 2 and Viridian Forest for PokéBot, in the **Pokémon Fire Ash** style.

**20 of 34 — batch 2 of 4.** Everything here is staged for review; nothing has been installed into the live asset folders yet.

---

## Fire Ash geography — two places, not one

PokéBot's code folds the forest into the road: one id, `kanto-route-2-and-viridian-forest`, one encounter pool, six buildings sharing one scene. Fire Ash does not — it keeps them apart.

> "Viridian Forest is a forest which lies between Viridian City and Pewter City in the middle of Route 2 with both the north and south entrances of Viridian Forest open to the route… The deep and sprawling forest is said to be a natural maze as many people get lost inside."
> — Pokémon Fire Ash Wiki, *Viridian Forest*

So this set is built as **two places in one folder**: the road (South Grass → gatehouse → North Grass) and the forest landmark it interrupts. Install paths are still flat `assets/` paths, so nothing here depends on that split being real in the code — but each file below is tagged with which place it belongs to.

Fire Ash's own layout, which the scenes follow:

| Spot | Fire Ash detail |
|---|---|
| Entrance glade | Light and airy, trees not thick, sun gets in; long unmaintained grass; trees in the distance shadowed |
| Deep forest | Dark and gloomy, little light, path winds around dense trees — a natural maze |
| On the way | Iconic Caterpie (Lv. 4) west of the entrance with an Antidote · hidden Poké Ball, north-east corner of the glade · second Antidote in the south-east grass patch |
| Two Bug Catchers, then | Iconic Pidgeotto (Lv. 7), also reachable through the grass path without fighting them |
| Third Bug Catcher | Guards a Potion |
| Fourth Bug Catcher | Last battle before the northern exit back onto Route 2 |

Its trainer list is the reason this set is worth doing: **Rick, Anthony, Doug and Samurai** are already the four keys in `trainers.py`, with the same teams — Rick (Caterpie 6, Weedle 6), Anthony (Caterpie 7, 8), Doug (Weedle 7), Samurai (Pinsir 7, Metapod 7).

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes and battlefields, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Battlefields | 1376 × 768 JPEG q95 — fitted to `card.py` `FIELD_H` 796 |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px flush to the bottom edge, 48 colours |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## Files

### 1. Place scenes — 9

| File | Place | Building / page | Shows | Weight |
|---|---|---|---|---|
| `town/route-2-south.jpg` | Route 2 | `locals` | South Grass: dirt road climbing north, tall grass either side, fence posts, far Viridian rooftops | 726 KB |
| `town/route-2-south-gate.jpg` | Route 2 | `south-gate` | Stone gatehouse, green tiled roof, forest wall behind, blank signboard | 755 KB |
| `town/viridian-forest.jpg` | **Forest** | `vf` — and the default scene of all six buildings | Deep canopy, mossy trail curving right, layered trunks, shelf fungus, sun shafts | 819 KB |
| `town/viridian-forest-entrance.jpg` | **Forest** | entrance glade | Fire Ash's light, airy threshold: open canopies, sun pools, long unmaintained grass, shadowed trees beyond | 884 KB |
| `town/viridian-forest-maze.jpg` | **Forest** | the maze | Dark gloomy heart: crowded knotted trunks, a path that forks and doubles back, only two thin light shafts | 638 KB |
| `town/route-2-cache.jpg` | **Forest** | `cache` — Forest Supply Stump | Hollow sawn stump as a supply cache, tin canisters, crate, lantern, green pennant | 640 KB |
| `town/route-2-north-gate.jpg` | Route 2 | `north-gate` | The gate seen from the forest side, meadow opening beyond | 819 KB |
| `town/route-2-north.jpg` | Route 2 | North Grass page | Forked path, stony outcrops, Pewter hills on the horizon | 673 KB |
| `town/route-2.jpg` | Route 2 | `/routeinfo` page `route-2` | Whole road in three bands: grassland → forest → meadow | 778 KB |

### 2. Battlefields — 3

| File | Field key | Weight |
|---|---|---|
| `battle/bg/kanto-route-2-and-viridian-forest.jpg` | **`kanto-route-2-and-viridian-forest`** — the registered key, south grass, scale 0.75, composed clear at `(987, 336)` and `(392, 654)` | 278 KB |
| `battle/bg/kanto-route-2-forest.jpg` | `kanto-route-2-forest` — forest floor, sun shafts | 646 KB |
| `battle/bg/kanto-route-2-north.jpg` | `kanto-route-2-north` — north meadow under stony hills | 503 KB |

### 3. Portraits — 7

Full-body sprites on flat cream `(244,245,227)`, 726 px tall, flush to the bottom, 2 px grid, 48 colours.

| File | `people.PERSON` key | Design | Weight |
|---|---|---|---|
| `people/route2-ranger.jpg` | `route2-ranger` — Forest Ranger | Adult man, mid-thirties, brown beard, olive ranger shirt with badge, belt pouches, wide-brim hat | 117 KB |
| `people/route2-guide.jpg` | `route2-guide` — Route 2 Guide | Adult woman, late twenties, straw sun hat, sky-blue shirt, khaki shorts, pack, rolled map | 106 KB |
| `people/route2-evolution-guides.jpg` | `route2-evolution-guides` — Route 2 Friends | **Two** ten-year-olds side by side — boy with a Poké Ball up, girl with hands on hips | 209 KB |
| `people/bug-catcher-rick.jpg` | `bug-catcher-rick` | Twelve, green shirt and cap, white-brimmed, net over the shoulder, freckles | 133 KB |
| `people/bug-catcher-anthony.jpg` | `bug-catcher-anthony` | Thirteen, straw hat, round glasses, net held in both hands — the studious one | 135 KB |
| `people/bug-catcher-doug.jpg` | `bug-catcher-doug` | Fourteen and lanky, headband instead of a cap, jar bag at the hip | 123 KB |
| `people/bug-catcher-samurai.jpg` | `bug-catcher-samurai` | The anime Samurai Fire Ash names him after: indigo kimono, grey hakama, topknot, headband, wooden sword, net | 141 KB |

### 4. Area map — 1

| File | Place | Shows | Weight |
|---|---|---|---|
| `region-maps/kanto-viridian-forest-map-north.jpg` | **Forest** north edge | Top-down forest edge breaking into bright Route 2 meadow, path out through the gap, grey stone ridge beyond | 492 KB |

### 5. Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Batch 1 contact sheet — 7 scenes + 3 battlefields |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — 7 portraits + 2 forest scenes + the north map |

---

## Still to come (batches 3–4, 14 assets)

| Batch | Contents | Count |
|---|---|---|
| 3 | Forest story beats: `walk-route-2` arrival, Iconic Caterpie, Iconic Pidgeotto, the two Bug Catchers on the path, the Potion the third guards, the fourth before the exit, Antidote stashes, `forest-first-aid` at the stump | 8 |
| 4 | Area maps: `route-2` south, `-south-gate`, forest centre, `-north-gate`, `-north`; region overview; labelled reference | 6 |

---

## Install

1. Copy into `assets/`: `town/*` → `assets/town/`, `people/*` → `assets/people/`, `battle/bg/*` → `assets/battle/bg/`.
2. `town/viridian-forest.jpg` needs no code change — all six Route 2 buildings already resolve to it.
3. The other scenes are per-building. In `bot/people.py`:

```python
Building("locals",         "Route 2 Locals",     "town/route-2-south",      ...),
Building("south-gate",     "South Gatehouse",    "town/route-2-south-gate", ...),
Building("vf",             "Viridian Forest",    "town/viridian-forest",    ...),
Building("forest-trainers","Forest Trainers",    "town/viridian-forest",    ...),
Building("cache",          "Forest Supply Stump","town/route-2-cache",      ...),
Building("north-gate",     "North Gatehouse",    "town/route-2-north-gate", ...),
```

4. Portraits: add all seven keys to `KANTO_PORTRAITS` in `bot/plugins/town.py`, otherwise they resolve to Pika (the four Bug Catchers are already in `PORTRAITS`, so they currently display Pika's art).
5. Battlefields: `battle.py` hardcodes `asset("battle", "bg", f"{name}.jpg")` with no `kanto/` branch, so these need that branch before they can be served from `kanto-assets`.
6. A Fire Ash-specific code note, not art: `spawns.py` gives the road Pidgey / Rattata / Caterpie / Weedle at Lv. 2–5. Fire Ash also puts **Pidgeotto Lv. 5** wild in the forest (a nod to the anime) and two **Iconic** encounters — Caterpie Lv. 4 and Pidgeotto Lv. 7. The Pidgeotto wild slot is missing from the pool.
