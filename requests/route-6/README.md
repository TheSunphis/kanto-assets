# Route 6 — asset request (Kanto)

Route 6 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**35 of 35 — route closed.** Batches 1–4: the road, its people, the story beats, both battlefields, the three route maps and both ringed region views. Everything here is staged for review; nothing is installed.

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

### Batch 2 — the people (10)

Every figure is ONE full-body sprite on flat cream `(244,245,227)`, 726 px to the floor of a 1376 × 768 frame,
48 colours, no scenery, no shadow. **The six trainers are the cartridge's own roster** for this route — same
classes, same names, same teams — because a bot that lets you walk into a trainer should not invent one.

| File | Key | Who | Age | Shows | Weight |
|---|---|---|---|---|---|
| `people/bug-catcher-keigo.jpg` | `bug-catcher-keigo` | **Bug Catcher Keigo** | 11 | Straw hat with a red band, pale green shirt, brown shorts and suspenders, sandals, a net held upright and an empty jar | 145 KB |
| `people/bug-catcher-elijah.jpg` | `bug-catcher-elijah` | **Bug Catcher Elijah** | 13 | Lankier, red cap worn backwards, orange-and-white striped jersey, a butterfly net over one shoulder, hand on hip | 112 KB |
| `people/camper-ricky.jpg` | `camper-ricky` | **Camper Ricky** | 14 | Green cap, khaki scout shirt with a neckerchief, olive shorts, hiking boots, bulging rucksack with a sleeping mat | 121 KB |
| `people/camper-jeff.jpg` | `camper-jeff` | **Camper Jeff** | 15 | Red cap, red-and-white striped shirt, denim shorts, soft rucksack, water bottle out, one hand waving | 111 KB |
| `people/picnicker-nancy.jpg` | `picnicker-nancy` | **Picnicker Nancy** | 14 | Pigtails with red ribbon, freckles, white blouse under denim dungarees, wicker basket and a folded check cloth | 125 KB |
| `people/picnicker-isabelle.jpg` | `picnicker-isabelle` | **Picnicker Isabelle** | 15 | Black bob, wide sun hat with a yellow ribbon, yellow sundress, satchel and a pale hamper | 113 KB |
| `people/route6-gate-guard.jpg` | `route6-gate-guard` | Gate guard, Saffron's south gate | **46** | Slate-blue tunic with brass buttons, peaked cap, white gloves, a steaming teacup and a clipboard — broad, grey-moustached, unmistakably an adult | 112 KB |
| `people/tunnel-lamp-man.jpg` | `tunnel-lamp-man` | Lamp man, Underground Path | **58** | Flat cap, oil-stained brown overalls, a long brass lighter pole upright, replacement wicks and an oil can on his belt | 109 KB |
| `people/pond-fisherman.jpg` | `pond-fisherman` | Fisherman at the pond | **44** | Green bucket hat, khaki vest with too many pockets, waterproof trousers and boots, rod over one shoulder, bait bucket | 152 KB |
| `people/route6-sailor.jpg` | `route6-sailor` | Sailor walking inland | **33** | White cap with a black ribbon, sailor top with a blue collar, duffel bag on a rope handle, coiled line on his belt | 94 KB |

The four adults are drawn as adults — heavier build, set faces, grey in the guard's moustache and the lamp man's
stubble — so nobody has to guess whether a grown-up is standing in the gate. The six trainers are the ages their
classes imply, and look it.

### Batch 3 — story beats (8) and both battlefields

