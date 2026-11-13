# Pallet Town — asset request (Kanto)

Every Pallet Town image for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**13 assets**, superseding the current set in `assets/`. Everything is staged for review; nothing has been installed.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px, centred at x = 694 |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## Files

### 1. Building scenes — 4

Drawn by `card.town()` at 1280 × 796 field + 190 px text box.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `town/ash-home.jpg` | `1408 × 768` | 343 KB | `town/ash-home.jpg` |
| `town/oak-corral.jpg` | `1408 × 768` | 505 KB | `town/oak-corral.jpg` |
| `town/rival-house.jpg` | `1408 × 768` | 416 KB | `town/rival-house.jpg` |
| `town/outside-lab.jpg` | `1408 × 768` | 363 KB | `town/outside-lab.jpg` |

`outside-lab` is new. The building previously borrowed `region/kanto-pallet-town.jpg`, so standing
outside the lab showed the same picture as the whole-town overview.

### 2. Story scenes — 4

The lab on revisits, the four-ball starter screen used by `/start`, and the two scripted quest beats.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `story/pallet-lab-revisit.jpg` | `1408 × 768` | 370 KB | `story/pallet-lab-revisit.jpg` |
| `story/pallet-starter-choice-4.jpg` | `1408 × 768` | 320 KB | `story/pallet-starter-choice-4.jpg` |
| `story/pallet-oak-corral.jpg` | `1408 × 768` | 433 KB | `story/pallet-oak-corral.jpg` |
| `story/pallet-rival-training.jpg` | `1408 × 768` | 366 KB | `story/pallet-rival-training.jpg` |

The last two are new and have **no consumer yet** — see the wiring notes.

### 3. Town view / region map — 1

`OVERVIEW['pallet-town']` and the `outside-lab` building share this one image.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `region/kanto-pallet-town.jpg` | `1408 × 768` | 633 KB | `region/kanto-pallet-town.jpg` |

### 4. Portraits — 4

Full-body sprites on cream `(244,245,227)`, 726 px tall, 2 px grid, 48 colours.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `people/daisy.jpg` | `1376 × 768` | 102 KB | `people/daisy.jpg` |
| `people/delia.jpg` | `1376 × 768` | 99 KB | `people/delia.jpg` |
| `people/gary.jpg` | `1376 × 768` | 108 KB | `people/gary.jpg` |
| `people/professor-oak.jpg` | `1376 × 768` | 110 KB | `people/professor-oak.jpg` |

---

## Wiring notes

### Portraits — three are ignored today

`professor-oak`, `gary` and `daisy` are **not** in `PORTRAITS` / `KANTO_PORTRAITS`, so `scene_of()`
never returns their keys and the bot never requests those files:

```python
KANTO_PORTRAITS |= {'professor-oak', 'gary', 'daisy'}   # delia is already there
```

### `outside-lab` — one line, ready to use

In `bot/people.py`, `BUILDINGS["pallet-town"]`:

```python
Building("outside-lab", "Outside Oak's Lab", "kanto/town/outside-lab", requires=("first-pokemon",)),
```

`_scene_url()` in `bot/plugins/town.py` resolves `kanto/town/outside-lab` to
`kanto_asset("town", "outside-lab.jpg")` — no other change needed.

### The two new story scenes need a `Quest.picture` field

`help-oak-corral` and `rival-training` are quest *actions*. Both fire inside buildings that already
have their own scenes, and `Quest` in `bot/quests/model.py` has no image field — epilogues render as
text over the building's scene. Until that exists, these two files are unused:

```python
# bot/quests/model.py — Quest dataclass
picture: str = ""          # optional kanto/story scene drawn with the epilogue

# bot/plugins/town.py — where the epilogue card is redrawn
if quest.picture:
    scene = _scene_url(quest.picture)

# Quests/Kanto/PalletTown/side.py
picture="kanto/story/pallet-oak-corral",     # on oak-corral-check
picture="kanto/story/pallet-rival-training", # on rival-training
```

### Already correct

Buildings point at the right scene keys, so the four building scenes drop straight in with no code
change beyond the `outside-lab` line above. `story/pallet-starter-choice-4.jpg` is fetched by
`start.py` as `kanto_asset("story", "pallet-starter-choice-4.jpg")` — the four Poké Ball stands match
the four starter buttons.
