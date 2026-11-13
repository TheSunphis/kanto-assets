# Vermilion City — asset request (Kanto)

Vermilion City for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**40 of 40 — the set is complete.** 12 place scenes, 10 portraits, 10 story beats, 2 battlefields, 4 area maps, 2 region views.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | Hard pixel edges, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, single figure 726 px, bottom-flush |
| Content rule | **Places** carry no people and no Pokémon. **Story** beats may and should contain people |
| No text | No signage, no shop names, no prices, no lettering of any kind — `card.py` draws the plate |

### The design thesis

Each Kanto set so far has been built on one material. Pewter is stone. Cerulean is water. Saffron is height and
walls. **Vermilion is iron over salt water**: corrugated sheds, cranes, rope, brass lamps, navy roofs, and paint
that has been repainted badly over rust. It is a working port, not a resort.

### Fire Ash, not FireRed

The cast here follows **Pokémon Fire Ash**, which means the anime's Vermilion rather than the cartridge's. That
changes who is standing where, and it is worth writing down because several of these people do not exist in FRLG:

| Fire Ash | What it means for this set |
|---|---|
| **Brock stands in front of the Gym** and will not move until you beat him | Brock's Pewter portrait is reused as-is — no redraw — but he needs a `Person` entry located *here* as well |
| Gym trainers are **Sailor Dwayne** and **Gentleman Tucker**, both Electric users | two named portraits instead of the anonymous `sailor` / `gentleman` class sprites |
| The Fan Club president **blathers about his Fearow** and hands over a Bicycle | `fan-club-president` |
| After Surge, a **lady in the Fan Club gives out a Light Ball** | `fan-club-lady` |
| The **Fishing Guru** gives the Old Rod | `fishing-guru` |
| The **S.S. Anne** must be boarded — you need both Misty's and Surge's badges | `ss-anne-captain`, and the harbour building |
| A **tall building in the centre** with a receptionist, TM90 and a Master Ball | **Cerise Laboratory** — not in FRLG, and its scene is coming in batch 4 |
| **Ritchie waits at the docks** in the post-game | `ritchie`, staged in batch 3 |
| **Jessie and James** turn up at Bill's Lighthouse north of the city | story beat in batch 3 — and `st-anne`

---

## Where Vermilion sits in the bot

Vermilion is **almost entirely unwired** — one line in `world.py` and nothing else:

```python
"vermilion-city": ("Vermilion City", "A busy harbour city where ships come and go.", 6, 5, "left"),
```

| Missing | Detail |
|---|---|
| `BUILDINGS["vermilion-city"]` | no entry at all — the city has no buildings to walk into |
| `PEOPLE` | nothing located there; no portraits, no trainers |
| `card.FIELDS` | no Vermilion field — no gym, no harbour battle |
| `spawns.py` | no hunting area |
| `assets/vermilion-city/` | only `region/kanto-vermilion-city.jpg` and `region/kanto-map-vermilion-city.jpg` |

It is on two roads already — `("saffron-city", "vermilion-city", "Route 6", [])` and
`("vermilion-city", "lavender-town", "Routes 11 and 12", [(8, 5)])` — and it is `SEVII_PORT`, the harbour the
ferry to the Sevii Islands leaves from and returns to. That makes the docks the one building in Kanto with a job
beyond scenery.

### Proposed buildings

| Key | Name | Scene | Blurb | People |
|---|---|---|---|---|
| `pc` | Pokémon Center | `town/vermilion-center` | A whitewashed Center under a navy roof, awnings over the doors. | nurse |
| `pm` | Poké Mart | `town/vermilion-mart` | The Mart's awning snaps in the wind off the water. | clerk |
| `gy` | Vermilion Gym | `town/vermilion-gym` | An old brick warehouse with a bolt painted over the door. | Lt. Surge, gym guide |
| `hb` | Vermilion Harbour | `town/vermilion-harbour` | The ferry to the Sevii Islands loads at the far pier. | harbour master, sailor |
| `fc` | Pokémon Fan Club | `town/vermilion-fan-club` | A comfortable house where people talk about their favourites. | chairman, member |
| `fg` | Fishing Guru's House | `town/vermilion-fishing-guru` | Rods lean against a tar-paper shack by the channel. | the guru |
| `lh` | The Lighthouse | `town/vermilion-lighthouse` | A red-banded tower at the end of the breakwater. | keeper |
| `mk` | Fish Market | `town/vermilion-market` | Four stalls, crushed ice, brass scales. | fishmonger |
| `wh` | Warehouse Row | `town/vermilion-warehouses` | Corrugated sheds, loading bays, a hand hoist. | dock worker |
| `sq` | Harbour Square | `town/vermilion-square` | An old anchor on a plinth, a bandstand, benches facing the water. | — |
| `cl` | Cerise Laboratory | `town/vermilion-cerise-lab` | A tall glass-and-steel building in the middle of the city. A receptionist hands out TM90 to visitors. | receptionist |
| `sc` | Vermilion School | `town/vermilion-school` | A red-brick school behind iron railings. The playground is empty this hour. | — |

