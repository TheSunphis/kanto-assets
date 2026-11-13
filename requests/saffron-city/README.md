# Saffron City — asset request (Kanto)

Saffron City for PokéBot, in the **Pokémon Fire Ash** style.

**40 of 40 — the set is complete.** 10 town scenes, 18 portraits, 2 battlefields, 4 story beats, 4 area maps, 2 region views. Nothing is installed; every file stays in `requests/`.

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

### Portraits — 18 of ~20

Full-body sprites on flat cream `(244,245,227)`, 726 px tall flush to the bottom, 2 px grid, 48 colours. Nobody here exists in the bot yet — each needs a `Person(...)` entry **and** a line in `people.PORTRAITS`, or the game will show the building's picture instead of the face.

| File | Proposed key | Design | Weight |
|---|---|---|---|
| `people/sabrina.jpg` | `sabrina` — Gym Leader | **Adult**, about twenty-five: very long straight dark teal-black hair past the waist, cool unblinking stare, deep magenta high-collared dress with black trim and sash, long white gloves, black boots, one hand half-raised as if about to use a power | 89 KB |
| `people/saffron-nurse.jpg` | `saffron-nurse` — Nurse Joy | The same Joy as Pewter's and Cerulean's: pink hair in two soft side loops, white cap with pink cross, white dress with pink trim and apron | 106 KB |
| `people/saffron-clerk.jpg` | `saffron-clerk` — Mart Clerk | **Adult**, about twenty-two: blue-and-white cap, blue shirt with white collar, white apron, a stock box against his hip | 95 KB |
| `people/saffron-guide.jpg` | `saffron-guide` — Gym Guide | **Adult**, about thirty: tall and narrow-shouldered, thin spectacles, cream waistcoat over a lilac shirt with rolled sleeves, bow tie, clipboard, hand raised mid-explanation | 94 KB |
| `people/karate-master.jpg` | `karate-master` — Fighting Dojo | **Adult**, about forty-five: heavily built, cropped greying hair, thick moustache, white gi with torn-off sleeves, black belt, taped knuckles, grounded stance with fists at his sides | 128 KB |
| `people/copycat.jpg` | `copycat` | **Child**, about eight, child proportions: pigtails with red ribbons, round glasses, green checked pinafore, hugging a plain cloth doll | 135 KB |
| `people/mr-psychic.jpg` | `mr-psychic` | **Adult**, about fifty: stooped, receding hair, thin pointed grey beard, violet-and-gold robe, crescent pendant, tinted spectacles, hands cupped round a glassy sphere | 120 KB |
| `people/fan-club-chairman.jpg` | `fan-club-chairman` | **Elderly**, about seventy: bald crown with white sides, thick white moustache, brown three-piece suit, red bow tie, half-moon spectacles, a stack of glossy photographs | 142 KB |
| `people/silph-guard.jpg` | `silph-guard` — Silph Co. | **Adult**, about thirty-five: navy uniform and peaked cap, shoulder patch with a plain white circle, boots planted apart, one hand on the walkie-talkie at his chest | 104 KB |
| `people/silph-president.jpg` | `silph-president` | **Elderly**, about sixty-eight: silver hair, trimmed grey moustache, charcoal three-piece suit, burgundy tie, folded document at his side | 93 KB |

The age spread is deliberate and checked: children are child-proportioned (`copycat` is visibly the smallest figure in the set), the dojo master and the Silph guard read as grown men, and the two elderly characters read as elderly rather than merely older.

#### Batch 3 — the Gym's psychics, the Dojo's black belts, the tower's staff

