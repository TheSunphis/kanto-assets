# Pallet Town — asset request (Kanto)

Full remake of every Pallet Town image for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 assets**, superseding the current set in `assets/`. Everything is staged for review; nothing has been installed.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 16-bit, FireRed / Fire Ash tileset, top-down |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Scenes | 1408 × 768 JPEG q95 — fitted to 1280 × 796, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px, centred at x = 694 |
| Content rule | No characters or Pokémon in scenes; dialogue is drawn by `card.py` at runtime |

---

## Files

### 1. Building scenes — 4

Drawn by `card.town()` at 1280 × 796 field + 190 px text box.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `ash-home.jpg` | `1408 × 768` | 343 KB | `assets/town/ash-home.jpg` |
| `oak-corral.jpg` | `1408 × 768` | 505 KB | `assets/town/oak-corral.jpg` |
| `rival-house.jpg` | `1408 × 768` | 416 KB | `assets/town/rival-house.jpg` |

### 2. Story scenes — 2

The lab on revisits, and the four-ball starter-choice screen used by `/start`.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `pallet-lab-revisit.jpg` | `1408 × 768` | 370 KB | `assets/story/pallet-lab-revisit.jpg` |
| `pallet-starter-choice-4.jpg` | `1408 × 768` | 320 KB | `assets/story/pallet-starter-choice-4.jpg` |

### 3. Town view / region map — 1

`OVERVIEW['pallet-town']` and the `outside-lab` building share this one image.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `kanto-pallet-town.jpg` | `1408 × 768` | 633 KB | `assets/region/kanto-pallet-town.jpg` |

### 4. Portraits — 4

Full-body sprites on cream `(244,245,227)`, 726 px tall, 2 px grid, 48 colours.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `daisy.jpg` | `1376 × 768` | 102 KB | `assets/people/daisy.jpg` |
| `delia.jpg` | `1376 × 768` | 99 KB | `assets/people/delia.jpg` |
| `gary.jpg` | `1376 × 768` | 108 KB | `assets/people/gary.jpg` |
| `professor-oak.jpg` | `1376 × 768` | 110 KB | `assets/people/professor-oak.jpg` |

---

## Wiring notes

- `professor-oak`, `gary` and `daisy` are **not** in `PORTRAITS` / `KANTO_PORTRAITS`, so their portraits are ignored until registered:

```python
KANTO_PORTRAITS |= {'professor-oak', 'gary', 'daisy'}   # delia is already there
```

- Buildings already point at the right scene keys, so the four scene files drop straight in with no code change.

- `assets/story/pallet-starter-choice-4.jpg` is used by `start.py` as `kanto_asset("story", "pallet-starter-choice-4.jpg")` — the four Poké Ball stands match the four starter buttons.
