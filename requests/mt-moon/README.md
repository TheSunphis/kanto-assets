# Mt. Moon — asset request (Kanto, **Extras**)

Mt. Moon for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style, built to stand as its own
**Extra** — a non-town special place with its own folder, the way Sea Cottage does.

**35 of 35 — the set is complete.** 11 place scenes, 10 portraits, 6 story beats, 2 battlefields, 4 floor maps, 2 region views.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset |
| Pixel grid | Hard pixel edges, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, single figure 726 px tall, bottom-flush |
| Content rule | **Places** carry no people and no Pokémon — sprites and creatures are drawn by `card.py` at runtime. **Story** beats may and should contain people |
| Light | Cave interior: cold blue-grey rock, one warm or pale beam; the two exteriors carry the sky |

---

## Where Mt. Moon has to sit in the bot

Right now Mt. Moon **is not a location**. It exists only as two `Building`s buried in the joined road:

```python
# people.py, inside BUILDINGS["kanto-route-3-mt-moon-and-route-4"]
Building("mm", "Mt. Moon", "town/mt-moon", "A dark cave full of Zubat. You hear footsteps deeper inside.",
         ("bug-catcher-kent", "hiker-marcos", "lass-iris", "super-nerd-jovan", "moon-rocket"), area="mt-moon"),
Building("fr", "Fossil Chamber", "town/mt-moon-fossils", "Two fossils lie on a rock. Someone is guarding them.",
         ("super-nerd-miguel",), area="mt-moon"),
```

and the six people are `Person(..., "kanto-route-3-mt-moon-and-route-4", ...)`. Promoting it to an Extra
means four edits, all of them outside the art:

| File | Change |
|---|---|
| `world.py` | `KANTO_TOWNS["mt-moon"] = ("Mt. Moon", "A cave bored through the mountain, cold and full of echoes.", 4, 0.4, "above")` — between Pewter `(2, 1)` and Cerulean `(6, 1)`, which is where Routes 3 and 4 actually meet it |
| `world.py` | add `"mt-moon"` to `KANTO_SPOTS`, to `NO_HEAL` (no Center inside a cave), and `MAP_PICTURE["mt-moon"] = "cerulean-city"` so the region map shows it on a neighbour's picture until it has its own |
| `people.py` | new `BUILDINGS["mt-moon"] = (...)` holding `mm`, `fr` and the new rooms this set adds — keys and blurbs below. Delete the two `Building`s from the road list and re-point the six `Person(...)` locations at `"mt-moon"` |
| `trainers.py` + `spawns.py` | the four trainers on the road (`bug-catcher-kent`, `hiker-marcos`, `lass-iris`, `super-nerd-jovan`) and `moon-rocket`/`super-nerd-miguel` move with them; the `{"key": "mt-moon", "label": "Mt. Moon 1F", "pool": "kanto-mt-moon-1f"}` sub-area stops being a sub-area of the road and becomes the Extra's own hunt area |

Battle fields: `card.FIELDS` has **no cave key at all** — every trainer in here currently fights on
`kanto-route-3-mt-moon-and-route-4`, which is outdoor route art. Two new keys are proposed in batch 3.

### Proposed building keys

| Key | Name | Scene | Blurb |
|---|---|---|---|
| `mm` | Mt. Moon | `town/mt-moon` | A dark cave full of Zubat. You hear footsteps deeper inside. |
| `fr` | Fossil Chamber | `town/mt-moon-fossils` | Two fossils lie on a rock. Someone is guarding them. |
| `en` | Cave Mouth | `town/mt-moon-entrance` | The path ends at a black opening in the rock. |
| `ps` | Narrow Passage | `town/mt-moon-passage` | Timber props hold the ceiling up. The drafts never stop. |
| `ld` | Ladder Shaft | `town/mt-moon-ladders` | Three ladders, three floors, and no way to tell which way is out. |
| `st` | Underground Stream | `town/mt-moon-stream` | Black water, flat stones, and a cold smell of stone. |
| `dp` | Lower Cavern | `town/mt-moon-deep` | The floor has collapsed. Mind the holes. |
| `ex` | Route 4 Exit | `town/mt-moon-exit` | Daylight, and a stair down to the grass. |
| `cr` | The Moon Shaft | `town/mt-moon-crater` | Moonlight falls all the way to the bottom of the mountain. |
| `cy` | Crystal Chamber | `town/mt-moon-crystals` | The crystals light the water better than a lantern would. |

