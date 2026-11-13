# Route 5 — asset request (Kanto)

Route 5 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 of ~31 — batch 1: the road.** Everything here is staged for review; nothing is installed.

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

### What Route 5 is

The odd one out among Kanto's routes: **there are no trainers on it at all.** It is the safe walk between the
riverside city and the great walled one, and everything on it is either a building you go into or a thing you
can't pass — the Day Care, the Saffron gate that stays shut without the Tea, and the stairs down to the
Underground Path. A route with no battles has to be interesting as a *place*, so this set leans on the fences,
the meadow, the water and the one orange roof you can see from the top of the hill.

---

## Where Route 5 sits in the bot

```python
Building("r5", "Route 5", "town/route-5",
         "A road running downhill to Saffron City. A little day-care house stands beside it.",
         people=(), area="")
```

No people, no trainers — which is correct for canon. Two things are missing that this set addresses:

| Gap | Detail |
|---|---|
| **No Day Care building** | the blurb *mentions* a day-care house but there is no way to walk into one. Canon has a man inside who takes ₽100 and ₽100 a level |
| **The field key is empty** | `card.FIELDS["kanto-route-5"]` exists at `(976, 380, 480, 640)` but there is **no file behind it** — the only route in Kanto with a field key and no art. Anything that fights here has nothing to show |

The Saffron gate and the Underground Path 5-6 stairway don't exist in the bot at all, though Route 5 is the only
way to reach either.

### Proposed buildings

| Key | Name | Scene | Blurb |
|---|---|---|---|
| `r5` | Route 5 | `town/route-5` | A road running downhill to Saffron City. A little day-care house stands beside it. *(existing key)* |
| `dc` | Day Care | `town/route-5-daycare` | A snug house with an orange roof. Somebody inside will look after a Pokémon for a price. |
| `gt` | Saffron Gate | `town/route-5-gate` | The gatehouse into the walled city. The guard is not letting anyone through today. |
| `gi` | Gate Passage | `town/route-5-gate-inside` | A vaulted stone passage with a bench and a board nobody has written on. |
| `ug` | Underground Path | `town/route-5-underground` | Stairs going down into the dark, and a long walk under the city to Route 6. |
| `ld` | The Ledges | `town/route-5-ledges` | Three long shelves of stone stepping down the hill. Easy going south. |
| `gf` | The Fenced Meadow | `town/route-5-grass` | A square of tall grass inside a white fence. Something is always moving in there. |
| `nd` | North End | `town/route-5-north-end` | The route becomes a street, and the street becomes the city. |
| `br` | The Stream | `town/route-5-stream` | Clear water over pebbles, a hump-backed bridge, and a willow in the way. |
| `vb` | The Climb Back | `town/route-5-view-back` | Looking up the hill from the bottom: ledges, fences, one orange roof, and the city on the skyline. |

---

## Files — batch 1: place scenes (10)

| File | Key | Shows | Weight |
|---|---|---|---|
| `town/route-5.jpg` | `r5` | The road running downhill between white fences and green meadows toward the walled city's gatehouse tower | 358 KB |
| `town/route-5-daycare.jpg` | `dc` | The Day Care: orange tiled roof, cream walls, green shutters, a picket-fenced garden with a clothesline and a vegetable patch, a bench and a milk churn | 652 KB |
| `town/route-5-gate.jpg` | `gt` | The gatehouse: pale stone, a wide arch with the portcullis raised, ivy on one corner, walls running away along the hedges | 607 KB |
| `town/route-5-gate-inside.jpg` | `gi` | Inside the gate: a vaulted stone passage, hard daylight from two windows, a bench, a table with a clipboard and a blank notice board | 524 KB |
| `town/route-5-underground.jpg` | `ug` | The tunnel stair: brick parapets, an iron handrail, a bracket lamp, and the last daylight on the top three steps | 704 KB |
| `town/route-5-ledges.jpg` | `ld` | Three long stone ledges stepping down a green hill, grass fringing every lip, paved walkways along the top two | 504 KB |
| `town/route-5-grass.jpg` | `gf` | The fenced meadow: deep tall grass inside white post-and-rail, a trodden path winding in, a gap on the south side | 673 KB |
| `town/route-5-north-end.jpg` | `nd` | The route becoming a city street: blue and green tiled roofs, a striped shop awning, a blank milestone, a bridge arching over teal water beyond | 646 KB |
| `town/route-5-stream.jpg` | `br` | The stream: teal water over pebbles, a hump bridge, stepping stones, reeds, and a willow trailing branches | 878 KB |
| `town/route-5-view-back.jpg` | `vb` | The climb seen from the bottom in late gold: fences, ledges, one orange roof on the slope, the city on the skyline | 891 KB |

---

## Still to come

| Batch | Contents | Count |
|---|---|---|
| 2 | Portraits — the Day Care man, his wife, the gate guard, a tunnel walker, a picnicker, a jogger, a gardener, a child at the fence | ~8 |
| 3 | Story beats — the ₽100 deal, collecting a levelled Pokémon, the guard's refusal, the Tea, the walk down — plus **both battle fields, including the missing `kanto-route-5`** | ~7 |
| 4 | Route maps, both region views ringed, the labelled reference | ~6 |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten route scenes |