| File | Proposed key | Design | Weight |
|---|---|---|---|
| `people/psychic-cameron.jpg` | `psychic-cameron` | **Adult**, about twenty: shaggy pale blond hair, half-lidded eyes, deep purple hooded tunic with wide sleeves over lilac trousers, palms turned up | 110 KB |
| `people/psychic-rachel.jpg` | `psychic-rachel` | **Adult**, about twenty-two: very long straight violet hair with one thin braid, lilac-and-white bodysuit, short purple mantle, gold bangles, fingers spread | 108 KB |
| `people/psychic-iona.jpg` | `psychic-iona` | **Elderly**, about sixty: silver hair in a pin-heavy bun, lined face, deep-plum fringed shawl over a lavender gown, amethyst pendant, hand raised flat | 108 KB |
| `people/blackbelt-hitoshi.jpg` | `blackbelt-hitoshi` | **Adult**, about twenty-five: shaved head, short dark beard, white gi, brown belt, barefoot, fists raised in guard | 115 KB |
| `people/blackbelt-hideki.jpg` | `blackbelt-hideki` | **Adult**, about thirty: stocky and broad, spiky hair, red headband, sleeveless gi, taped wrists, one fist forward | 137 KB |
| `people/silph-rocket.jpg` | `silph-rocket` — the man in black | **Adult**, about thirty: black peaked cap and uniform with a plain red circle emblem, gloves and boots, utility belt, hand on a holstered item, weight on one leg, enjoying the obstruction | 83 KB |
| `people/silph-receptionist.jpg` | `silph-receptionist` | **Adult**, about twenty-eight: auburn hair tucked behind one ear, pale blue blazer over a white blouse, hands folded at the waist | 88 KB |
| `people/silph-scientist.jpg` | `silph-scientist` | **Adult**, about forty: thinning hair, thick-rimmed glasses, fretful, lab coat over a pale green shirt, blank ID card, clipboard clutched to his chest | 115 KB |

### Battlefields — both fields Saffron was missing

`card.FIELDS` has no Saffron key at all, so every trainer in the Gym and the Dojo currently fights on the generic `grass` fallback. Two files fix that:

| File | Proposed field key | Anchors | Scale | Shows | Weight |
|---|---|---|---|---|---|
| `battle/bg/saffron-gym.jpg` | `saffron-gym` | `(976, 392)` far, `(458, 648)` near | 1.0 | The Psychic Gym arena: checkered violet-and-white tiles, four glowing teleport pads set flush in the floor, mirrored pillars, violet braziers on chains, a marble dais at the far end, drifting haze | 331 KB |
| `battle/bg/saffron-dojo.jpg` | `saffron-dojo` | `(976, 392)` far, `(458, 648)` near | 1.0 | The Dojo floor: worn tatami mats, dark timber pillars, shoji screens lit from behind, a raised alcove with a **blank** scroll and a flower arrangement, weapons rack, dusty afternoon light | 530 KB |

Both are empty of figures — the trainer sprites and the opponent are drawn over them at runtime, per [`BATTLE_ART.md`](../BATTLE_ART.md).

### Story beats — 4

