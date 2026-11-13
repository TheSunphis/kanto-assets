# Pewter City — asset request (Kanto)

Pewter City for PokéBot, in the **Pokémon Fire Ash** style.

**28 of ~33 — batches 1 to 3: the town, the gym battlefield, all seven portraits, nine story beats and the city map.** Nothing is installed; every file stays in `requests/`.

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

## Files — batch 2: the battlefield and portraits

### The gym battlefield — 1

| File | Field key | Weight |
|---|---|---|
| `battle/bg/pewter-gym.jpg` | **`pewter-gym`** — fitted at `card.FIELDS["pewter-gym"]` = `(976, 392, 458, 648)`, scale 1.0 | 336 KB |

This is the one registered battle key in the whole bot that had **no picture anywhere** since `49b2987` deleted it. Camper Liam and Brock both fight here, so until this file exists their battles are drawn on the generic `grass` fallback. The art is Fire Ash's own description of the Gym: a Japanese rock garden inside — raked pale gravel, three mossy boulders, a stone lantern, and the raised stone pedestal at the back, with the two battler spaces kept clear of clutter.

### Portraits — 5 of 7

Full-body sprites on flat cream `(244,245,227)`, 726 px tall, flush to the bottom, 2 px grid, 48 colours.

| File | `people.PERSON` key | Design | Weight |
|---|---|---|---|
| `people/brock.jpg` | `brock` — Gym Leader | Sturdy teenager, darker tan skin, half-closed eyes, spiky dark brown hair, orange sleeveless vest over a tan shirt, brown cargo trousers, grey boots, rock badge on the chest | 109 KB |
| `people/camper-liam.jpg` | `camper-liam` | Twelve, green shirt and brown shorts, red cap, bulky backpack with bedding rolled on top, dirt smudge, fist raised | 139 KB |
| `people/curator.jpg` | `curator` — Museum Curator | Late fifties, grey hair and moustache, wire glasses, brown tweed, cream shirt and bow tie, holding a fossil fragment | 119 KB |
| `people/pewter-guide.jpg` | `pewter-guide` — Gym Guide | Early thirties, grey buttoned shirt with name tag, clipboard in hand, explaining the Gym's rules | 94 KB |
| `people/pewter-clerk.jpg` | `pewter-clerk` — Mart Clerk | Mid twenties, blue-and-white cap, blue shirt with white collar, white apron, price gun and parcels | 105 KB |

| `people/pewter-nurse.jpg` | `pewter-nurse` — Nurse Joy | Adult woman, pink hair in two soft side loops, white cap with pink cross, white dress with pink trim, apron, white stockings | 105 KB |
| `people/gardener.jpg` | `gardener` | Adult woman in her forties, weathered brown skin, straw sun hat over curly hair, green shirt and canvas apron, gloves at the belt, hand trowel | 118 KB |

Both of these were held back in batch 2 — `gardener` had come out as a labelled "GBA Sprite Concept" sheet with four figures and captions, `pewter-nurse` as a coarse low-resolution block. Both are clean single figures now; the fix was dropping the concept-sheet wording and asking explicitly for one large detailed figure.

### Story beats — 2

| File | Beat | Weight |
|---|---|---|
| `story/pewter-story-arrival.jpg` | `reach-pewter` — the road from Route 2 through the south gate towers into the grey city | 511 KB |
| `story/pewter-story-badge.jpg` | `beat-brock` — the stone pedestal in the rock garden, the octagonal Boulder Badge in its case under one shaft of light | 475 KB |

### Story beats — 7 more

| File | Quest it serves | Shows | Weight |
|---|---|---|---|
| `story/pewter-story-fossil-lab.jpg` | `talk-curator` | The museum's workroom: brass resurrection machine, clamped fossil stones, amber jars, shelves of specimen boxes | 630 KB |
| `story/pewter-story-dome-helix.jpg` | `curator-twice` | Two cases side by side under spotlights — the domed fossil left, the spiralled fossil right | 504 KB |
| `story/pewter-story-gym-door.jpg` | `gym-guide-talk` | The Gym facade: doorway onto the rock garden, a lectern with an open book beside it | 488 KB |
| `story/pewter-story-gym-inside.jpg` | `beat-camper` | Inside the rock garden: raked gravel, scuffed patches where trainers stood, pedestal at the back | 573 KB |
| `story/pewter-story-east-exit.jpg` | the old man who blocks Route 3 | The east street, lowered barrier across the road, stone arch to the country beyond | 715 KB |
| `story/pewter-story-pokeball.jpg` | the hidden Poké Ball | A walled corner of bare ground and one vivid tile of light grass, with the ball tucked into the blades — **drawn in code**, since the generated version left it out | 680 KB |
| `story/pewter-story-street-corner.jpg` | `pewter-neighbours` | Two streets meeting at a paved corner: bench, dry fountain basin, stairway up between houses, evening light | 774 KB |

### Area map — 1

| File | Shows | Weight |
|---|---|---|
| `region-maps/kanto-pewter-city-map.jpg` | The whole city in map scale: gate towers at the bottom, the columned museum and its plaza to the north, the Gym beside its gravel plot, the garden quarter, rocky hills above | 737 KB |

### Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Batch 1 contact sheet — all ten town scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the gym battlefield, five portraits, two story beats |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — the two redone portraits, seven story beats, the city map |

---

## Still to come (batch 4, 5 assets)

| Contents | Count |
|---|---|
| Area maps: south gate, east exit, museum quarter | 3 |
| Region map (Kanto overview, gold ring on Pewter) | 1 |
| Labelled reference sheet with the Boulder Badge order | 1 |

---

## Install — proposal only, nothing applied yet

Per the current rule this set stays in `requests/`. When it does get installed, the layout is `assets/<location>/<category>/<file>`, so these go to `assets/pewter-city/town/`, portraits to `assets/pewter-city/people/`, and the gym battlefield to `assets/pewter-city/battle/pewter-gym.jpg`.

Two code facts worth knowing before that day:

1. `_scene_url()` in `bot/plugins/town.py` switches on a `kanto/` prefix — a scene key must read `kanto/town/pewter-center` to be served from this repo instead of Pika.
2. Portraits need adding to `KANTO_PORTRAITS`, and battle art needs the `kanto/` branch that `battle.py` still lacks.
