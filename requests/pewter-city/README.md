# Pewter City — asset request (Kanto)

Pewter City for PokéBot, in the **Pokémon Fire Ash** style.

**10 of ~32 — batch 1 of 4: the town itself.** Nothing is installed; every file stays in `requests/`.

---

## What the bot expects here

Read out of the PokéBot source, so the files below match the keys it actually fetches.

- **Location id:** `pewter-city`
- **Five buildings** in `people.BUILDINGS["pewter-city"]`:

| Key | Name | Scene key it fetches | Gym gate |
|---|---|---|---|
| `pc` | Pokémon Center | `town/pewter-center` | — |
| `pm` | Poké Mart | `town/pewter-mart` | — |
| `mu` | Pewter Museum | `town/pewter-museum` | — |
| `fg` | Flower Garden | `town/pewter-garden` | — |
| `gy` | Pewter Gym | `town/pewter-gym` | `requires=("ready-for-rock",)` |

- **Seven people:** `pewter-nurse`, `pewter-clerk`, `curator`, `gardener`, `pewter-guide`, `camper-liam`, `brock`
- **Two trainers, both on `pewter-gym`:** Camper Liam, then Brock. That field key has **no picture at all** since `49b2987` deleted it — today those two battles render on the generic `grass` fallback. Fixing that is batch 2. See [`BATTLE_ART.md`](../BATTLE_ART.md).
- **Fifteen quests:** `reach-pewter`, `visit-museum`, `ready-for-rock`, `gym-guide-talk`, `beat-camper`, `beat-brock`, `talk-curator`, `curator-twice`, `garden-walk`, `no-faint-camper`, `rematch-camper`, `badge-on-card`, `talk-gardener`, `pewter-neighbours`, `pewter-everyone`

---

## Fire Ash's Pewter City, which the scenes follow

> "Pewter City is a city located in northwestern Kanto… The city has two exits. To the east is Route 3, leading to Route 4 and Mt. Moon. To the south is Route 2, leading to Viridian City."
> — Pokémon Fire Ash Wiki, *Pewter City*

| Detail | Where it lands |
|---|---|
| **Museum of Science in the northern part of the city**; a scientist revives Fossils, another explains most fossil Pokémon are Rock-type | `town/pewter-museum.jpg`, `town/pewter-museum-hall.jpg` |
| **Gym is "a small building with a Japanese rock garden inside, one Trainer and Brock waiting on a large stone pedestal"** | `town/pewter-gym.jpg` — small and plain outside, raked gravel, three boulders, stone lantern and the pedestal visible through the open door |
| **An old man stops you leaving through Route 3** without the Boulder Badge | `town/pewter-east-road.jpg` — the east exit, with the stone arch and a barrier bar across the road |
| **Hidden Poké Ball at the north-western end, in the single light-coloured grass tile** | `town/pewter-northwest.jpg` — bare ground, broken walls, and one bright square of light grass |
| Boulder Badge + TM080 Rock Slide from Brock; TM037 Sandstorm from Forrest | story beats, batch 3 |

Everything else follows the city's own character: grey-brown stone blocks, slate roofs, slab paving, bare rocky hills closing the skyline.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes and battlefields, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px flush to the bottom, 48 colours |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## Files — 10 town scenes

| File | `people.py` key | Shows | Weight |
|---|---|---|---|
| `town/pewter-center.jpg` | `pc` ✅ existing key | Pale stone Centre, wide red roof, white circular emblem, grey slab forecourt, hills behind | 730 KB |
| `town/pewter-mart.jpg` | `pm` ✅ existing key | Blue roof, striped awning, crates and handcart, street lamp, box hedges | 724 KB |
| `town/pewter-museum.jpg` | `mu` ✅ existing key | Columned limestone museum, pediment with a shell-and-tusk carving, fossil statues on plinths, wide steps | 614 KB |
| `town/pewter-garden.jpg` | `fg` ✅ existing key | Flower beds between boulders, gravel paths, benches, stone water channel, rooftops behind | 869 KB |
| `town/pewter-gym.jpg` | `gy` ✅ existing key | Small plain stone Gym; through the doorway the rock garden, raked gravel and the stone pedestal | 414 KB |
| `town/pewter-south-gate.jpg` | **new key** | Southern entrance from Route 2: twin stone towers, crenellated wall, blank signpost, green road outside | 934 KB |
| `town/pewter-east-road.jpg` | **new key** | Eastern exit toward Route 3: stone arch, streets narrowing, barrier bar across the road | 796 KB |
| `town/pewter-street.jpg` | **new key** | Residential street: stone houses with slate roofs, water pump, handcart, crates, rock faces behind | 472 KB |
| `town/pewter-northwest.jpg` | **new key** | North-west end: broken walls, leaning gate, bare rocky slope, one bright patch of light grass | 740 KB |
| `town/pewter-museum-hall.jpg` | **new key** | Museum interior: checker marble, columns, glass cases with dome-backed and spiral-shelled fossil skeletons | 510 KB |

Five files drop straight onto the existing building keys with no code change. The other five are extra scenes — the city gates, the street, the north-west corner and the museum hall — and each needs one new `Building(...)` entry if you want it reachable.

### Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Contact sheet of all ten town scenes |

---

## Still to come (batches 2–4, ~22 assets)

| Batch | Contents | Count |
|---|---|---|
| 2 | **`pewter-gym` battlefield — the one registered battle key with no art anywhere**, plus 7 portraits (`pewter-nurse`, `pewter-clerk`, `curator`, `gardener`, `pewter-guide`, `camper-liam`, `brock`) | 8 |
| 3 | Story beats: arrival (`reach-pewter`), museum (`visit-museum`, `talk-curator`, `curator-twice`), the gym door guide, `beat-camper`, `beat-brock` and the Boulder Badge, the old man at the east exit, the hidden Poké Ball | 8 |
| 4 | Area maps (city, south gate, east exit, museum quarter), region map, labelled reference | 6 |

---

## Install — proposal only, nothing applied yet

Per the current rule this set stays in `requests/`. When it does get installed, the layout is `assets/<location>/<category>/<file>`, so these go to `assets/pewter-city/town/`, portraits to `assets/pewter-city/people/`, and the gym battlefield to `assets/pewter-city/battle/pewter-gym.jpg`.

Two code facts worth knowing before that day:

1. `_scene_url()` in `bot/plugins/town.py` switches on a `kanto/` prefix — a scene key must read `kanto/town/pewter-center` to be served from this repo instead of Pika.
2. Portraits need adding to `KANTO_PORTRAITS`, and battle art needs the `kanto/` branch that `battle.py` still lacks.