Route 6's beats are all arrivals and obstructions: you come up out of a tunnel into the light, you squeeze through
the gap in the ledges, you get jumped in the grass, you find the gate shut in your face. Each one carries people,
because a beat with nobody in it is just another landscape.

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/route-6-tunnel-out.jpg` | Out of the dark | A trainer climbs the last three steps out of the sunken stairwell, one hand shading their eyes, satchel swinging, the road running away south toward distant rooftops | 446 KB |
| `story/route-6-berry-hill.jpg` | What the hill hides | A trainer crouched on the raised platform, one hand pulling a berry bush aside, the other steadying an open pouch — round red berries, a blank marker, a bench, the drop to the road behind | 416 KB |
| `story/route-6-ledge-gap.jpg` | Through the gap | A trainer braced between the two stone ledges, one boot up on the rock, one hand on the lip, backpack straps held tight, looking down at the drop | 449 KB |
| `story/route-6-grass-ambush.jpg` | The grass patch | Keigo up out of the tall grass with his net raised in both hands and his mouth open, a trainer in a red cap turning toward him, hand going to their belt | 593 KB |
| `story/route-6-picnic.jpg` | Cloth by the pond | Two Picnickers on a check cloth — flask, enamel cups, sandwiches, a folded sun hat — reeds and the jetty behind, one laughing, one pouring | 571 KB |
| `story/route-6-gate-locked.jpg` | Shut out | Night at the south gate: portcullis down and locked, a guard with a lantern and a palm-out hand, a trainer stopped on the wet paving, two lit windows high in the wall | 619 KB |
| `story/route-6-lamp-down.jpg` | Ten lamps | The tunnel corridor by lamplight, an old lamp man on a stool reaching up with his brass pole as the flame catches, a trainer walking under him with one hand on the wall | 392 KB |
| `story/route-6-pond-fisher.jpg` | Nothing biting | The fisherman on the end of the jetty, line tight and motionless, a trainer sitting behind him with chin in hand and plainly nothing to do | 434 KB |

**Both battlefields.** Route 6 had no field key at all, so every fight on it fell back to bare `grass` — the
generic field used by half of Kanto. These two fill that in, on the house anchors:

| File | Field key | Shows | Weight |
|---|---|---|---|
| `battle/bg/kanto-route-6.jpg` | `kanto-route-6` *(new)* | Mown grass and pale paving in the foreground, a white post-and-rail fence across the middle with a clear gap, tall grass beyond it, round bushes and one flowering tree at the sides, the walled city's tower low on the horizon | 339 KB |
| `battle/bg/kanto-route-6-underground.jpg` | `kanto-route-6-underground` *(new)* | Flagged stone floor, blue-grey glazed brick with a whitewashed band, two green-shaded bracket lamps with warm pools of light and hard shadow between them, a bench and bin pushed to the wall | 373 KB |

Anchors for both: `(976, 380)` far — `(480, 640)` near, scale `1.0`, the same anchors Route 5 uses. The
underground field matters only if the tunnel becomes its own hunt area; the route field is the one that pays for
itself today, because Route 6 is the first route since Route 4 with trainers standing on it.

### Batch 4 — route maps (3) and region views (2)

Route 6 is short and mostly vertical: gate at the top, grass and water at the bottom, and a crowd of small
structures in between that are hard to hold in your head from the scene pictures alone. Three maps fix that.

| File | Shows | Weight |
|---|---|---|
| `routeinfo/route-6.jpg` | The whole route on one screen: the city wall and its gate at the top, the road running straight down between fenced lawns, both stair-houses above the middle, the two ledges on the right, the grass patch below them, the pond bottom-right and the port rooftops at the very bottom | 494 KB |
| `routeinfo/route-6-north.jpg` | The northern half in detail: the gatehouse and its apron, the sunken brick stair on the left, the stone shelter on the right, the two ledges with their gap, the raised platform with its bench and bush | 520 KB |
| `routeinfo/route-6-south.jpg` | The southern end: the tall grass with its leaning signpost and ditch, the pond with jetty, reeds and lily pads, the road bending east into a street of palms, tiled roofs and a strip of sea | 669 KB |

Both region views are the whole Kanto landmass with **empty sea in the corners**, no captions of any kind, ringed
in the house colours (8 px `(120,84,26)` inside 5 px `(247,201,72)`):

| File | Shows | Ring | Weight |
|---|---|---|---|
| `region/kanto-route-6.jpg` | The illustrated region view; the ring sits on the road between the inland city and the coastal road | centre `1118,420`, radius 46 × 62 | 336 KB |
| `region/kanto-map-route-6.jpg` | The flat schematic map; same road, one square of town at the junction | centre `1052,470`, radius 42 × 60 | 183 KB |

The ring is small again, and honestly: Route 6 is a few hundred paces of road. It is *dense* paces — two tunnel
mouths, a gate, two ledges, a pond and six trainers — but on a map of Kanto it is a dot. A labelled reference
sheet, `_route-6-labeled-reference.jpg`, puts the five plus one story frame in a single view with the ring
coordinates printed under each panel.

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten route scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the ten portraits |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — eight story beats and both battlefields |
| `review/_sheet-batch-4.jpg` | Batch 4 contact sheet — three route maps and both ringed region views |

---

## Wiring — what to paste

Ten `Person` entries, all standing on `kanto-route-6`. The portrait lookup needs the keys added to
`KANTO_PORTRAITS` too, or they fall back to the picture of the building they stand in:

```python
KANTO_PORTRAITS |= {"bug-catcher-keigo", "bug-catcher-elijah", "camper-ricky", "camper-jeff",
                    "picnicker-nancy", "picnicker-isabelle", "route6-gate-guard", "tunnel-lamp-man",
                    "pond-fisherman", "route6-sailor"}
