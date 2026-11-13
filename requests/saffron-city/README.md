# Saffron City — asset request (Kanto)

Saffron City for PokéBot, in the **Pokémon Fire Ash** style.

**10 of ~40 — batch 1 of 4: the city itself.** Nothing is installed; every file stays in `requests/`.

---

## Saffron is the one Kanto town the bot has not wired at all

Every other set so far arrived at a town that already declared its buildings. Saffron does not. Checked directly against the bot source:

| Where | Saffron today |
|---|---|
| `world.KANTO_TOWNS` | **present** — "The city at the centre of Kanto where four roads meet.", map position `6, 3` |
| `world.KANTO_ROUTES` | **four links in and out** — Route 5 from Cerulean, Route 6 to Vermilion, Route 7 to Celadon, Route 8 to Lavender. The busiest crossroads in Kanto. |
| `people.BUILDINGS` | **no entry at all** — no scene keys, so the town has nothing to open |
| `people.PEOPLE` | **no people** — no nurse, no clerk, no Gym Leader |
| `card.FIELDS` | **no battlefield** — no `saffron-gym`, no dojo field |
| `people.OVERVIEW` | **no entry** |
| `assets/saffron-city/` | only `region/kanto-map-saffron-city.jpg` and `region/kanto-saffron-city.jpg` |

So this set cannot be a drop-in replacement the way Pewter's and Cerulean's were. It has to **propose** its keys, and the wiring above has to be written for the art to appear. The proposal is at the bottom of this file — `Building(...)` entries, `Person(...)` keys and the two battle fields.

The one good inheritance: `OVERVIEW` for a town follows `region/kanto-<town>`, and `assets/saffron-city/region/kanto-saffron-city.jpg` already exists under exactly that name.

---

## A note on sourcing

The Pokémon Fire Ash Wiki **has no Saffron City page** — the article exists but renders empty, the same as Cerulean's. So these scenes come from FRLG and anime canon plus what the bot declares: Sabrina's psychic Gym, the occupied Silph Co. tower, the Fighting Dojo next door with its gift Hitmonlee or Hitmonchan, Copycat's house, Mr. Psychic's house, the Trainer Fan Club, and the four gates that make Saffron what it is.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, city exteriors |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes and battlefields, 48 for portraits |
| Town scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Battlefields | 1376 × 768 JPEG q95 — fitted to `card.py` `FIELD_H` 796 |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px flush to the bottom, 48 colours |
| Content rule | **A place carries nobody.** Town scenes, battlefields, area maps and region views stay empty of people and Pokémon — every figure is a portrait sprite `card.py` draws at runtime. **Story art is different: a frozen moment may hold people.** |

### What Saffron should feel like

Pewter is stone and Cerulean is water; **Saffron is height and walls.** The city is ringed by a fortified wall pierced by four gates, and its skyline is towers — Silph's glass slab above everything, grey office blocks hemming in every street, and then two oddities squeezed between them: a wooden dojo with a curved roof, and a violet house with a crooked upper storey. That contrast is the whole character of the place: a modern city with two very old things in the middle of it.

---

## Files — 10 town scenes

| File | Proposed key | Shows | Weight |
|---|---|---|---|
| `town/saffron-center.jpg` | `pc` | Pokémon Center: curved red roof, circular emblem over glass doors, hedge-lined plaza of pale stone, city blocks behind | 691 KB |
| `town/saffron-mart.jpg` | `pm` | Poké Mart: blue roof over a red-and-white striped awning, blank signboard, crates and a leaning bicycle, walls of grey stone behind | 704 KB |
| `town/saffron-gym.jpg` | `gy` | Sabrina's Gym: pale violet stone, dome, wide arch, purple banners with a plain circular emblem, candlestick lamp posts on the stair, purple glow in the doorway | 523 KB |
| `town/saffron-silph.jpg` | `sl` | Silph Co.: a glass-and-steel tower climbing out of frame over a plaza of pale stone, planters, a dry fountain, office blocks flanking | 543 KB |
| `town/saffron-dojo.jpg` | `dj` | Fighting Dojo: low plaster-and-timber hall, broad curved dark roof, paper screens, raked gravel court, stone lantern, crimson banner — hemmed in by city blocks | 723 KB |
| `town/saffron-plaza.jpg` | `pl` | The crossroads: circular flagstone plaza, stone fountain, four avenues north/south/east/west, lamp posts and clipped trees, long late-afternoon shadows | 726 KB |
| `town/saffron-copycat.jpg` | `cc` | Copycat's house: small cream townhouse with a pink roof, bay window packed with dolls and a toy train, doorstep, laundry over the balcony, cat flap | 565 KB |
| `town/saffron-mr-psychic.jpg` | `mp` | Mr. Psychic's house: crooked violet timber front, round window with an inward-swirling pane, hanging beads, brass telescope, dusk light | 449 KB |
| `town/saffron-fan-club.jpg` | `fc` | Trainer Fan Club: warm yellow single-storey hall, bow window of framed photographs and pennants, rolled red carpet at the door | 485 KB |
| `town/saffron-north-gate.jpg` | `ng` | The north gate: fortified gatehouse, rounded archway onto the road out to Route 5, turrets, ivy, iron lanterns, hills beyond | 728 KB |

### Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Batch 1 contact sheet — the 10 town scenes |

---

## Still to come (batches 2–4, ~30 assets)

| Batch | Contents | Count |
|---|---|---|
| 2 | Portraits: `sabrina`, `saffron-nurse`, `saffron-clerk`, `saffron-guide`, `karate-master`, `copycat`, `mr-psychic`, `fan-club-chairman`, `silph-guard`, `silph-president` | 10 |
| 3 | Gym and dojo trainers (`psychic-*`, `blackbelt-*`), the man in black holding Silph, plus both battlefields `saffron-gym` and `saffron-dojo` | 10 |
| 4 | Story beats — the takeover, the warp-tile hall, the dojo's gift, the Marsh Badge — plus 4 area maps, the region overview and the labelled reference | ~10 |

---

## Proposed wiring — nothing applied, this is what the art needs

For the 10 scenes above to open, `people.BUILDINGS` needs an entry. Nothing in this table exists in the bot yet:

```python
"saffron-city": (
    Building("pc", "Pokémon Center", "town/saffron-center", "The nurse is busy behind the counter.", ("saffron-nurse",), "center"),
    Building("pm", "Poké Mart", "town/saffron-mart", "The shelves are full. The clerk is counting stock.", ("saffron-clerk",), "shop"),
    Building("pl", "Crossroads", "town/saffron-plaza", "Four roads meet here: north, south, east and west."),
    Building("gy", "Saffron Gym", "town/saffron-gym", "The doors stand open. The air hums.", ("saffron-guide",)),
    Building("sl", "Silph Co.", "town/saffron-silph", "The tower's glass doors are shut.", ("silph-guard",)),
    Building("dj", "Fighting Dojo", "town/saffron-dojo", "A wooden training hall between the towers.", ("karate-master",)),
    Building("cc", "Copycat's House", "town/saffron-copycat", "Dolls fill the bay window.", ("copycat",)),
    Building("mp", "Mr. Psychic's House", "town/saffron-mr-psychic", "A violet house that leans a little.", ("mr-psychic",)),
    Building("fc", "Trainer Fan Club", "town/saffron-fan-club", "Framed photographs crowd the window.", ("fan-club-chairman",)),
    Building("ng", "North Gate", "town/saffron-north-gate", "The road out to Route 5."),
),
```

Two battle fields to register in `card.FIELDS`, both currently missing:

| Field key | Anchors (far — near) | Scale |
|---|---|---|
| `saffron-gym` | `(976, 392)` — `(458, 648)` | 1.0 |
| `saffron-dojo` | `(976, 392)` — `(458, 648)` | 1.0 |

Those anchors are the convention every other set uses, not measurements from these files. Battle art is location-unique, per [`BATTLE_ART.md`](../BATTLE_ART.md).

---

## Install — proposal only, nothing applied yet

Under `assets/<location>/<category>/<file>` this batch goes to `assets/saffron-city/town/`. Later batches go to `people/`, `battle/bg/`, `story/`, `region-maps/` and `region/`.

`_scene_url()` in `bot/plugins/town.py` needs the `kanto/` prefix on a scene key to serve it from this repo, and the existing entries are mixed — Pallet writes `"kanto/town/ash-home"`, Cerulean writes `"town/cerulean-center"`. Whichever way Saffron is wired, it should match how the prefix is being handled when that code lands.