---

## Files — batch 1: place scenes (9 of 10)

| File | Key | Shows | Weight |
|---|---|---|---|
| `town/mt-moon-fossils.jpg` | `fr` | The fossil shelf: two shells half-exposed in layered rock, cut back in clean steps, lit by one warm crack of light, a fallen stalactite below | 310 KB |
| `town/mt-moon-entrance.jpg` | `en` | The cave mouth at night from outside: jagged black opening in a rock face, scree, a dirt trail with a signpost and rope fence, moon and stars above | 427 KB |
| `town/mt-moon-passage.jpg` | `ps` | A narrow winding passage: timber pit props, a lantern bracket with no lantern, water running down one face, blue light ahead and shadow behind | 378 KB |
| `town/mt-moon-ladders.jpg` | `ld` | A vertical shaft with three stacked ladders bolted at different heights, ledges at each level, a frayed rope, one pale rectangle of moonlight at the top | 325 KB |
| `town/mt-moon-stream.jpg` | `st` | Underground stream: black-blue water, three flat stepping stones, smooth wet boulders, rippling reflected light on the walls | 346 KB |
| `town/mt-moon-deep.jpg` | `dp` | The collapsed lower floor: a wide hole dropping into darkness, broken ledges at different heights, one stone bridge, a dim glow from below | 641 KB |
| `town/mt-moon-exit.jpg` | `ex` | The far exit from inside: a ragged opening flooding the chamber with dawn light, a stair cut down to green grass, dust in the beams | 435 KB |
| `town/mt-moon-crater.jpg` | `cr` | The moon shaft: tiered rock ledges rising to a jagged hole, one huge beam of moonlight striking a flat slab ringed by standing stones | 267 KB |
| `town/mt-moon-crystals.jpg` | `cy` | A crystal chamber: sharp teal formations at every angle, a still reflecting pool, the crystals lighting the ceiling themselves | 548 KB |

### Batch 2 — the cave's mouth, and nine people

`town/mt-moon.jpg` was regenerated as a **scene** rather than a map and is now the third-floor main chamber:
dirt floor, boulders, two ladders on the ledges, a broken crate, one moonbeam from a hole in the ceiling.

The six people already installed in `assets/mt-moon/people/` were **1280 × 796 scene images** with a drawn cave
behind each figure. All six are redrawn here to the real spec — single figure, cream, 726 px, bottom-flush.

| File | Key | Design | Weight |
|---|---|---|---|
| `people/bug-catcher-kent.jpg` | `bug-catcher-kent` | A **boy of twelve**, child proportions: straw sun hat, short yellow tee, blue shorts, butterfly net over one shoulder, looking nervous | 136 KB |
| `people/lass-iris.jpg` | `lass-iris` | A **girl of twelve**: pigtails with red ribbons, pale green dress over a white blouse, hands clasped, looking up hopefully | 98 KB |
| `people/super-nerd-jovan.jpg` | `super-nerd-jovan` | A **teenager of sixteen**: lanky, bowl cut, round glasses, white shirt buttoned to the collar, notebook open mid-note | 84 KB |
| `people/super-nerd-miguel.jpg` | `super-nerd-miguel` | A **teenager of seventeen**: curly hair, thick glasses, lab coat over a green shirt, both arms spread wide to block the way | 114 KB |
| `people/hiker-marcos.jpg` | `hiker-marcos` | A **man of forty**: burly, bushy beard, knitted beanie, red-and-black flannel, loaded backpack with a bedroll | 140 KB |
| `people/moon-rocket.jpg` | `moon-rocket` | **Man in Black**, adult: black peaked cap and uniform, plain red circle emblem, torch on the belt, arms folded, smug | 83 KB |
| `people/seymour.jpg` | `seymour` **new** | **Man of forty-five**, the Clefairy researcher: thinning hair, wire glasses, lab coat over a green field shirt, satchel strap, notebook and pencil | 123 KB |
| `people/rocket-scout.jpg` | `rocket-scout` **new** | **Woman of twenty-eight**, adult: lean and alert, dark hair through the back of a black cap, plain red circle emblem, coiled rope, hand raised to peer into the dark | 83 KB |
| `people/fossil-maniac.jpg` | `fossil-maniac` **new** | **Man of sixty-five**, elderly: weathered face, white moustache, goggles pushed up onto his forehead, patched canvas coat, satchel, rock hammer | 134 KB |

