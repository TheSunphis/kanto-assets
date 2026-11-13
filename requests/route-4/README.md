# Route 4 — asset request (Kanto)

Route 4 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**36 of 36 — the set is complete.** 10 place scenes, 10 portraits, 8 story beats, 2 battlefields, 4 route maps, 2 region views.

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

### Batch 2 — the people (10)

Five of these are the route's fixed furniture and five are the road's regulars. Every age is stated in the prompt on
purpose: the children are children, the old masters are old, and the salesman is a grown man who has done this before.

| File | Key | Role | Design | Weight |
|---|---|---|---|---|
| `people/magikarp-salesman.jpg` | `magikarp-salesman` | Sells a Magikarp for ₽500 in the Center. **No refunds** | **Man of forty-five**: narrow-faced, thin curled moustache, slicked hair, eyes half-closed in a sly grin, brown trench coat collar up, felt hat, one hand out palm-up | 114 KB |
| `people/tutor-mega-punch.jpg` | `tutor-mega-punch` | Teaches **Mega Punch** | **Man of seventy**: short, barrel-chested and enormous, bald with thick white brows, flattened nose, indigo gi with a white sash, fists up in a boxer's guard, scarred knuckles | 150 KB |
| `people/tutor-mega-kick.jpg` | `tutor-mega-kick` | Teaches **Mega Kick** | **Man of seventy**: tall and gaunt, thin grey topknot and wispy beard, white gi with a black sash, one bare foot held out straight in a slow high kick | 106 KB |
| `people/lass-crissy.jpg` | `lass-crissy` | The **only trainer on the eastern half**, up on the highest hill | **Girl of twelve**, child proportions: brown bob with a red ribbon, freckles, pale blue pinafore over a white blouse, satchel, one hand shading her eyes | 115 KB |
| `people/rock-girl.jpg` | `rock-girl` | Trips over a boulder she was sure was a creature | **Girl of seven**, unmistakably small: round cheeks, gap-toothed pout, yellow sundress with a green sash, one knee scraped and bandaged, hand rubbing the back of her head | 114 KB |
| `people/route4-hiker.jpg` | `route4-hiker` | Trainer on the west climb | **Woman of thirty**: wiry, dark braid, sunburnt, rust-orange rain shell, olive trousers with a knee patch, mud on her boots, walking pole planted beside her | 136 KB |
| `people/route4-bird-keeper.jpg` | `route4-bird-keeper` | Trainer watching the sky | **Man of nineteen**: lanky, straw-blond hair under a soft green cap, olive shirt sleeves rolled, binoculars round his neck, one hand raised to them | 114 KB |
| `people/route4-picnicker.jpg` | `route4-picnicker` | Trainer at the grass | **Woman of twenty-four**: wavy auburn hair with a checked scarf, freckles, cream sundress, straw hat hanging down her back, covered wicker basket | 132 KB |
| `people/route4-camper.jpg` | `route4-camper` | Trainer at the ledges | **Boy of seventeen**: skinny, sunburnt, backwards navy cap, plaster on one cheek, canvas rucksack with a frying pan tied on, hands on hips | 129 KB |
| `people/route4-traveller.jpg` | `route4-traveller` | Walks the route and complains about it | **Woman of seventy-five**: round-backed, grey bun under a dark headscarf, charcoal skirt, mustard cardigan, tartan shawl, basket over one arm, a hand on her aching back | 127 KB |

**Wiring:**

```python
"magikarp-salesman": "route-4", "tutor-mega-punch": "route-4", "tutor-mega-kick": "route-4",
"lass-crissy": "route-4", "rock-girl": "route-4", "route4-hiker": "route-4",
"route4-bird-keeper": "route-4", "route4-picnicker": "route-4", "route4-camper": "route-4",
"route4-traveller": "route-4",
```

`lass-crissy`, `route4-hiker`, `route4-bird-keeper`, `route4-picnicker` and `route4-camper` need `Trainer(...)`
entries if they are meant to battle — the salesman, both tutors, the girl and the old traveller are dialogue only.
The salesman also needs an item hook: ₽500 for a Magikarp, with **no refund** — that is the joke and it should
survive into the code.