```

```python
Person("bug-catcher-keigo", "Bug Catcher Keigo", "kanto-route-6", (
    ("The grass patch is full of bugs today! Look at this one, wait, don't look at it.",),
)),
Person("bug-catcher-elijah", "Bug Catcher Elijah", "kanto-route-6", (
    ("BUTTERFREE! Raised it from a Caterpie. It only knows powder moves and it still wins.",),
)),
Person("camper-ricky", "Camper Ricky", "kanto-route-6", (
    ("Me and my Squirtle walked down from the gate. Saffron was locked up tight.",),
    ("The guard wants some special tea before he opens it. Tea!",),
)),
Person("camper-jeff", "Camper Jeff", "kanto-route-6", (
    ("You came out of the tunnel? Long walk, that. I would rather climb the ledges.",),
)),
Person("picnicker-nancy", "Picnicker Nancy", "kanto-route-6", (
    ("We set the cloth out by the pond. There's room if you want to sit.",),
)),
Person("picnicker-isabelle", "Picnicker Isabelle", "kanto-route-6", (
    ("Three Pidgey. Three! They eat like a whole picnic on their own.",),
)),
Person("route6-gate-guard", "Gate Guard", "kanto-route-6", (
    ("Saffron is closed. Gate's closed, road's closed, the lot.", "Come back when you can do something about my thirst."),
    ("Oh, is that tea? From Celadon? Go on then. Go on through.",),
)),
Person("tunnel-lamp-man", "Lamp Man", "kanto-route-6", (
    ("Ten lamps from here to the far stairs. I light them all, twice a day.",),
)),
Person("pond-fisherman", "Fisherman", "kanto-route-6", (
    ("Nothing biting. Nothing has bitten since spring.",),
)),
Person("route6-sailor", "Sailor", "kanto-route-6", (
    ("Vermilion's a short walk south. You can smell the harbour from the top of the hill.",),
)),
```

Six of them are trainers, and the cartridge's team is the team here:

```python
Trainer("bug-catcher-keigo", "Bug Catcher Keigo", "Bug Catcher", "kanto-route-6",
        (("weedle", 16, None), ("caterpie", 16, None), ("weedle", 16, None)), 48, "kanto-route-6"),
Trainer("bug-catcher-elijah", "Bug Catcher Elijah", "Bug Catcher", "kanto-route-6",
        (("butterfree", 20, None),), 60, "kanto-route-6"),
Trainer("camper-ricky", "Camper Ricky", "Camper", "kanto-route-6",
        (("squirtle", 20, None),), 100, "kanto-route-6"),
Trainer("camper-jeff", "Camper Jeff", "Camper", "kanto-route-6",
        (("spearow", 16, None), ("raticate", 16, None)), 80, "kanto-route-6"),
Trainer("picnicker-nancy", "Picnicker Nancy", "Picnicker", "kanto-route-6",
        (("rattata", 16, None), ("pikachu", 16, None)), 80, "kanto-route-6"),
Trainer("picnicker-isabelle", "Picnicker Isabelle", "Picnicker", "kanto-route-6",
        (("pidgey", 16, None), ("pidgey", 16, None), ("pidgey", 16, None)), 80, "kanto-route-6"),
```

Prize money is the cartridge figure at the bot's one-quarter scale (₱192 → ₱48, ₱400 → ₱100, ₱320 → ₱80,
₱240 → ₱60). All six use the `kanto-route-6` field, which now has art behind it in
`battle/bg/kanto-route-6.jpg`; the field key and the anchors it needs are in the batch 3 table above.

---

## Totals

| Group | Count |
|---|---|
| Place scenes (`town/`) | 10 |
| Portraits (`people/`) | 10 |
| Story beats (`story/`) | 8 |
| Battlefields (`battle/bg/`) | 2 |
| Route maps (`routeinfo/`) | 3 |
| Region views (`region/`) | 2 |
| **Assets** | **35** |
| Contact sheets (`review/`) | 4 |
| Labelled reference | 1 |
| This README | 1 |
| **Files under `requests/route-6/`** | **41** |

Route 6 is complete. The route that existed in the bot as one line of text — no buildings, no field key, no
spawns — now has ten places to open, ten people to meet, six of them trainers with the cartridge's own teams,
eight beats, two battlefields, and maps to look at. **Route closed.**