**Wiring for the three new people** — each needs a `Person(...)` in `people.py` and a line in `PORTRAITS`:

```python
"seymour": "mt-moon", "rocket-scout": "mt-moon", "fossil-maniac": "mt-moon",
```

`seymour` and `fossil-maniac` are dialogue characters, not trainers — no `trainers.py` entry. `rocket-scout` is a
second body for the cave's Rocket presence; if she should fight, she needs a `Trainer(...)` in `trainers.py` on the
new `mt-moon` location, otherwise she is a `Person` only.

### Batch 3 — story, and the two battlefields

`card.FIELDS` has **no cave key**, so every trainer in here currently fights on `kanto-route-3-mt-moon-and-route-4` —
outdoor route art with a cave's trainers standing in it. Two files fix that.

**Battlefields**, both 1376 × 768, empty of figures as always:

| File | Proposed field key | Shows | Weight |
|---|---|---|---|
| `battle/bg/mt-moon-cave.jpg` | `mt-moon-cave` | The floor of a cave chamber: broad open dirt arena deliberately plain in the middle, boulders and rock shelves behind, two timber pit props, one moonbeam on the middle distance | 262 KB |
| `battle/bg/mt-moon-crater.jpg` | `mt-moon-crater` | The moon shaft as an arena: flat ring of pale stone, tiered ledges stepping up behind, a ring of standing stones either side of a column of moonlight | 338 KB |

Anchors for both, by the convention every other field uses: `(976, 392)` far — `(458, 648)` near, scale `1.0`.

**Story beats** — six, and these are allowed to carry people, because a story frame is a frozen moment:

| File | Beat | Shows | Weight |
|---|---|---|---|
| `story/mt-moon-fossil-choice.jpg` | Miguel's claim | The shelf with both fossils lit brightest in the frame, a teenage boy in a white coat at the edge of it, arms spread wide, face turned away | 275 KB |
| `story/mt-moon-rocket-fossil.jpg` | The Man in Black | A black-clad man crouched at the shelf with a torch held low, one glove flat on the stone, a canvas bag open and empty beside him | 343 KB |
| `story/mt-moon-two-grunts.jpg` | Two of them | A broad man and a lean woman in black facing each other across a lantern in a propped passage, both in near-silhouette | 386 KB |
| `story/mt-moon-collapse.jpg` | The rockfall | Rubble across the passage, dust rolling forward, a child in a straw hat crouched low with both arms over their head | 325 KB |
| `story/mt-moon-crater-moonlight.jpg` | The shaft fully lit | Tiered ledges up to the opening, one huge column of moonlight on the slab, the ring of standing stones, dust suspended in the beam. Empty — the moment belongs to the place | 309 KB |
| `story/mt-moon-exit-dawn.jpg` | Out | A ragged opening framing a pink-and-gold sky, sunrise raking the floor, one small backpacked figure walking out with a hand up against the glare | 404 KB |

The dawn frame is the loudest in the set — the sky is deliberately hotter than anything else here, because it is the
only warm light in a cold place. If it reads as too much beside the cave scenes, it is the first candidate for a re-roll.

