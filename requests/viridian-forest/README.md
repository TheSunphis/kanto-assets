# Viridian Forest — asset request (Kanto)

Viridian Forest for PokéBot, in the **Pokémon Fire Ash** style.

**22 of 23 — 22 assets staged.** The road it sits inside has its own set: **[`requests/route-2/`](../route-2/)**.

---

## Fire Ash says this is a place, not a stretch of road

> "Viridian Forest is a forest which lies between Viridian City and Pewter City in the middle of Route 2 with both the north and south entrances of Viridian Forest open to the route… The deep and sprawling forest is said to be a natural maze as many people get lost inside. The trees in the forest are so thick that little light gets in…"
> — Pokémon Fire Ash Wiki, *Viridian Forest*

It has its own map, its own items and its own four trainers. So it gets its own set here, and the road set stops at the gatehouses.

Fire Ash's own description, which the scenes follow:

| Spot | Fire Ash detail |
|---|---|
| Entrance glade | *"light and airy: the trees are not as thick and sunlight is able to get in fine… trees in the distance appear to be shadowed"*; long unmaintained grass |
| Deep forest | dark and gloomy, little light, the path winds around dense trees — a natural maze |
| Loot on the way | Iconic Caterpie (Lv. 4) west of the entrance with an Antidote · hidden Poké Ball, north-east corner of the glade · second Antidote in the south-east grass patch |
| Two Bug Catchers, then | Iconic Pidgeotto (Lv. 7) — also reachable through the grass path without fighting them |
| Third Bug Catcher | guards a Potion |
| Fourth Bug Catcher | last battle before the northern exit back onto Route 2 |

### The four trainers, exactly as in Fire Ash

All four keys already exist in `trainers.py` (`town = kanto-route-2-and-viridian-forest`, `field = grass`):

| Trainer | Fire Ash team | Reward |
|---|---|---|
| Bug Catcher **Rick** | Caterpie ♂ Lv. 6 · Weedle ♂ Lv. 6 | 96 |
| Bug Catcher **Anthony** | Caterpie ♂ Lv. 7 · Caterpie ♂ Lv. 8 | 128 |
| Bug Catcher **Doug** | Weedle ♂ Lv. 7 | 112 |
| Bug Catcher **Samurai** | Pinsir ♂ Lv. 7 · Metapod ♂ Lv. 7 | 112 |

### Two things Fire Ash has that `spawns.py` does not

- **Wild Pidgeotto Lv. 5** lives in the forest — the wiki flags it as "most likely to represent the events of the anime", since Pidgey normally evolves at 18.
- Two **Iconic** encounters: Caterpie Lv. 4 (west of the entrance) and Pidgeotto Lv. 7 (past the first two Bug Catchers). The bot has no Iconic-encounter data at all.

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

### 1. Scenes — 4

| File | Building / page | Shows | Weight |
|---|---|---|---|
| `town/viridian-forest.jpg` | `vf` — and **the default scene of all six Route 2 buildings**, so this is the file the whole road currently shows | Deep canopy, mossy trail curving right, layered trunks, shelf fungus, sun shafts | 819 KB |
| `town/viridian-forest-entrance.jpg` | entrance glade | The light, airy threshold: open canopies, sun pools, long grass, shadowed trees beyond | 884 KB |
| `town/viridian-forest-maze.jpg` | the maze | Dark heart: crowded knotted trunks, a path that forks and doubles back, only two thin light shafts | 638 KB |
| `town/viridian-forest-cache.jpg` | `cache` — Forest Supply Stump | Hollow sawn stump used as a supply cache, tin canisters, crate, lantern, green pennant | 640 KB |

### 2. Battlefield — 1

| File | Field key | Weight |
|---|---|---|
| `battle/bg/kanto-viridian-forest.jpg` | `kanto-viridian-forest` — forest floor, sun shafts, battler spaces at `(987, 336)` and `(392, 654)` kept clear | 646 KB |

### 3. Portraits — 4

Full-body sprites on flat cream `(244,245,227)`, 726 px tall, flush to the bottom, 2 px grid, 48 colours.

| File | `people.PERSON` key | Design | Weight |
|---|---|---|---|
| `people/bug-catcher-rick.jpg` | `bug-catcher-rick` | Twelve, green shirt and cap with white brim, net over the shoulder, freckles | 133 KB |
| `people/bug-catcher-anthony.jpg` | `bug-catcher-anthony` | Straw hat and round glasses, net held in both hands — the studious one | 135 KB |
| `people/bug-catcher-doug.jpg` | `bug-catcher-doug` | Fourteen and lanky, headband instead of a cap, jar bag at the hip | 123 KB |
| `people/bug-catcher-samurai.jpg` | `bug-catcher-samurai` | The anime Samurai Fire Ash names him after: indigo kimono, grey hakama, topknot, headband, wooden sword, net | 141 KB |

### 4. Area maps — 4

