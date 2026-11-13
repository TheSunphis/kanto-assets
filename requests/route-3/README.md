# Route 3 — asset request (Kanto)

Kanto Route 3 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**36 assets** requested. Everything here is staged for review; nothing has been installed into the live asset folders yet.

---

## Style & technical spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 16-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours shared across the whole route (green / warm brown / grey stone / sky blue) |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px, centred at x = 694 |
| Region maps | 1280 × 796 PNG with a gold position ring |
| Content rule | No characters, no Pokémon, no text — dialogue and UI are drawn by `card.py` at runtime |

---

## Files

### 1. Place scenes — 13

Assets used by `Building.scene` and drawn by `card.town()` at 1280 × 796 field + 190 px text box.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `route-3-clearing-east.jpg` | `1408 × 768` | 644 KB | `town/route-3-clearing-east.jpg` |
| `route-3-clearing.jpg` | `1408 × 768` | 645 KB | `town/route-3-clearing.jpg` |
| `route-3-grass-1.jpg` | `1408 × 768` | 771 KB | `town/route-3-grass-1.jpg` |
| `route-3-grass-2.jpg` | `1408 × 768` | 470 KB | `town/route-3-grass-2.jpg` |
| `route-3-hills.jpg` | `1408 × 768` | 876 KB | `town/route-3-hills.jpg` |
| `route-3-ledges-2.jpg` | `1408 × 768` | 535 KB | `town/route-3-ledges-2.jpg` |
| `route-3-ledges.jpg` | `1408 × 768` | 387 KB | `town/route-3-ledges.jpg` |
| `route-3-mart.jpg` | `1408 × 768` | 569 KB | `town/route-3-mart.jpg` |
| `route-3-moon-gate.jpg` | `1408 × 768` | 387 KB | `town/route-3-moon-gate.jpg` |
| `route-3-north.jpg` | `1408 × 768` | 624 KB | `town/route-3-north.jpg` |
| `route-3-pits.jpg` | `1408 × 768` | 791 KB | `town/route-3-pits.jpg` |
| `route-3-plateau.jpg` | `1408 × 768` | 425 KB | `town/route-3-plateau.jpg` |
| `route-3-story-clefairy.jpg` | `1408 × 768` | 244 KB | `town/route-3-story-clefairy.jpg` |
| `route-3.jpg` | `1584 × 672` | 671 KB | `town/route-3.jpg` |

### 2. NPC + trainer portraits — 10

Full-body sprites on flat cream `(244,245,227)`, 726 px tall, 2 px grid, 48 colours — matched to the existing `people/delia.jpg`.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `bug-catcher-colton.jpg` | `1376 × 768` | 133 KB | `people/bug-catcher-colton.jpg` |
| `bug-catcher-greg.jpg` | `1376 × 768` | 135 KB | `people/bug-catcher-greg.jpg` |
| `bug-catcher-james.jpg` | `1376 × 768` | 128 KB | `people/bug-catcher-james.jpg` |
| `lass-janice.jpg` | `1376 × 768` | 107 KB | `people/lass-janice.jpg` |
| `lass-robin.jpg` | `1376 × 768` | 108 KB | `people/lass-robin.jpg` |
| `lass-sally.jpg` | `1376 × 768` | 105 KB | `people/lass-sally.jpg` |
| `researcher.jpg` | `1376 × 768` | 110 KB | `people/researcher.jpg` |
| `route-3-mart-clerk.jpg` | `1376 × 768` | 97 KB | `people/route-3-mart-clerk.jpg` |
| `youngster-calvin.jpg` | `1376 × 768` | 108 KB | `people/youngster-calvin.jpg` |
| `youngster-joey.jpg` | `1376 × 768` | 110 KB | `people/youngster-joey.jpg` |

### 3. Battlefield backgrounds — 3

Keys must exist in `card.FIELDS` with fighter coordinates.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `kanto-route-3-cave.jpg` | `1376 × 768` | 204 KB | `battle/bg/kanto-route-3-cave.jpg` |
| `kanto-route-3-mt-moon-and-route-4.jpg` | `1376 × 768` | 225 KB | `battle/bg/kanto-route-3-mt-moon-and-route-4.jpg` |
| `kanto-route-3-plateau.jpg` | `1376 × 768` | 249 KB | `battle/bg/kanto-route-3-plateau.jpg` |

### 4. /routeinfo backdrop — 1

Background behind the encounter table on the Route 3 page.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `route-3.jpg` | `1376 × 768` | 363 KB | `routeinfo/route-3.jpg` |

### 5. /region area maps — 8

Marked crops of `route-3.jpg`. Consumed by `_route_map_asset()` once area markers are registered.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `kanto-route-3-map-clearing.png` | `1280 × 796` | 308 KB | `town/kanto-route-3-map-clearing.png` |
| `kanto-route-3-map-gate.png` | `1280 × 796` | 385 KB | `town/kanto-route-3-map-gate.png` |
| `kanto-route-3-map-grass-east.png` | `1280 × 796` | 356 KB | `town/kanto-route-3-map-grass-east.png` |
| `kanto-route-3-map-grass-west.png` | `1280 × 796` | 408 KB | `town/kanto-route-3-map-grass-west.png` |
| `kanto-route-3-map-ledges-2.png` | `1280 × 796` | 266 KB | `town/kanto-route-3-map-ledges-2.png` |
| `kanto-route-3-map-ledges.png` | `1280 × 796` | 298 KB | `town/kanto-route-3-map-ledges.png` |
| `kanto-route-3-map-north.png` | `1280 × 796` | 365 KB | `town/kanto-route-3-map-north.png` |
| `kanto-route-3-map-plateau.png` | `1280 × 796` | 351 KB | `town/kanto-route-3-map-plateau.png` |

### Reference

| File | Size | Purpose |
|---|---|---|
| `_route-3-labeled-reference.jpg` | 1584 × 672 | The route map with all 13 locations numbered and named — for orientation only, **not** an installable asset |

---

## Where each file goes

The bot fetches these over HTTP, so they must land in the asset repository, not the bot repository.

| Group | Destination |
|---|---|
| Scenes, region maps | `TheSunphis/Pika` → `assets/town/` |
| Portraits | `TheSunphis/Pika` → `assets/people/` |
| Battlefields | `TheSunphis/Pika` → `assets/battle/bg/` |
| `/routeinfo` backdrop | `TheSunphis/Pika` → `assets/routeinfo/` |

`bot/config.py` resolves `asset()` against `ASSETS_URL` = `https://raw.githubusercontent.com/TheSunphis/Pika/main/assets` and `kanto_asset()` against the Kanto repo. Any file that belongs in the Kanto repo should be moved under its `assets/` tree before release.

---

## Code changes these assets expect

```python
# card.py — battlefield registrations (missing entries silently fall back to "grass")
FIELDS["kanto-route-3-plateau"] = (976, 392, 458, 648)
FIELDS["kanto-route-3-cave"]    = (976, 392, 458, 648)

# people.py — 10 portraits must be registered or scene_of() ignores the files
PORTRAITS |= {'bug-catcher-colton', 'lass-janice', 'youngster-joey', 'bug-catcher-greg',
              'youngster-calvin', 'lass-sally', 'bug-catcher-james', 'lass-robin',
              'route-3-mart-clerk', 'researcher'}

# region.py — area markers so the 8 region maps are used
markers[ROUTE3_MOON_ROUTE4] = ({'route-3-clearing': 'clearing', 'route-3-north': 'north', ...}, 'kanto-route-3-map')
```
