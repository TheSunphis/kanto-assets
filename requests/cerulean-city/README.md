# Cerulean City — asset request (Kanto)

Cerulean City for PokéBot, in the **Pokémon Fire Ash** style.

**29 of ~40 — batches 1–3: the city, both battlefields, all 15 portraits, and four story beats.** Nothing is installed; every file stays in `requests/`.

---

## What the bot expects here

- **Location id:** `cerulean-city`
- **Five buildings** in `people.BUILDINGS["cerulean-city"]`:

| Key | Name | Scene key it fetches |
|---|---|---|
| `pc` | Pokémon Center | `town/cerulean-center` |
| `pm` | Poké Mart | `town/cerulean-mart` |
| `bs` | Bike Shop | `town/cerulean-bike` |
| `nb` | Nugget Bridge | `town/cerulean-bridge` |
| `gy` | Cerulean Gym | `town/cerulean-gym` |

- **Fifteen people — the biggest portrait job in Kanto:** `cerulean-nurse`, `cerulean-clerk`, `bike-owner`, `bridge-lookout`, `cerulean-guide`, `swimmer-luis`, `picnicker-diana`, `misty`, `bug-catcher-cale`, `lass-ali`, `youngster-timmy`, `lass-reli`, `camper-ethan`, `bridge-rocket`, `bill`
- **Nine trainers across two fields:**

| Field | Trainers |
|---|---|
| `cerulean-gym` | Swimmer Luis · Picnicker Diana · **Misty** |
| `nugget-bridge` | Bug Catcher Cale · Lass Ali · Youngster Timmy · Lass Reli · Camper Ethan · **Bridge Rocket** — the ordered gauntlet |

## Both of these battlefields had no art anywhere

`card.FIELDS` declares two keys here, and `49b2987` had deleted both pictures. With Pewter's gym, these were the last registered battle keys in the bot with nothing behind them, so every trainer above was being drawn on the generic `grass` fallback. Both are now here:

| File | Field key | Anchors | Scale |
|---|---|---|---|
| `battle/bg/cerulean-gym.jpg` | `cerulean-gym` | `(976, 392)` far, `(458, 648)` near | 1.0 |
| `battle/bg/nugget-bridge.jpg` | `nugget-bridge` | `(976, 375)` far, `(430, 625)` near | 1.0 |

The gym field is the aquarium interior — pale tiled deck, a pool crossing the mid-ground, the great glass tank behind. The bridge field is the stone deck with its parapets and lamps, the river running past on both sides.

---

## A note on sourcing

The Pokémon Fire Ash Wiki has **no Cerulean City page** — the article renders empty. So unlike Pewter, Viridian Forest and Route 2, there is no wiki walkthrough to follow here: these scenes come from FRLG and anime canon plus what the bot itself declares. Anything specifically Fire Ash about Cerulean will have to come from the game, not the wiki.

---

## What was already installed — read this before judging the count

`assets/cerulean-city/` is **not empty**. It already holds 23 pieces of Cerulean art, put there by the `0baa964` reorganisation:

| Category | Already in `assets/cerulean-city/` |
|---|---|
| Portraits — 14 | `misty`, `bike-owner`, `bridge-lookout`, `bridge-rocket`, `bug-catcher-cale`, `camper-ethan`, `cerulean-clerk`, `cerulean-guide`, `cerulean-nurse`, `lass-ali`, `lass-reli`, `picnicker-diana`, `swimmer-luis`, `youngster-timmy` |
| Town scenes — 5 | `cerulean-bike`, `cerulean-bridge`, `cerulean-center`, `cerulean-gym`, `cerulean-mart` |
| Region — 2 | `kanto-cerulean-city`, `kanto-map-cerulean-city` |
| Route info — 1 | `nugget-bridge` |
| **Battlefields — 0** | **nothing at all** |

So the honest split of this request:

- **The two battlefields are the real gap.** `cerulean-gym` and `nugget-bridge` had no art in `assets/` or in `requests/`, while nine trainers fight on them.
- **The 5 town scenes here replace installed ones** — same filenames, art matched to the other Kanto sets.
- **The 9 portraits here replace installed ones** — same keys, so they drop straight in.
- **All 15 portraits are now here** — batch 3 closed the six gaps (`bike-owner`, `bug-catcher-cale`, `lass-ali`, `youngster-timmy`, `lass-reli`, `camper-ethan`) plus `bill`, which was the only portrait with no installed counterpart.
- **Story art is banked, not wired.** `Quest` has no `picture` field, so these four are for the point where story scenes get a place to live.

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