| File | Shows | Weight |
|---|---|---|
| `region-maps/kanto-viridian-forest-map-south.jpg` | The southern entrance glade in map scale: gate at the bottom, clearing, paths splitting north, canopy packed around it | 892 KB |
| `region-maps/kanto-viridian-forest-map-centre.jpg` | The maze heart: the trail forking and doubling back through dense canopy, one clearing off to the right | 878 KB |
| `region-maps/kanto-viridian-forest-map-north.jpg` | The forest edge breaking into bright Route 2 meadow, path out through the gap, grey stone ridge beyond | 492 KB |
| `region-maps/kanto-viridian-forest-map-deep.jpg` | The deepest, gloomiest canopy: one trail twisting through it in switchbacks, a dead-end stub, one hidden pocket clearing | 711 KB |

### 5. Story scenes — 8

Backdrops for the talk/quest screens, in Fire Ash's own walkthrough order. No creatures in frame — the Pokémon and items are drawn by `card.py`.

| File | Fire Ash beat | Shows | Weight |
|---|---|---|---|
| `story/…-arrival.jpg` | Entering from the south gate | Gate pillars and arch, blank signpost with a red warning triangle, bright glade beyond, shadowed trees deeper in | 866 KB |
| `story/…-antidote.jpg` | Antidote west of the entrance | A tin lying half-open in the trampled grass at the glade's edge | 695 KB |
| `story/…-ball.jpg` | Hidden Poké Ball, north-east corner of the glade | Gnarled root base, a red-and-white ball tucked in the gap, one shaft of light | 842 KB |
| `story/…-path.jpg` | The grass-less path, where two Bug Catchers wait | Narrow packed trail hemmed by walls of tall grass, bending left out of sight | 741 KB |
| `story/…-clearing.jpg` | The grassy side-clearing where the Iconic Pidgeotto waits: turf ringed by tall grass, one low branch, loose feathers and a twig nest on the ground, dappled light | 609 KB |
| `story/…-potion.jpg` | The Potion the third Bug Catcher guards | Fallen mossy log, dark hollow beneath it, a small bottle tucked in the dry earth | 571 KB |
| `story/…-exit.jpg` | The last stretch to the northern exit | Dim trunks crowding the foreground, the path running out into a glowing opening | 640 KB |
| `story/…-stump.jpg` | `forest-first-aid` — the supply stump | Hollow stump with tin and cloth, crate and lantern; one beam of late light, everything else in shade | 604 KB |

### 6. Region map — 1

| File | Dimension | Shows | Weight |
|---|---|---|---|
| `region/kanto-viridian-forest.jpg` | `1376 × 768` | Kanto overview with the gold ring drawn on the forest between Viridian City and the town north of it | 533 KB |

The ring is **drawn in code** after eye-checking the output, never requested from the model — the first attempt at a ring in this project landed a whole town away from its target. Two strokes, dark `(120,84,26)` under gold `(247,201,72)`, centred `(418, 356)` with radii `88 × 76`.

This is a **standalone stylised base**, not a crop of the bot's real Kanto map: the old Kanto set was deleted in `c92f24c`, so there was no base to ring. Swap it for a real base and re-ring when one returns to the repo.

### 7. Review

| File | Shows |
|---|---|
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — 7 story scenes + 3 area maps |
| `review/_sheet-batch-4.jpg` | Batch 4 contact sheet — the clearing, the deep-maze map, the region map |

---

## Still to come (1 asset)

| Contents | Count |
|---|---|
| `review/_viridian-forest-labeled-reference.jpg` — the whole forest laid out in Fire Ash walking order with numbered callouts drawn in code | 1 |

The Iconic Pidgeotto clearing that was held back in batch 3 is now done, regenerated with dappled light instead of a rectangular shaft.

---

## Install — and what the split still needs from the code

1. Copy into `assets/`: `town/*` → `assets/town/`, `people/*` → `assets/people/`, `battle/bg/*` → `assets/battle/bg/`. Filenames are already the keys the bot fetches.
2. **`town/viridian-forest.jpg` sorts itself out with no code change** — all six `BUILDINGS["kanto-route-2-and-viridian-forest"]` entries already resolve to it, which is exactly the scene they should show.
3. Portraits: add the four Bug Catcher keys to `KANTO_PORTRAITS` in `bot/plugins/town.py`. Note they are **already** in `PORTRAITS`, so today they display Pika's art instead.
4. Battlefield: needs a `kanto/` branch in `battle.py`, which hardcodes `asset("battle", "bg", f"{name}.jpg")`.

If you also want the code to treat the forest as its own place, as Fire Ash does, that is four small edits and no art changes:

| File | Change |
|---|---|
| `bot/world.py` | Replace the single `("viridian-city", "pewter-city", "Route 2 and Viridian Forest", [])` entry with two hops through a `viridian-forest` place, so travel and `/region` show the forest as its own stop |
| `bot/spawns.py` | Give the forest its own pool (`kanto-viridian-forest`) — a chance to add the wild Pidgeotto — and point `route-2-forest` at it |
| `bot/people.py` | Move `vf`, `forest-trainers` and `cache` under a `viridian-forest` key |
| `bot/trainers.py` | Move the four Bug Catchers' `town` to `viridian-forest`; `card.FIELDS` gets a `kanto-viridian-forest` entry |
