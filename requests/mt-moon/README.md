# Mt. Moon — asset request (Kanto, **Extras**)

Mt. Moon for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style, built to stand as its own
**Extra** — a non-town special place with its own folder, the way Sea Cottage does.

**9 of ~40 — batch 1: the cave.** The tenth image of the batch was rejected (see *Rejected* below) and is
held over. Everything here is staged for review; nothing is installed.

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

### Rejected

`town/mt-moon.jpg` came back as a **top-down map with tiled maze walls** — the wrong register entirely, and
the one filename the installed set already uses. Regenerating it first in batch 2.

### Note on the art already in `assets/mt-moon/`

All six portraits there are **1280 × 796 scene images** — each figure standing in a drawn cave with a ladder,
a stream and glowing crystals behind them — not 1376 × 768 cream-background portraits. The two town scenes are
the cave exterior and the fossil shelf at 1280 × 796 as well. They read beautifully but none of them matches the
portrait spec, so batch 2 redraws the six people properly rather than layering new portraits beside them.

---

## Still to come

| Batch | Contents | Count |
|---|---|---|
| 2 | `mt-moon` place scene, then the six existing people redrawn as spec portraits, plus Seymour the Clefairy researcher, a second Rocket, a fossil maniac and a Clefairy watcher | ~10 |
| 3 | Story beats — the fossil choice, the Man in Black, the moonlit shaft — and two cave battle fields | ~8 |
| 4 | Area maps of each floor, the region views with the ring on the mountain, the labelled reference | ~10 |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the nine cave scenes |