### Batch 2 — the people (10)

| File | Key | Fire Ash role | Design | Weight |
|---|---|---|---|---|
| `people/lt-surge.jpg` | `lt-surge` | Gym Leader, **one-on-one against his Raichu** | **Man of thirty-five**: very tall and heavily muscled, tanned, spiky pale-blond crew cut, olive tank top, camo trousers, fingerless gloves, two plain dog tags, arms folded | 121 KB |
| `people/sailor-dwayne.jpg` | `sailor-dwayne` | Gym trainer | **Man of twenty-six**: sunburnt, stubble, open grin, white sailor uniform with a striped navy collar, white cap | 117 KB |
| `people/gentleman-tucker.jpg` | `gentleman-tucker` | Gym trainer | **Man of sixty-five**: silver hair, white moustache, monocle on a chain, burgundy three-piece suit, cravat, gold watch chain, cane | 100 KB |
| `people/fan-club-president.jpg` | `fan-club-president` | Blathers about his **Fearow**, gives the Bicycle | **Man of seventy**: round-bellied, nearly bald, lavender cardigan, maroon bow tie, hands behind his back, leaning back to start a long story | 106 KB |
| `people/fan-club-lady.jpg` | `fan-club-lady` | Hands out a **Light Ball** after Surge | **Woman of forty-five**: comfortably built, auburn wave, pink floral blouse, pearls, green cardigan over the shoulders, handbag | 114 KB |
| `people/fishing-guru.jpg` | `fishing-guru` | Gives the **Old Rod** | **Man of sixty-five**: leathery and weathered, white beard, floppy bucket hat, many-pocketed fishing vest over a striped jumper, bamboo rod held like a staff | 141 KB |
| `people/vermilion-nurse.jpg` | `vermilion-nurse` | Center | **Woman of thirty**: pink hair in two flat loops, white cap with a plain red band and **no cross**, pink apron, hands folded | 107 KB |
| `people/vermilion-clerk.jpg` | `vermilion-clerk` | Mart | **Man of twenty-one**: navy tabard apron, blank name badge, carrying a stack of plain boxes | 89 KB |
| `people/ss-anne-captain.jpg` | `ss-anne-captain` | **Seasick**, gives Cut | **Man of fifty-five**: portly, green about the gills, white beard, navy double-breasted coat with brass buttons, peaked cap with a blank badge, one hand on his stomach | 117 KB |
| `people/cerise-receptionist.jpg` | `cerise-receptionist` | The tall building in the centre — TM90 and a Master Ball | **Woman of twenty-six**: tight bun, rectangular glasses, teal blazer, blank lanyard card, clipboard | 88 KB |

**Wiring** — ten `Person(...)` entries and ten `PORTRAITS` lines, all pointed at `"vermilion-city"`:

```python
"lt-surge": "vermilion-city", "sailor-dwayne": "vermilion-city", "gentleman-tucker": "vermilion-city",
"fan-club-president": "vermilion-city", "fan-club-lady": "vermilion-city", "fishing-guru": "vermilion-city",
"vermilion-nurse": "vermilion-city", "vermilion-clerk": "vermilion-city",
"ss-anne-captain": "vermilion-city", "cerise-receptionist": "vermilion-city",
```

`lt-surge` needs a `Trainer(...)` in `trainers.py` as the Gym Leader with the Raichu, and `sailor-dwayne` /
`gentleman-tucker` as his two Gym trainers. `fan-club-president`, `fan-club-lady`, `fishing-guru`,
`cerise-receptionist` are dialogue only.