Story art is the one place people are allowed, because a story frame is a frozen moment rather than a place the bot returns to. Only the takeover has a figure in it, and only as a distant silhouette.

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/silph-takeover.jpg` | The tower, taken | The lobby after the doors were forced: toppled chairs, papers across the marble, a barricade of desks across the doorway, one lamp still burning, and a single black-clad silhouette far down the hall with his back turned | 482 KB |
| `story/saffron-warp-hall.jpg` | The hall that moves you | Checkerboard floor, four teleport pads on a broken diagonal, mirror panels reflecting the wrong walls, purple braziers — symmetrical at first glance and wrong on the second | 491 KB |
| `story/dojo-shrine.jpg` | The Dojo's offer | The shrine alcove: a blank hanging scroll, a low lacquered table with two empty offertory trays, one beam of dusty light across worn tatami | 378 KB |
| `story/marsh-badge.jpg` | The Marsh Badge | A round gold-rimmed disc of pale pink enamel with three small gold dots, lying small on the violet cushion under a spotlight. No letterform anywhere — the lesson from Cerulean's badge applied up front | 450 KB |

### Area maps — 4, at 1376 × 768

| File | Covers | Weight |
|---|---|---|
| `region-maps/kanto-saffron-city-map-centre.jpg` | The crossroads: circular plaza, fountain, four avenues, Centre and Mart on the near corners | 507 KB |
| `region-maps/kanto-saffron-city-map-silph-quarter.jpg` | The tower quarter: the glass slab and its entrance plaza, dry fountain, grid of streets and mid-rise blocks | 527 KB |
| `region-maps/kanto-saffron-city-map-gym-quarter.jpg` | Gym and Dojo **side by side**, the violet dome against the curved wooden roof — the contrast this set is built on | 524 KB |
| `region-maps/kanto-saffron-city-map-gates.jpg` | The north gate: the wall, the gatehouse over the road out, the townhouses and lanes below it | 695 KB |

### Region views — 2, at 1376 × 768

| File | Shows | Saffron ringed at |
|---|---|---|
| `region/kanto-saffron-city.jpg` | The Kanto landmass with the walled city sitting dead centre where four roads meet — ridges north, forest west, the southern port, the volcano island below | `703, 373`, r 172 × 138 |
| `region/kanto-map-saffron-city.jpg` | A flat schematic: pale land, grey ridges, forest blocks, two southern islands, and the walled city at the exact centre with four roads radiating out of it in a cross | `690, 372`, r 118 × 108 |

Both installed files of these names in `assets/saffron-city/region/` predate the set and would be replaced by this pair. Rings are drawn in code over finished art, after inspecting where the city actually landed — never asked for in the prompt, because generated geography drifts.

### Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Batch 1 contact sheet — the 10 town scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the 10 portraits |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — 8 portraits and both battlefields |
| `review/_sheet-batch-4.jpg` | Batch 4 contact sheet — 4 area maps, 1 region view, 4 story beats |
| `_saffron-city-labeled-reference.jpg` | The map side of the set at a glance — both region views and all four area maps, captioned, with both ring coordinates printed |

---

## The set is complete

| Category | Count | Notes |
|---|---|---|
| Town scenes | 10 | all ten need `Building(...)` entries — the town has none |
| Portraits | 18 | all need `Person(...)` **and** a line in `PORTRAITS` |
| Battlefields | 2 | `saffron-gym`, `saffron-dojo` — neither field key exists yet |
| Story beats | 4 | the takeover, the warp hall, the shrine, the Marsh Badge |
| Area maps | 4 | centre, tower quarter, Gym-and-Dojo, north gate |
| Region views | 2 | landmass + schematic, both ringed |

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

Two battle fields to register in `card.FIELDS`, both still missing — the art for them is already in `battle/bg/` as of batch 3:

| Field key | Art | Anchors (far — near) | Scale |
|---|---|---|---|
| `saffron-gym` | ✅ `battle/bg/saffron-gym.jpg` | `(976, 392)` — `(458, 648)` | 1.0 |
| `saffron-dojo` | ✅ `battle/bg/saffron-dojo.jpg` | `(976, 392)` — `(458, 648)` | 1.0 |

Those anchors are the convention every other set uses, not measurements from these files. Battle art is location-unique, per [`BATTLE_ART.md`](../BATTLE_ART.md).

The ten portraits need their own entries in `people.PEOPLE`, plus a line each in the `PORTRAITS` set — the set is what tells the bot a person has a picture of their own:

```python
# in PORTRAITS, alongside the existing names
'sabrina', 'saffron-nurse', 'saffron-clerk', 'saffron-guide', 'karate-master',
'copycat', 'mr-psychic', 'fan-club-chairman', 'silph-guard', 'silph-president',
'psychic-cameron', 'psychic-rachel', 'psychic-iona', 'blackbelt-hitoshi',
'blackbelt-hideki', 'silph-rocket', 'silph-receptionist', 'silph-scientist',
```

---

## Install — proposal only, nothing applied yet

Under `assets/<location>/<category>/<file>`: town scenes to `assets/saffron-city/town/`, portraits to `people/`, both battlefields to `battle/bg/`, story beats to `story/`, area maps to `region-maps/`, and the region view to `region/`.

`_scene_url()` in `bot/plugins/town.py` needs the `kanto/` prefix on a scene key to serve it from this repo, and the existing entries are mixed — Pallet writes `"kanto/town/ash-home"`, Cerulean writes `"town/cerulean-center"`. Whichever way Saffron is wired, it should match how the prefix is being handled when that code lands.
