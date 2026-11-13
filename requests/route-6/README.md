# Route 6 — asset request (Kanto)

Route 6 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 of ~35 — batch 1: the road itself, in ten scenes.** Everything here is staged for review; nothing is installed.

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

### What Route 6 is

The first route in Kanto with a fight on it after two quiet ones. It runs south from the great gate of Saffron
City down to the port of Vermilion, and it is crowded with *structure*: the gatehouse at the top, **two**
Underground Path housings, a pair of ledges with a gap in them, two elevated platforms that hide a Sitrus Berry
and a Rare Candy, a long ragged grass patch, and a pond in the south-east with a jetty on it.

It also carries the whole point of the Saffron problem. Until the guard at Saffron's gate has had his Tea from
Celadon, the Underground Path is the **only** way round the city — Route 6 is where that shortcut comes out, and
the route is effectively the road to Vermilion for anyone without a drink to spare.

**Six trainers live here**, all of them optional in the cartridge but impossible to ignore in a bot that lets you
walk into them: two Bug Catchers, two Campers and two Picnickers, all around level 16–20 — Keigo, Ricky, Nancy,
Elijah, Isabelle and Jeff.

---

## Where Route 6 sits in the bot

Route 6 is the emptiest road in Kanto **in code**: it is listed as the road between Saffron and Vermilion, and
that is all it is.

```python
("saffron-city", "vermilion-city", "Route 6", []),
```

| Gap | Detail |
|---|---|
| **No buildings at all** | `BUILDINGS` has no `kanto-route-6` key. Route 5 at least had one entry with a blurb; Route 6 has *nothing* to open, so a trainer standing on it can only look at the map |
| **No field key** | `card.FIELDS` has no `kanto-route-6` at all — Route 5 at least had `(976, 380, 480, 640)` waiting for art. Anything that fights on Route 6 falls back to bare `grass` |
| **No spawn table** | `spawns.py` has no `kanto-route-6` entry, so nothing can be encountered here |

The two Underground Path housings, the ledges, the berry platforms and the pond are not in the bot in any form.
This set gives every one of them a key, a scene and a blurb.

### Proposed buildings

| Key | Name | Scene | Blurb |
|---|---|---|---|
| `r6` | Route 6 | `town/route-6` | The road south from Saffron's gate, running between white fences and lawns toward Vermilion. *(new)* |
| `sg` | Saffron Gate | `town/route-6-gate` | The south gatehouse of Saffron City. Solid stone, an iron portcullis, and a guard with a decision to make. *(new)* |
| `u5` | Underground Path 5–6 | `town/route-6-underground-56` | A brick stair-house beside the road. The stairs go down under Saffron and come up on Route 5. *(new)* |
| `u6` | Underground Path 6–7 | `town/route-6-underground-67` | A squat stone shelter on the east side of the road. Ten lamps and a long walk to Route 7. *(new)* |
| `ld` | The Ledges | `town/route-6-ledges` | Two shelves of rock across the hill with a gap between them. Drop off the top one and you are not coming back up. *(new)* |
| `pl` | Berry Plateau | `town/route-6-plateau` | A raised square of turf beside the road with a stone marker, a bench, and a berry bush. *(new)* |
| `gf` | The Grass Patch | `town/route-6-grass` | A long ragged field of tall grass. Two Bug Catchers work this one. *(new)* |
| `pd` | The Pond | `town/route-6-pond` | A still pond in the south-east corner, reeds, lily pads and a short wooden jetty. *(new)* |
| `se` | South End | `town/route-6-south-end` | Where the road becomes a street and the air smells of salt and rope. Vermilion is a few paces on. *(new)* |
| `vb` | Looking Back | `town/route-6-view-back` | The climb north in evening light, all the way up to the wall and the tower. *(new)* |

### Proposed field keys

Two, on the house anchors, closed for Route 5 and reused here:

| Field key | Anchors (far — near) | Scale | Art |
|---|---|---|---|
| `kanto-route-6` | `(976, 380)` — `(480, 640)` | 1.0 | `battle/bg/kanto-route-6.jpg` *(batch 3)* |
| `kanto-route-6-underground` | `(976, 380)` — `(480, 640)` | 1.0 | `battle/bg/kanto-route-6-underground.jpg` *(batch 3)* |

### Proposed spawn table

Straight from the cartridge, FireRed weights, so Route 6 finally has something in it:

```python
"kanto-route-6": [("pidgey", 40, 13, 16), ("meowth", 35, 10, 16), ("bellsprout", 25, 13, 16)],
```

LeafGreen swaps `bellsprout` for `oddish`; the pond answers to surf (Psyduck FR / Slowpoke LG) and the rods
answer to Magikarp, Poliwag and Goldeen.

---

## Files — batch 1: place scenes (10)

| File | Key | Shows | Weight |
|---|---|---|---|
| `town/route-6.jpg` | `r6` | The paved road running away between white post-and-rail fences, hedges and lawns, the city wall and its gatehouse tower on the horizon | 391 KB |
| `town/route-6-gate.jpg` | `sg` | The south gatehouse: pale stone, a wide arch with the portcullis raised into shadow, ivy on one corner, walls running away along hedged banks | 789 KB |
| `town/route-6-underground-56.jpg` | `u5` | The west stair-house: red brick with whitewashed courses, a dark doorway, and a sunken stone stair with a green iron handrail going down | 567 KB |
| `town/route-6-underground-67.jpg` | `u6` | The east entrance: a squat stone shelter with a blue-grey tiled roof, a broad flight of steps turning out of sight, a blank notice board | 419 KB |
| `town/route-6-ledges.jpg` | `ld` | Two long stone ledges cut across a green hill, grass fringing every lip, hard shadow beneath, a paved path switchbacking through the gap | 375 KB |
| `town/route-6-plateau.jpg` | `pl` | The raised platform: mown turf on a pale rock cliff, a berry bush with red fruit, a blank stone marker, a wooden bench, a ramp down to the road | 428 KB |
| `town/route-6-grass.jpg` | `gf` | A long ragged patch of deep tall grass with a trodden gap through it, a leaning blank signpost, a ditch and a hawthorn hedge behind | 678 KB |
| `town/route-6-pond.jpg` | `pd` | The pond: flat teal water with hard ripple bands, lily pads, reeds and bulrushes, a three-post jetty, a willow at the left | 643 KB |
| `town/route-6-south-end.jpg` | `se` | The route becoming a port street: palms with striped trunks, a striped shop awning, blue and green tiled roofs, masts and grey water beyond, a blank milestone | 636 KB |
| `town/route-6-view-back.jpg` | `vb` | The climb seen from the south in gold evening light: switchback road, white fences, a clump of trees, the walled city and one lit window on the skyline | 464 KB |

---

## Still to come

| Batch | Contents | Count |
|---|---|---|
| 2 | Portraits — the six trainers, plus the gate guard, the tunnel lamp-man, a fisherman at the pond and a walker on the road | 10 |
| 3 | Story beats (8) and both battlefields | 10 |
| 4 | Route maps (3), both region views ringed, the labelled reference | 5 |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten route scenes |