### Batch 3 — story beats (8) and both battlefields

Story frames are allowed to carry people — they are frozen moments, not places the bot returns to.

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/vermilion-anne-boarding.jpg` | Boarding the S.S. Anne | The liner's lit hull at dusk, a gangway down to the quay, a sailor with a clipboard, a young trainer holding something small up to him | 442 KB |
| `story/vermilion-captain-cabin.jpg` | The seasick captain | A panelled cabin lit by swinging oil lamps, portholes showing tilted water, a big man in a navy coat bent over the desk, green about the gills, the whole room at a faint angle | 503 KB |
| `story/vermilion-gym-brock.jpg` | Brock won't move | A stocky figure seen from behind, square in front of the half-open steel door, arms folded, a sapling in the crack beside him | 475 KB |
| `story/vermilion-gym-switches.jpg` | The trash cans | A bare concrete gym under cage lamps, conduit and junction boxes along the wall, a row of metal cans with their lids resting against them, one lid off on the floor | 478 KB |
| `story/vermilion-fan-club-parlour.jpg` | The Fearow story | A parlour stuffed with ornaments and lace curtains: an old man in a cardigan leaning forward mid-tale, tea tray between him and a seated trainer seen from behind, golden window light | 512 KB |
| `story/vermilion-ritchie-docks.jpg` | Ritchie at the docks | A timber pier at sunset, a boot up on the bollard, a young trainer in a green headband silhouetted against flat orange water | 436 KB |
| `story/vermilion-lighthouse-rocket.jpg` | At Bill's Lighthouse | The red-banded tower at night with its beam sweeping out over black water, two black-uniformed figures small on the path below, one pointing up | 360 KB |
| `story/vermilion-ferry-dawn.jpg` | The ferry out | First light on three empty piers, a white ferry easing away with its wake spreading, warehouses in mist. Empty — the departure belongs to the place | 523 KB |

**Battlefields**, both 1376 × 768 and empty of figures. Note that Vermilion had **no `card.FIELDS` key at all**, so
every trainer here currently fights on `grass`:

| File | Proposed field key | Shows | Weight |
|---|---|---|---|
| `battle/bg/vermilion-gym.jpg` | `vermilion-gym` | The gutted shed as an arena: plain concrete floor, brick wall, steel trusses, conduit and junction boxes, two cage lamps, cans and barrels pushed to the edges | 292 KB |
| `battle/bg/vermilion-harbour.jpg` | `vermilion-harbour` | The quay as an arena: stone setts, bollards and coiled rope at the edge, deep blue water, the liner's hull to the left, crane and crates to the right | 521 KB |

Anchors for both, by the convention every field uses: `(976, 392)` far — `(458, 648)` near, scale `1.0`.

**A wiring wrinkle worth knowing:** Brock's portrait lives at `assets/pewter-city/people/brock.jpg`, and `Person`
carries a single `town` field. So standing him in front of the Vermilion Gym means a second entry —
`Person("brock-vermilion", "Brock", "vermilion-city", ...)` — with `PORTRAITS["brock-vermilion"] = "pewter-city"`
pointing back at the same file. One portrait, two places.

### Batch 4 — the two missing buildings, the maps, and the badge

**Two place scenes finish the city's geography.** Both were gaps that mattered: the centre of the map had no
building on it, and the anime's Vermilion school didn't exist at all.

| File | Key | Shows | Weight |
|---|---|---|---|
| `town/vermilion-cerise-lab.jpg` | `cl` | The tall building in the middle of the city: an eleven-storey tower of pale concrete and blue-green glass, cantilevered canopy on thin columns, shallow steps to a glass lobby with a desk visible inside, a steel sphere on the forecourt, hedges in long planters, flagpoles with **plain unlettered** banners, a bicycle rack | 642 KB |
| `town/vermilion-school.jpg` | `sc` | The city school: long two-storey red brick with a slate roof, arched windows, a bell tower with a green copper cap, a walled playground with a climbing frame, hopscotch on the asphalt and a basketball hoop, plane trees along the railings | 675 KB |

**Story** — two more, making ten in total:

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/vermilion-gym-leader-floor.jpg` | The leader's floor | The inner arena down a corridor of steel columns, a raised platform at the far end under two cage lamps, one tall figure in an olive tank top standing on it with his back to us | 337 KB |
| `story/vermilion-thunder-badge.jpg` | The Thunder Badge | A round gold-rimmed disc of deep orange enamel with a bold angular bolt across it, lying small on a charcoal velvet cushion under a spotlight. Round and flat, and the prompt bans letterforms outright — the bolt is the one shape allowed | 354 KB |

