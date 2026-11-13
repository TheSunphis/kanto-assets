# Route 2 & Viridian Forest — asset request (Kanto)

Route 2 through Viridian Forest for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 of 32 — batch 1 of 4.** Everything here is staged for review; nothing has been installed into the live asset folders yet.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes and battlefields, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Battlefields | 1376 × 768 JPEG q95 — fitted to `card.py` `FIELD_H` 796 |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px, centred |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## What the bot expects for this road

Read out of the PokéBot source, so the files below match the keys it actually fetches.

- **Road id:** `kanto-route-2-and-viridian-forest`
- **Six buildings, one shared scene.** `people.BUILDINGS["kanto-route-2-and-viridian-forest"]` declares `locals`, `south-gate`, `vf`, `forest-trainers`, `cache` (Forest Supply Stump) and `north-gate` — and **every one of them points at the same scene key, `town/viridian-forest`**. So `town/viridian-forest.jpg` alone upgrades all six screens. The other five scene files are per-building upgrades that need one `scene=` edit each (see *Install*).
- **Areas:** `route-2` South Grass · `route-2-south-gate` · `route-2-forest` Viridian Forest · `route-2-north-gate` · `route-2-north` North Grass, plus `digletts-cave` listed under `/routeinfo` Extra.
- **`/routeinfo` pages:** `route-2` → scene `route-2`; the five area pages → scenes `route-2` and `viridian-forest`.
- **One registered battlefield key:** `kanto-route-2-and-viridian-forest`, drawn at `(987, 336, 392, 654)` with `FIELD_SCALE` **0.75**. That is why the battle art below is composed with a clear lower-left and upper-right.

---

## Files

### 1. Place scenes — 7

| File | Building (`people.py` key) | Shows | Weight |
|---|---|---|---|
| `town/viridian-forest.jpg` | `vf` — Viridian Forest *(also the default scene of all six buildings)* | Deep-canopy forest interior, mossy trail curving right, layered trunks, shelf fungus, sun shafts | 819 KB |
| `town/route-2-south.jpg` | `locals` — Route 2 Locals | South Grass: dirt road climbing north, tall grass either side, fence posts, far Viridian rooftops | 726 KB |
| `town/route-2-south-gate.jpg` | `south-gate` — South Gatehouse | Stone gatehouse, green tiled roof, forest wall behind, blank signboard | 755 KB |
| `town/route-2-cache.jpg` | `cache` — Forest Supply Stump | Hollow sawn stump as a supply cache, tin canisters, crate, lantern, green pennant | 640 KB |
| `town/route-2-north-gate.jpg` | `north-gate` — North Gatehouse | The same gate seen from the forest side, meadow opening beyond | 819 KB |
| `town/route-2-north.jpg` | — North Grass | Open meadow, forked path, stony outcrops, Pewter hills on the horizon | 673 KB |
| `town/route-2.jpg` | `/routeinfo` page `route-2` | Whole road in three bands: grassland → forest → meadow, gatehouses at both seams | 778 KB |

### 2. Battlefields — 3

| File | Field key | Weight |
|---|---|---|
| `battle/bg/kanto-route-2-and-viridian-forest.jpg` | **`kanto-route-2-and-viridian-forest`** — the registered key, south grass, treeline + dirt path, scale 0.75 | 278 KB |
| `battle/bg/kanto-route-2-forest.jpg` | `kanto-route-2-forest` — forest floor, sun shafts, battler spaces kept clean | 646 KB |
| `battle/bg/kanto-route-2-north.jpg` | `kanto-route-2-north` — north meadow under stony hills | 503 KB |

The registered key is the flattest of the three by design — it has to stay uncluttered at `(987, 336)` and `(392, 654)` where the sprites stand. Say the word and it can be regenerated with more foreground texture.

### 3. Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Contact sheet of all ten — 4 × 3 grid, in file order |

---

## Still to come (batches 2–4, 22 assets)

| Batch | Contents | Count |
|---|---|---|
| 2 | Portraits: `route2-ranger`, `route2-guide`, `route2-evolution-guides`, `bug-catcher-{rick,anthony,doug,samurai}` + 3 more | 10 |
| 3 | Story scenes: `walk-route-2` arrival, the two catches, `bug-net`, `route-2-regulars`, `stronger-still`, `forest-first-aid`, `clear-the-way` | 8 |
| 4 | Area maps ×5 (`route-2`, `-south-gate`, `-forest`, `-north-gate`, `-north`), region overview, labelled reference | 7 |

---

## Install

1. Copy the sets into `assets/`: `town/*` → `assets/town/`, `battle/bg/*` → `assets/battle/bg/`.
2. `town/viridian-forest.jpg` needs no code change — all six Route 2 buildings already resolve to it.
3. The other five scenes are per-building. In `bot/people.py`, the config lives in one place:

```python
"kanto-route-2-and-viridian-forest": (
    Building("locals",         "Route 2 Locals",     "town/route-2-south",      ...),
    Building("south-gate",     "South Gatehouse",    "town/route-2-south-gate", ...),
    Building("vf",             "Viridian Forest",    "town/viridian-forest",    ...),
    Building("forest-trainers","Forest Trainers",    "town/viridian-forest",    ...),
    Building("cache",          "Forest Supply Stump","town/route-2-cache",      ...),
    Building("north-gate",     "North Gatehouse",    "town/route-2-north-gate", ...),
)
```

4. Battlefields: `battle.py` hardcodes `asset("battle", "bg", f"{name}.jpg")`, so these must sit in **`assets/battle/bg/`** — and to be served from `kanto-assets` at all, `battle.py` needs the same `kanto/` branch `town.py` already has.
