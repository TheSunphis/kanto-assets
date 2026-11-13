# Route 2 — asset request (Kanto)

The Route 2 road for PokéBot, in the **Pokémon Fire Ash** style.

**12 images — the road is complete.** Every scene, battlefield and portrait the bot can fetch for Route 2 is here; the two review sheets are extras. Nothing is missing. Viridian Forest has its own set: **[`requests/viridian-forest/`](../viridian-forest/)**.

**Nothing has been installed.** Every file stays in `requests/` for review — that is the current rule, and the install notes at the bottom are a proposal for later, not something applied.

---

## Why the forest is not in here

Route 2 runs Viridian City → Pewter City, and Viridian Forest interrupts it. Fire Ash keeps the forest as a **landmark with its own map and its own four trainers**, so the two are built as separate sets: this one is the road only — South Grass, the gatehouses, North Grass.

Route 2 in Fire Ash also holds the **north-western terminus of Diglett's Cave**, which the bot lists separately under `/routeinfo` → Extra (`digletts-cave`), and which is not part of this set.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes and battlefields, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Battlefields | 1376 × 768 JPEG q95 — fitted to `card.py` `FIELD_H` 796 |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px flush to the bottom, 48 colours |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## Files

### 1. Place scenes — 5

| File | Building (`people.py` key) | Shows | Weight |
|---|---|---|---|
| `town/route-2-south.jpg` | `locals` — Route 2 Locals | South Grass: dirt road climbing north, tall grass, fence posts, far Viridian rooftops | 726 KB |
| `town/route-2-south-gate.jpg` | `south-gate` — South Gatehouse | Stone gatehouse, green tiled roof, forest wall behind, blank signboard | 755 KB |
| `town/route-2-north-gate.jpg` | `north-gate` — North Gatehouse | The same gate from the far side, meadow opening beyond | 819 KB |
| `town/route-2-north.jpg` | North Grass page | Forked path, stony outcrops, Pewter hills on the horizon | 673 KB |
| `town/route-2.jpg` | `/routeinfo` page `route-2` | Whole road in three bands: grassland → forest → meadow | 778 KB |

### 2. Battlefields — 2

| File | Field key | Weight |
|---|---|---|
| `battle/bg/kanto-route-2-and-viridian-forest.jpg` | **`kanto-route-2-and-viridian-forest`** — the registered key, south grass, scale 0.75, composed clear at `(987, 336)` and `(392, 654)` | 278 KB |
| `battle/bg/kanto-route-2-north.jpg` | `kanto-route-2-north` — north meadow under stony hills | 503 KB |

### 3. Portraits — 3

| File | `people.PERSON` key | Design | Weight |
|---|---|---|---|
| `people/route2-ranger.jpg` | `route2-ranger` — Forest Ranger | Adult man, mid-thirties, beard, olive ranger shirt with badge, belt pouches, wide-brim hat | 117 KB |
| `people/route2-guide.jpg` | `route2-guide` — Route 2 Guide | Adult woman, straw sun hat, sky-blue shirt, khaki shorts, pack, rolled map | 106 KB |
| `people/route2-evolution-guides.jpg` | `route2-evolution-guides` — Route 2 Friends | **Two** ten-year-olds side by side — boy holding a Poké Ball up, girl with hands on hips | 209 KB |

### 4. Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Batch 1 — 7 scenes + 3 battlefields *(before the split; the forest files have since moved)* |
| `review/_sheet-batch-2.jpg` | Batch 2 — 7 portraits + 2 forest scenes + the north forest map *(likewise spans both sets)* |

---

## Optional extras — none of them required

The old plan here listed 10 more files. Re-checked against the bot and against what is already in `assets/`, most of them should not be made at all:

| Item | Verdict |
|---|---|
| **3 area maps** (south, gates, north grass) | **Dropped.** `assets/route-2/town/` already ships eight authentic Fire Ash route maps — `kanto-route-2-map.png` overlays endpoints and notes on the Fire Ash Wiki's own `Kanto_Route_2.png`, and `kanto-route-2-map-{south,south-gate,forest,north-gate,north,cave}.png` add bot position markers, all CC BY-SA attributed in `ATTRIBUTION.md`. Generated maps would be invented geography and strictly worse than the real ones. |
| **Region overview** | **Not needed.** The Kanto overview is shared art and stays in Pika — that is what `49b2987` settled. |
| **4 road story beats** | **Blocked, not missing.** `bot/quests/model.py`'s `Quest` has no `picture` field, so no quest image is fetched by any screen today. Writing them now buys nothing until that wiring exists. |
| **1 spare `kanto-route-2-gate` battlefield variant** | Optional cosmetic. The one registered key, `kanto-route-2-and-viridian-forest`, is covered. |
| **Labelled reference sheet** | Optional — the attributed Fire Ash route maps already do this job properly. |

## The same question applies to Viridian Forest

The forest set's four area maps are generated art of a place that also has an official map. The authentic one is `Kanto_Viridian_Forest_Map.png` on the Pokémon Fire Ash Wiki, and `assets/route-2/town/ATTRIBUTION.md` shows the exact recipe used to bring the Route 2 map in: download the wiki image, convert to PNG, overlay bot markers, keep the CC BY-SA attribution.

Doing that for the forest would be strictly better than all four of my `region-maps/` files. Say the word and I will swap them.

---

## Install — proposal only, nothing applied yet (`assets/<location>/` layout)

`kanto-assets` was reorganised in `0baa964` / `49b2987` / `6e0889c`: runtime art now lives at `assets/<location>/<category>/<file>` and `requests/` is review-only. This set installs to `assets/route-2/` — which today holds the older route-2 map art and its `ATTRIBUTION.md`, alongside `town/` and `routeinfo/`.

| From here | To |
|---|---|
| `town/*.jpg` | `assets/route-2/town/` |
| `people/*.jpg` | `assets/route-2/people/` |
| `battle/bg/*.jpg` | `assets/route-2/battle/` — battles are **location-unique**, no borrowing, so they live with the road. See [`BATTLE_ART.md`](../BATTLE_ART.md) |

Then the code:

1. All six Route 2 buildings currently resolve to `town/viridian-forest`, which lives in the forest set. Until `people.py` gives them their own scenes, that one forest file is what the road shows:

```python
Building("locals",         "Route 2 Locals",     "kanto/town/route-2-south",      ...),
Building("south-gate",     "South Gatehouse",    "kanto/town/route-2-south-gate", ...),
Building("north-gate",     "North Gatehouse",    "kanto/town/route-2-north-gate", ...),
```

2. Portraits: add all three keys to `KANTO_PORTRAITS` in `bot/plugins/town.py`, or they resolve to Pika.
3. `_scene_url()` in `town.py` switches on a `kanto/` prefix, so scene keys need it to be served from this repo.
4. Fire Ash data gap: the road's pool is Pidgey / Rattata / Caterpie / Weedle at Lv. 2–5. Fire Ash also has **Pidgeotto Lv. 5 wild** in the forest, missing from `spawns.py`.