**One more portrait**, also in this batch:

| File | Key | Design | Weight |
|---|---|---|---|
| `people/moon-gazer.jpg` | `moon-gazer` **new** | **Man of fifty-five**: thinning grey hair and beard, plaid blanket-coat over a wool sweater, brass lantern low in one hand, walking stick in the other. He is the one who climbs up for every full moon | 137 KB |

Wiring: `"moon-gazer": "mt-moon"` in `PORTRAITS`, plus a `Person(...)`. Dialogue only.

### Batch 4 — floor maps and the two region views

**Floor maps**, 1376 × 768 under `routeinfo/` — the same category the installed `assets/mt-moon/routeinfo/mt-moon.jpg`
already lives in, so these drop into place:

| File | Floor | Shows | Weight |
|---|---|---|---|
| `routeinfo/mt-moon.jpg` | Overview | The whole cave as one plan: chambers joined by winding tunnels, dead ends, streams, boulder scatters, ladders between levels, openings at west and east where the road passes through | 533 KB |
| `routeinfo/mt-moon-1f.jpg` | Entry level | The entrance chamber, the long diagonal to the central cavern with its two alcoves, the narrow way east, two ladders down, a stream along the bottom | 501 KB |
| `routeinfo/mt-moon-b2f.jpg` | Collapsed level | Three pits breaking the floor into islands joined by single-file bridges, side chambers north, two ladders, a crystal alcove | 283 KB |
| `routeinfo/mt-moon-fossil-chamber.jpg` | Fossil chamber | One room, the raised shelf on the north wall carrying both fossils, a single corridor in from the south, a ladder at the east corner | 291 KB |

**Region views**, both ringed in code after checking where the mountain actually landed:

| File | Shows | Mt. Moon ringed at |
|---|---|---|
| `region/kanto-mt-moon.jpg` | The whole Kanto landmass: ridges north, forest west, the southern port, the volcano island below — and a single grey-brown mountain standing over the road with a black cave mouth at its foot | `840, 190`, r 125 × 110 |
| `region/kanto-map-mt-moon.jpg` | The flat schematic: pale land, grey ridges, blue coast, two southern islands, with the mountain drawn as one rounded peak and the cave mouth cut into its base | `692, 155`, r 148 × 105 |

Two rejection-and-retry rounds were needed on the landmass view: the first came back as a zoomed-in corner rather than
the whole region, and the second came back wordless in the right framing but with the region's map style intact. The
schematic's peak reads a little like the volcano island drawn grey — different enough at a glance, and it is the
smaller of the two files.

### Note on the art already in `assets/mt-moon/`

Both installed town scenes were 1280 × 796. Both are now replaced here at 1408 × 768: `town/mt-moon` is the main
chamber, `town/mt-moon-fossils` is the fossil shelf, redrawn to match the rest of the set.

---

## The set is complete

| Category | Count | Notes |
|---|---|---|
| Place scenes | 11 | `town/` — one per proposed building key, including both installed filenames redrawn |
| Portraits | 10 | six redrawn from scene-style originals, four new (`seymour`, `rocket-scout`, `fossil-maniac`, `moon-gazer`) |
| Story beats | 6 | the fossil choice, the Man in Black, two grunts, the rockfall, the lit shaft, the dawn exit |
| Battlefields | 2 | `mt-moon-cave`, `mt-moon-crater` — no cave field key existed before |
| Floor maps | 4 | overview, entry level, collapsed level, fossil chamber |
| Region views | 2 | landmass and schematic, both ringed |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the nine cave scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the nine portraits |
| `review/_sheet-batch-3.jpg` | Batch 3 contact sheet — fossil shelf, moon gazer, six story beats, both battlefields |
| `review/_sheet-batch-4.jpg` | Batch 4 contact sheet — four floor maps, two region views |
| `_mt-moon-labeled-reference.jpg` | The map side of the set at a glance, captioned, both ring coordinates printed |