**Area maps**, 1376 × 768, under `region-maps/` as in the Saffron set:

| File | Covers | Weight |
|---|---|---|
| `region-maps/kanto-vermilion-city-map-centre.jpg` | The square: tower to the north, bandstand west, the anchor monument in the middle, four streets out | 587 KB |
| `region-maps/kanto-vermilion-city-map-docks.jpg` | The working harbour: three piers, the liner at the middle one, market stalls, crane and crates, the breakwater lighthouse | 462 KB |
| `region-maps/kanto-vermilion-city-map-gym-quarter.jpg` | The gym's brick shed with the bolt on it, the Fan Club house next door, the Fishing Guru's shack on the channel, the footbridge | 736 KB |
| `region-maps/kanto-vermilion-city-map-north.jpg` | The park and pond, the school and its playground, the road out to Route 6, the lighthouse on its headland | 719 KB |

**Region views**, both ringed in code after checking where the harbour actually landed:

| File | Shows | Vermilion ringed at |
|---|---|---|
| `region/kanto-vermilion-city.jpg` | The whole landmass, with the harbour city pressed against a deep blue inlet in the south-east, three piers out into the water and the liner alongside | `1013, 415`, r 190 × 88 |
| `region/kanto-map-vermilion-city.jpg` | The flat schematic: the south-east coast folded into a bay, the red-roofed port at the head of it, three thin piers and a white ship | `1143, 530`, r 82 × 74 |

Both installed files of these names in `assets/vermilion-city/region/` predate the set and would be replaced by this pair.

---

## Files — batch 1: place scenes (10)

| File | Key | Weight |
|---|---|---|
| `town/vermilion-center.jpg` | `pc` | 509 KB |
| `town/vermilion-mart.jpg` | `pm` | 585 KB |
| `town/vermilion-gym.jpg` | `gy` | 544 KB |
| `town/vermilion-harbour.jpg` | `hb` | 488 KB |
| `town/vermilion-fan-club.jpg` | `fc` | 727 KB |
| `town/vermilion-fishing-guru.jpg` | `fg` | 454 KB |
| `town/vermilion-lighthouse.jpg` | `lh` | 515 KB |
| `town/vermilion-market.jpg` | `mk` | 607 KB |
| `town/vermilion-warehouses.jpg` | `wh` | 595 KB |
| `town/vermilion-square.jpg` | `sq` | 603 KB |

Notes on three of them:

- **`vermilion-gym`** is a converted brick warehouse, not a stadium — canon puts Lt. Surge's Gym behind a rolling
  steel door with a bolt on the wall. The bolt is an angular shape only; no letters anywhere.
- **`vermilion-harbour`** carries the liner, the crane and the lighthouse in one frame, because `SEVII_PORT` means
  this is where a player leaves Kanto entirely.
- **`vermilion-market`** is deliberately the busiest composition in the set — the one scene where the emptiness is
  doing work rather than just obeying the rule.

---

## The set is complete

| Category | Count | Notes |
|---|---|---|
| Place scenes | 12 | `town/` — ten buildings plus the Cerise Laboratory and the school |
| Portraits | 10 | Surge, Dwayne, Tucker, the two Fan Club figures, the Fishing Guru, nurse, clerk, S.S. Anne captain, Cerise receptionist |
| Story beats | 10 | eight moments plus the leader's floor and the Thunder Badge |
| Battlefields | 2 | `vermilion-gym`, `vermilion-harbour` — the city had no field key at all |
| Area maps | 4 | centre, docks, gym quarter, north |
| Region views | 2 | landmass and schematic, both ringed on the harbour |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten city scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the ten portraits |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — eight story beats and both battlefields |
| `review/_sheet-batch-4.jpg` | Batch 4 contact sheet — Cerise lab, school, four area maps, badge, leader's floor |
| `_vermilion-city-labeled-reference.jpg` | The map side of the set at a glance, captioned, both ring coordinates printed |
