# Viridian City — asset request (Kanto)

Viridian City for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 of 24 staged so far.** This is the first batch; the remaining 14 are listed under *Still to come*.
Everything here is staged for review; nothing has been installed into the live asset folders.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px, centred |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## Files

### 1. Place scenes — 6

One per building in `BUILDINGS["viridian-city"]`, including a dedicated Pokémon Center. That
building currently uses the shared `center/center` asset, so this is the first Viridian-specific
Center exterior.

| File | Building (`people.py` key) | Shows | Weight |
|---|---|---|---|
| `town/viridian-center.jpg` | `pc` — Pokémon Center | Red roof, glass front, round sign disc, forecourt | 419 KB |
| `town/viridian-mart.jpg` | `pm` — Poké Mart | Blue roof, striped awning, bike rack and crates | 402 KB |
| `town/viridian-road.jpg` | `nr` — North Road | Paving north to the city wall and Route 2 gate | 436 KB |
| `town/viridian-school.jpg` | `ts` — Trainers' School | School building, outdoor desks under a shelter, blank blackboard | 470 KB |
| `town/viridian-pond.jpg` | `pd` — Pond | Round ornamental pond, jetty, benches | 428 KB |
| `town/viridian-gym.jpg` | `gy` — Viridian Gym | Columned stone gym, doors chained shut | 452 KB |

### 2. Portraits — 4 of 8

Full-body sprites on cream `(244,245,227)`, 726 px tall, 2 px grid, 48 colours.

| File | Character (`people.py` key) | Weight |
|---|---|---|
| `people/nurse-joy.jpg` | `nurse-joy` — Nurse Joy | 108 KB |
| `people/mart-clerk.jpg` | `mart-clerk` — Mart Clerk | 105 KB |
| `people/old-man.jpg` | `old-man` — the man who teaches catching | 97 KB |
| `people/granddaughter.jpg` | `granddaughter` | 112 KB |

---

## Still to come — the other 14

| Group | # | Files |
|---|---|---|
| Portraits | 4 | `teacher`, `student`, `bug-catcher`, `gym-guide` |
| Story beats | 6 | `viridian-story-first-heal` (`first-heal`), `-stock-up` (`stock-up`), `-old-man` (`old-man-lesson`), `-school` (`school-lesson`), `-gym-closed` (`closed-gym`), `-team-of-three` (`team-of-three`) |
| Maps | 2 | `kanto-viridian-city.jpg` (region overview), `viridian-town-map.jpg` (town sheet) |
| Battlefield | 1 | `kanto-viridian-gym.jpg` — the gym field, for when the gym opens |
| Reference | 1 | `_viridian-city-labeled-reference.jpg`, not installable |

---

## Wiring

```python
# people.py — five of the six buildings already have Viridian-specific scene keys;
# only the Center is shared today.
Building("pc", "Pokémon Center", "kanto/town/viridian-center"),   # was center/center
Building("pm", "Poké Mart",      "kanto/town/viridian-mart"),
Building("nr", "North Road",     "kanto/town/viridian-road"),
Building("ts", "Trainers' School","kanto/town/viridian-school"),
Building("pd", "Pond",           "kanto/town/viridian-pond"),
Building("gy", "Viridian Gym",   "kanto/town/viridian-gym", requires=("team-of-three",)),

# people.py — portraits are ignored until registered
PORTRAITS |= {'nurse-joy', 'mart-clerk', 'old-man', 'granddaughter'}

# card.py — the gym has no field registered yet; battles there would fall back to "grass"
FIELDS["kanto-viridian-gym"] = (976, 392, 458, 648)
```

`viridian-gym` is reachable only once `team-of-three` is done, and `trainers.py` currently lists **no
trainers in this town at all** — so the gym has no opponent yet and the battlefield above is
future-proofing, not a present gap. The only battlefield key in the bot's data for this area is
`kanto-route-2-and-viridian-forest`, which belongs to Route 2.
