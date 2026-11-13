# Viridian Forest — asset request (Kanto)

Viridian Forest for PokéBot, in the **Pokémon Fire Ash** style.

**10 of 23 — 10 assets staged.** The road it sits inside has its own set: **[`requests/route-2/`](../route-2/)**.

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

### 4. Area map — 1

| File | Shows | Weight |
|---|---|---|
| `region-maps/kanto-viridian-forest-map-north.jpg` | Top-down forest edge breaking into bright Route 2 meadow, the path out through the gap, grey stone ridge beyond | 492 KB |

---

## Still to come (13 assets)

| Contents | Count |
|---|---|
| Story beats: arrival at the glade, Iconic Caterpie, the Antidote stashes, the two Bug Catchers on the path, Iconic Pidgeotto, the guarded Potion, the fourth before the exit, `forest-first-aid` at the stump | 8 |
| Area maps: south entrance, centre, deep maze | 3 |
| Region overview with the forest ringed | 1 |
| Labelled reference sheet with the Fire Ash route order | 1 |

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
