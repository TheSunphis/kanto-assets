# Vermilion City — asset request (Kanto)

Vermilion City for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**20 of ~40 — batches 1 and 2: the city and its people.** Everything here is staged for review; nothing is installed.

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
| `cl` | Cerise Laboratory | `town/vermilion-cerise-lab` *(batch 4)* | A tall glass-and-steel building in the middle of the city. A receptionist hands out TM90 to visitors. | receptionist |

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

## Still to come

| Batch | Contents | Count |
|---|---|---|
| 3 | Story beats — boarding the S.S. Anne, the seasick captain, the tree in front of the Gym, the switches in the trash cans, the Fan Club audience, Ritchie at the docks, Jessie and James at Bill's Lighthouse — plus `vermilion-gym` and `vermilion-harbour` battle fields | ~10 |
| 4 | `town/vermilion-cerise-lab` and a school scene, four area maps, both region views ringed, the labelled reference | ~10 |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten city scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the ten portraits |