## Files — 8 town scenes

| File | `people.py` key | Shows | Weight |
|---|---|---|---|
| `town/cerulean-center.jpg` | `pc` ✅ existing key | White glazed tile, wide red roof, circular emblem, canal with railing behind | 640 KB |
| `town/cerulean-mart.jpg` | `pm` ✅ existing key | Blue roof, striped awning, crates, lamp, canal glimpse at the top | 880 KB |
| `town/cerulean-bike.jpg` | `bs` ✅ existing key | Bike shop: yellow-green signboard, silhouetted bikes in the window, a rank of bicycles outside on stands | 654 KB |
| `town/cerulean-gym.jpg` | `gy` ✅ existing key | Aquarium Gym: white tile, deep blue roof, glass front onto a lit tank of water and plants, cresting-wave sign | 728 KB |
| `town/cerulean-bridge.jpg` | `nb` ✅ existing key | Nugget Bridge as a place: the long stone deck running north between parapets and lamps, wide river either side | 749 KB |
| `town/cerulean-waterfront.jpg` | **new key** | The canal: quays, iron railings, landing stairs, a tied rowing boat, arched footbridge, white and pale-blue houses | 766 KB |
| `town/cerulean-north-road.jpg` | **new key** | The road out toward Routes 24/25 and Bill's cottage: flower meadows, signpost at the fork, hills and a river beyond | 632 KB |
| `town/cerulean-cave-path.jpg` | **new key** | The rocky path to Cerulean Cave: scree, a dark cave mouth under a boulder arch, bright water along the cliff foot | 539 KB |

Five drop onto existing building keys with no code change. Three are extra scenes and need one `Building(...)` entry each.

### Portraits — all 15

Full-body sprites on flat cream `(244,245,227)`, 726 px tall, flush to the bottom, 2 px grid, 48 colours. Every one of these **replaces** the same-named file already in `assets/cerulean-city/people/`.

| File | `people.PERSON` key | Design | Weight |
|---|---|---|---|
| `people/misty.jpg` | `misty` — Gym Leader | Teenage girl, bright orange hair in a high side ponytail, yellow sleeveless top with red trim, red suspenders, denim-blue shorts, red-and-white high-tops, hand on hip | 118 KB |
| `people/bill.jpg` | `bill` | Young adult researcher, messy light brown hair, round wire glasses, pen behind the ear, open white lab coat over a green shirt, device in hand | 118 KB |
| `people/bridge-lookout.jpg` | `bridge-lookout` | Sixteen, wide flat blue cap, freckles, light blue ranger shirt with chest pockets, binoculars up and strap round the neck | 121 KB |
| `people/cerulean-nurse.jpg` | `cerulean-nurse` — Nurse Joy | Pink hair in two soft side loops, white cap with pink cross, white dress with pink trim, apron — matching the Pewter Centre's Joy exactly | 109 KB |
| `people/cerulean-clerk.jpg` | `cerulean-clerk` — Mart Clerk | Mid twenties, blue-and-white cap, blue shirt with white collar, white apron, price gun and parcels | 115 KB |
| `people/cerulean-guide.jpg` | `cerulean-guide` | Late twenties, dark bun, pale blue blazer and trousers, lapel badge, town map in hand, arm raised in welcome | 111 KB |
| `people/swimmer-luis.jpg` | `swimmer-luis` | Adult swimmer, tanned, wet dark hair, blue trunks, goggles pushed up on his forehead, towel over one shoulder | 103 KB |
| `people/picnicker-diana.jpg` | `picnicker-diana` | Fifteen, braids under a wide straw hat with a ribbon, green sleeveless top, orange skirt, wicker basket, checkered blanket | 134 KB |
| `people/bridge-rocket.jpg` | `bridge-rocket` — Team Rocket | Early twenties, black peaked cap and jacket with a plain red circle emblem, boots and gloves, satchel strap, smug | 84 KB |

#### Batch 3 — the remaining six

Same spec, same cream, same 726 px. These had no counterpart in `requests/` before; all six already exist in `assets/cerulean-city/people/`, so they are replacements.

