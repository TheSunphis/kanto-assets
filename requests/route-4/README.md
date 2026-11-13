# Route 4 — asset request (Kanto)

Route 4 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 of ~30 — batch 1: the road.** Everything here is staged for review; nothing is installed.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset |
| Pixel grid | Hard pixel edges, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, single figure 726 px, bottom-flush |
| Content rule | **Places** carry no people and no Pokémon. **Story** beats may and should contain people |

### What Route 4 is

The road between the mountain and the river city, and the only stretch in Kanto that is really **two routes in
one**: the western half climbs to the cave mouth and the eastern half falls away in one-way ledges toward the city.
That one-way fall is the whole design of the place — the route is easy to finish and hard to walk back, which is
why every scene here is built around ledges, drops and a road you can only take in one direction.

---

## Where Route 4 sits in the bot

Route 4 is a single `Building` inside the joined road `kanto-route-3-mt-moon-and-route-4`:

```python
Building("r4", "Route 4", "town/route-4",
         "Past the cave the road drops in ledges towards Cerulean City. No way back up them.",
         people=(), area="route-4"),
```

with **no people at all**, and a spawn sub-area already pointing at it:

```python
{"key": "route-4", "label": "Route 4", "pool": "kanto-route-4"}
```

The battle field is the shared `kanto-route-3-mt-moon-and-route-4` at `(976, 392) — (458, 648)`, so trainers here
currently use the joined road's backdrop rather than anything specific to the route.

### What Fire Ash puts on this route

| Thing | Why it matters |
|---|---|
| A **Pokémon Center on the route itself** | one of only two route Centres in Kanto — the other is on Route 10. Losing it would make the mountain crossing much harsher |
| The **Magikarp salesman** inside that Center | sells a Magikarp for ₽500, no refunds. The best-known thing on the route |
| **Two Move Tutors** on the eastern side | Mega Kick and Mega Punch, one each |
| A **Lass on the highest hill** | reachable only by surfing over from Route 24; the only trainer in the eastern segment |
| A **little girl who trips over a boulder** she thought was a creature | canon flavour, and my favourite small detail in the whole set |

### Proposed buildings

| Key | Name | Scene | Blurb |
|---|---|---|---|
| `r4` | Route 4 | `town/route-4` | Past the cave the road drops in ledges towards Cerulean City. No way back up them. *(existing key)* |
| `r4w` | West Approach | `town/route-4-west` | The track climbs towards the cave mouth between low rock shelves. Some of the boulders look rounder than they should. |
| `r4c` | Route 4 Pokémon Center | `town/route-4-center` | A Center alone on the mountainside. The only warm roof for a long way in either direction. |
| `r4t` | Tutors' House | `town/route-4-tutors` | A low house with two training posts in the yard. Somebody here teaches punches that hit harder than they should. |
| `r4o` | The High Hill | `town/route-4-overlook` | The highest point on the route. The whole basin lies below, bridges and all. |
| `r4l` | The Ledges | `town/route-4-ledges` | Five shelves of flat stone. Easy down. Impossible up. |
| `r4f` | Tall Grass | `town/route-4-grass` | Deep grass either side of a thin path. Somebody has been through recently. |
| `r4r` | The River Crossing | `town/route-4-waterfall-side` | A three-plank bridge over fast water, with willows leaning in from both banks. |
| `r4e` | East Gate | `town/route-4-east-gate` | Two stone posts, a worn milestone, and the first rooftops of the city beyond. |
| `r4m` | Cave Mouth | `town/route-4-cave-mouth` | Back out in the daylight, looking up at the hole you came through. |

---

## Files — batch 1: place scenes (10)

| File | Key | Shows | Weight |
|---|---|---|---|
| `town/route-4.jpg` | `r4` | The road down: three low ledges splitting a dirt track that can only be followed toward the city far below | 545 KB |
| `town/route-4-west.jpg` | `r4w` | The climb to the cave mouth between rock shelves, big smooth boulders, tall grass and a blank marker post | 679 KB |
| `town/route-4-center.jpg` | `r4c` | The roadside Center: red hipped roof, glass doors, striped awning over a bench, a bicycle against the wall, a plain unlettered sign post | 561 KB |
| `town/route-4-tutors.jpg` | `r4t` | The tutors' house: timber and pale plaster, wide porch, two wooden training posts in a swept yard, staves against the wall, a rain barrel | 559 KB |
| `town/route-4-overlook.jpg` | `r4o` | The high hill: a golden crown of dry grass, one wind-bent tree, a flat boulder to sit on, the teal river basin and bridges far below | 539 KB |
| `town/route-4-ledges.jpg` | `r4l` | Five stepped shelves of grey stone with grassy lips, a path between each, a bare post at the top | 738 KB |
| `town/route-4-grass.jpg` | `r4f` | Deep stands of tall swaying grass either side of a trampled path, boulders half-swallowed, a broken stone wall behind | 659 KB |
| `town/route-4-waterfall-side.jpg` | `r4r` | Fast teal water over flat stones, a three-plank footbridge, reeds, leaning willows, grey crags rising beyond | 753 KB |
| `town/route-4-east-gate.jpg` | `r4e` | Two low stone gateposts, a blank milestone, and the city's first rooftops and a river bridge in morning haze | 755 KB |
| `town/route-4-cave-mouth.jpg` | `r4m` | Looking back at the cave: black opening in the crag, scree fanning out, the trail descending through ledges, a tipped hand cart | 789 KB |

---

## Still to come

| Batch | Contents | Count |
|---|---|---|
| 2 | Portraits — the Magikarp salesman, both Move Tutors, the Lass on the hill, the girl and the boulder, a hiker, a picnicker, a bird keeper, a camper | ~10 |
| 3 | Story beats — the ₽500 sale, the boulder that isn't, the ledge jump, the tutors' demonstration, the hilltop Lass — plus a `kanto-route-4` battle field split west and east | ~8 |
| 4 | The route maps (overview, west, east), both region views ringed, the labelled reference | ~6 |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten route scenes |