### Batch 3 — story beats (8) and the two battlefields

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/route-4-magikarp-sale.jpg` | ₽500, no refunds | Inside the Center: the man in the trench coat leaning over the counter, one hand raised flat as if swearing an oath, sliding a cloth-wrapped bundle across; a trainer's back, cap and open purse in the foreground | 354 KB |
| `story/route-4-boulder.jpg` | The boulder that isn't | A smooth grey boulder as tall as a child in the grass, a very small girl in a yellow sundress leaning forward to point at it | 455 KB |
| `story/route-4-ledge-jump.jpg` | The drop | A trainer caught in mid-air below a stone lip, knees bent, straps flying, dust bursting where they are about to land and pebbles still falling | 387 KB |
| `story/route-4-tutors-demo.jpg` | Two ways to hit | The swept yard: one old master driving his fist into a rope-wrapped post with splinters flying, the other holding a high kick against the second post | 741 KB |
| `story/route-4-hill-lass.jpg` | The highest hill | A girl on a flat boulder at the crest, hand shading her eyes, the whole teal basin and its bridges below her | 841 KB |
| `story/route-4-center-night.jpg` | The only warm roof | The Center at night, walls washed moon-blue, yellow light on the path, a bicycle against the wall, one small figure hesitating at the door | 478 KB |
| `story/route-4-east-view.jpg` | Down into the city | Two stone gateposts framing the road, a blank milestone, and two travellers already ahead of us walking into the morning haze over the rooftops | 484 KB |
| `story/route-4-cave-return.jpg` | Out | Stepping out of the cave with an arm up against the glare, the trail and its ledges falling away below, the interior still a blue-black void behind | 625 KB |

**Battlefields.** The route currently shares the joined road's backdrop at `kanto-route-3-mt-moon-and-route-4`, which is
outdoor route art for a road that is really two different places. Splitting it:

| File | Proposed field key | Shows | Weight |
|---|---|---|---|
| `battle/bg/kanto-route-4-west.jpg` | `kanto-route-4-west` | The climb: plain dirt track, low rock shelves either side, big boulders at the edges, fence post and wire, the crags and cave mouth behind | 349 KB |
| `battle/bg/kanto-route-4-east.jpg` | `kanto-route-4-east` | The terrace above the valley: open gold grass, a lip of grey stone at the far edge, the teal river basin and the city in haze beyond | 490 KB |

Anchors for both: `(976, 392)` far — `(458, 648)` near, scale `1.0`. If only one key is wanted, use the **east** one —
that is where the trainers are, and the west half is mountain climbing rather than battling.

### Batch 4 — the route maps and both region views

**Route maps**, 1376 × 768 under `routeinfo/` — the category the installed `assets/route-4/routeinfo/route-4.jpg`
already lives in, so the overview drops straight into place:

| File | Shows | Weight |
|---|---|---|
| `routeinfo/route-4.jpg` | The whole route west to east: the climb with its boulders, the Center beside the road, the **cave mass filling the middle with a black opening on each face**, then the ledges falling east to the rooftops | 416 KB |
| `routeinfo/route-4-west.jpg` | The western half: the road climbing through three ledge steps, rock shelves with gaps, boulder scatters, the Center on its footpath, the cave mouth at the top | 496 KB |
| `routeinfo/route-4-east.jpg` | The eastern half: the cave mouth, six ledge steps down, the tutors' house with its swept yard, tall grass, the river and plank bridge along the bottom, the gateposts to the city | 547 KB |
| `routeinfo/route-4-center.jpg` | A detail map of the roadside Center: the building on its stone footpath, bicycle, lamp post, bench, two rock shelves stepping across the road behind, the crag above | 662 KB |

**Region views**, both ringed in code after checking where the mountain actually landed. The ring deliberately
catches **both cave mouths** — that is the whole route:

| File | Shows | Route 4 ringed at |
|---|---|---|
| `region/kanto-route-4.jpg` | The whole landmass: the mountain standing on the road between the western stone town and the eastern riverside city, a black cave mouth on each face, the descent east toward the city | `827, 163`, r 150 × 92 |
| `region/kanto-map-route-4.jpg` | The flat schematic: the same mountain drawn as one peak with both mouths cut into it, ledge marks on the eastern stretch, the blue city beyond | `680, 187`, r 245 × 135 |

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

## The set is complete

| Category | Count | Notes |
|---|---|---|
| Place scenes | 10 | `town/` — ten proposed building keys where the bot has one |
| Portraits | 10 | the salesman, both tutors, the hilltop Lass, the girl, and five road regulars |
| Story beats | 8 | the sale, the boulder, the drop, the demonstration, the hill, the night, the gate, the cave |
| Battlefields | 2 | `kanto-route-4-west`, `kanto-route-4-east` — split from the joined road's shared backdrop |
| Route maps | 4 | overview, west, east, Center detail |
| Region views | 2 | landmass and schematic, both ringed across both cave mouths |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten route scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the ten portraits |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — eight story beats and both battlefields |
| `review/_sheet-batch-4.jpg` | Batch 4 contact sheet — four route maps |
| `_route-4-labeled-reference.jpg` | The map side of the set at a glance, captioned, both ring coordinates printed |
