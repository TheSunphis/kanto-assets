# Viridian City — asset request (Kanto)

Viridian City for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**24 of 24 — the set is complete.**
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

### 2. Portraits — 8

Full-body sprites on cream `(244,245,227)`, 726 px tall, 2 px grid, 48 colours.

| File | Character (`people.py` key) | Weight |
|---|---|---|
| `people/nurse-joy.jpg` | `nurse-joy` — Nurse Joy | 108 KB |
| `people/mart-clerk.jpg` | `mart-clerk` — Mart Clerk | 105 KB |
| `people/old-man.jpg` | `old-man` — the man who teaches catching | 97 KB |
| `people/granddaughter.jpg` | `granddaughter` | 112 KB |
| `people/teacher.jpg` | `teacher` — Trainers' School teacher | 104 KB |
| `people/student.jpg` | `student` | 109 KB |
| `people/bug-catcher.jpg` | `bug-catcher` | 118 KB |
| `people/gym-guide.jpg` | `gym-guide` — the official outside the gym | 111 KB |

### 3. Story beats — 6

Art for the six scripted Viridian quests. Four are interiors drawn with the same top-down camera as
the town scenes, so they read as the room you walked into.

| File | Quest (`Quests/Kanto/ViridianCity/main.py`) | Shows | Weight |
|---|---|---|---|
| `story/viridian-story-first-heal.jpg` | `first-heal` | The Pokémon Center counter and its empty healing machine | 456 KB |
| `story/viridian-story-stock-up.jpg` | `stock-up` | Inside the Poké Mart, stocked shelves and counter | 468 KB |
| `story/viridian-story-old-man.jpg` | `old-man-lesson` | The old man's living room, tea and three ball capsules on the shelf | 512 KB |
| `story/viridian-story-school.jpg` | `school-lesson` | The classroom, desks and blank blackboard | 470 KB |
| `story/viridian-story-gym-closed.jpg` | `closed-gym` | The gym doors, chained and padlocked | 445 KB |
| `story/viridian-story-team-of-three.jpg` | `team-of-three` | The chain coiled on the ground, one door ajar with light spilling out | 492 KB |

### 4. Maps — 2

| File | Dimensions | Shows | Weight |
|---|---|---|---|
| `town/viridian-town-map.jpg` | `1584 × 672` | The whole town as a map sheet: crossroads, all six buildings, the pond, the north gate | 467 KB |
| `region/kanto-viridian-city.jpg` | `1376 × 768` | Central Kanto with Viridian ringed in gold — Pewter north beyond the forest, Pallet south on its cape | 459 KB |

### 5. Battlefield — 1

| File | Dimensions | Shows | Weight |
|---|---|---|---|
| `battle/kanto-viridian-gym.jpg` | `1376 × 768` | The gym's arena floor, columns and hanging banner | 247 KB |

### 6. Reference (not installable)

| File | Purpose |
|---|---|
| `review/_viridian-city-labeled-reference.jpg` | The town sheet with all six locations numbered, for orientation only |

---

## Note on the region map

`region/kanto-viridian-city.jpg` was drawn fresh because the previous Kanto region set was deleted
from this repo in `c92f24c`. It is framed on Viridian at the centre of the image rather than being a
crop of a full Kanto map, so the gold ring is part of the artwork, not an overlay a caller applies —
if a full region map comes back later, replace this file and re-ring it at the right coordinates.

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
PORTRAITS |= {'nurse-joy', 'mart-clerk', 'old-man', 'granddaughter',
              'teacher', 'student', 'bug-catcher', 'gym-guide'}

# Quests/Kanto/ViridianCity/main.py — the six story scenes need a Quest.picture field
picture="kanto/story/viridian-story-first-heal",    # on first-heal
picture="kanto/story/viridian-story-stock-up",      # on stock-up
picture="kanto/story/viridian-story-old-man",       # on old-man-lesson
picture="kanto/story/viridian-story-school",        # on school-lesson
picture="kanto/story/viridian-story-gym-closed",    # on closed-gym
picture="kanto/story/viridian-story-team-of-three", # on team-of-three

# card.py — the gym has no field registered yet; battles there would fall back to "grass"
FIELDS["kanto-viridian-gym"] = (976, 392, 458, 648)

# region.py — the region picture is keyed by place name
def _kanto_picture(picture):
    if picture == "viridian-city":
        return kanto_asset("region", "kanto-viridian-city.jpg")

# town.py / region.py — the town sheet, if it is wired as the town view
kanto_asset("town", "viridian-town-map.jpg")
```

`viridian-gym` is reachable only once `team-of-three` is done, and `trainers.py` currently lists **no
trainers in this town at all** — so the gym has no opponent yet and the battlefield above is
future-proofing, not a present gap. The only battlefield key in the bot's data for this area is
`kanto-route-2-and-viridian-forest`, which belongs to Route 2.