| File | `people.PERSON` key | Design | Weight |
|---|---|---|---|
| `people/bike-owner.jpg` | `bike-owner` — Bike Shop | **Adult**, stocky and mid-forties, receding dark hair and a thick moustache, red-and-white cycling cap, shop polo under a heavy leather mechanic's apron, work boots, wrench and oil rag | 116 KB |
| `people/bug-catcher-cale.jpg` | `bug-catcher-cale` | Fifteen, wide flat straw hat over messy green hair, green shirt, tan cargo shorts and knee socks, butterfly net upright, leather satchel | 139 KB |
| `people/lass-ali.jpg` | `lass-ali` | Ten, chin-length brown hair with two red clips, pink dress with white rounded collar and chest bow, red Mary Janes, hands clasped hopefully | 108 KB |
| `people/youngster-timmy.jpg` | `youngster-timmy` | Ten, backwards yellow-and-black cap, blue-and-white striped tee, hands in pockets, chin-up cocky challenge | 109 KB |
| `people/lass-reli.jpg` | `lass-reli` | Eleven, blonde pigtails with green ribbons, green dress over a white pincushion-hem pinafore, one hand raised in a wave | 124 KB |
| `people/camper-ethan.jpg` | `camper-ethan` | Eleven, red bandana headband, green vest over a cream shirt, backpack with a strapped bedroll, hands on the straps | 128 KB |

The child trainers are deliberately small next to `bike-owner`, `cerulean-guide` and the other adults — the size difference is the point.

### Story beats — 4, banked until `Quest` grows a picture field

> **The content rule is absolute here: no people and no Pokémon in any scene.** Every character in the bot's scenes is a **portrait sprite** that `card.py` draws at runtime on top of the art — so a figure baked into the background would double up with the portrait, or appear in a beat where no such character is present. These four were generated and inspected empty of figures, and the two bridge pieces **originally shipped with trainers in them and were regenerated from scratch, empty.**
>
> The beat has to read from the *place* alone: the barricade says "blocked", the long empty span says "a run to make", not a painted crowd.

1408 × 768, 64 colours, no people, no creatures — backdrops only:

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/nugget-bridge-gauntlet.jpg` | The run | The arched timber footbridge seen from the near end, empty end to end, flower boxes and bright canal either side, the far shore's rooftops beyond — the span the five are strung along, waiting for the sprites | 515 KB |
| `story/nugget-bridge-rocket.jpg` | The far end, closed off | Sunset over the deck with a makeshift roadblock across the far end — stacked crates, dark luggage and two striped sawhorses — the way off the bridge shut. No figure: the Rocket is the portrait sprite | 549 KB |
| `story/cerulean-gym-pool.jpg` | The arena before Misty | Tiled deck, vast turquoise pool, rafts and a diving board, glass tank walls, empty spectator benches | 689 KB |
| `story/bill-cottage-machine.jpg` | Bill's machine | The humming glass-cored cylinder, cables across the floorboards, a desk of monitors showing only abstract glow, night sea in the round window | 497 KB |

### Review

| File | Shows |
|---|---|
| `review/_sheet.jpg` | Batch 1 contact sheet — 8 town scenes, 2 battlefields |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the 9 new portraits |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — 6 portraits and 4 story beats |

---

## Still to come (batch 4, ~10 assets)

| Contents | Count |
|---|---|
| Misty waiting at the pool edge, the Cascade Badge, two canal scenes; then the area maps (city, Nugget Bridge, gym quarter, cave path), the Kanto region overview, and the labelled reference sheet | ~10 |

---

## Install — proposal only, nothing applied yet

This set stays in `requests/`. Under `assets/<location>/<category>/<file>` it would go to `assets/cerulean-city/town/`, portraits to `assets/cerulean-city/people/`, and the two battlefields to `assets/cerulean-city/battle/bg/cerulean-gym.jpg` and `.../battle/bg/nugget-bridge.jpg` — battle art being location-unique, per [`BATTLE_ART.md`](../BATTLE_ART.md).

Two code facts that still apply: `_scene_url()` in `bot/plugins/town.py` needs the `kanto/` prefix on a scene key to serve it from this repo, and `battle.py` has no `kanto/` branch at all, so neither battlefield can be reached until that is added.
