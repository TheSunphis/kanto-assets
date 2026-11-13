# Route 2 — asset request (Kanto)

The Route 2 road for PokéBot, in the **Pokémon Fire Ash** style.

**20 images — the road is complete.** 5 place scenes, 3 battlefields, 3 portraits, 4 area maps, 4 story beats, 1 ringed region map. Nothing borrowed from Pika. Viridian Forest has its own set: **[`requests/viridian-forest/`](../viridian-forest/)**.

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

## Area maps and region map — included, because nothing comes from Pika any more

Earlier this README dropped both, on the assumption the Kanto overview and area art could stay shared in Pika. That is not the arrangement: **location art comes from `kanto-assets` only.** So both are here now.

| File | Shows | Weight |
|---|---|---|
| `region-maps/kanto-route-2-map-south.jpg` | Southern half: road forking north, grass patches on both shoulders, fences, boulders, town gatehouse roof at the bottom edge | 628 KB |
| `region-maps/kanto-route-2-map-south-gate.jpg` | The south gatehouse in map scale, road running through it, forest packed around | 894 KB |
| `region-maps/kanto-route-2-map-north-gate.jpg` | The north gatehouse: forest below the gate, sunlit meadow above, road continuing out | 747 KB |
| `region-maps/kanto-route-2-map-north.jpg` | Northern half: forked road climbing to the stony ridge, tall grass and rock outcrops | 730 KB |
| `region/kanto-route-2.jpg` | Kanto overview, gold ring drawn in code on the road just north of Viridian City, at the western end of the forest band — `(324, 238)`, radii `76 × 62` | 455 KB |

**One thing to be aware of:** `assets/route-2/town/` already holds eight *authentic* Fire Ash route maps derived from the Fire Ash Wiki's own `Kanto_Route_2.png`, CC BY-SA attributed in its `ATTRIBUTION.md`. These generated ones are consistent with the rest of this set's art, but they are not the official map — use whichever you prefer, and do not let both claim the same filename.

## Story beats — included, with a caveat

| File | Beat | Weight |
|---|---|---|
| `story/route-2-story-arrival.jpg` | Leaving Viridian City: fence and stone marker at the town boundary, road north between the grass | 671 KB |
| `story/route-2-story-grass.jpg` | The two big grass patches either side of the road, where the four regulars live | 1030 KB |
| `story/route-2-story-gate.jpg` | The north gatehouse, forest behind, meadow opening beyond | 769 KB |
| `story/route-2-story-pweter.jpg` | The last rise before Pewter City: grey ridge, city wall and rooftops at the top of the road | 680 KB |

**Caveat:** `bot/quests/model.py`'s `Quest` has no `picture` field, so no screen fetches quest art today. These are banked until that wiring exists.

## Battlefields — 3

The one registered key plus two location-unique variants:

| File | Field key | Weight |
|---|---|---|
| `battle/bg/kanto-route-2-and-viridian-forest.jpg` | **`kanto-route-2-and-viridian-forest`** — the registered key, south grass, scale 0.75 | 278 KB |
| `battle/bg/kanto-route-2-north.jpg` | `kanto-route-2-north` — north meadow under the stony ridge | 503 KB |
| `battle/bg/kanto-route-2-gate.jpg` | `kanto-route-2-gate` — the gatehouse as a backdrop, battler spaces clear | 745 KB |

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
