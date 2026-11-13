# Route 5 — asset request (Kanto)

Route 5 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**20 of ~31 — batches 1 and 2: the road and its people.** Everything here is staged for review; nothing is installed.

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

### Batch 2 — the people (10)

Route 5 has no trainers, so none of these people want a battle. They are the route's furniture: the two who look after
Pokémon, the one who won't let you into the city, and seven people simply living on a road between two cities.

| File | Key | Role | Design | Weight |
|---|---|---|---|---|
| `people/daycare-man.jpg` | `daycare-man` | Takes a Pokémon for **₽100, then ₽100 a level** | **Man of seventy**: stooped, bald with white sideburns, round spectacles, pencil behind one ear, brown cardigan, long work apron, carpet slippers, one hand waving | 106 KB |
| `people/daycare-lady.jpg` | `daycare-lady` | His wife; the house, and the tea | **Woman of sixty-eight**: round and bustling, grey bun under a green headscarf, pale blue house dress, white apron, knitted shawl, tea towel over one arm | 139 KB |
| `people/gate-guard.jpg` | `gate-guard` | **Won't open the gate** without the Tea | **Man of forty-two**: solid and square, moustache, slate-blue uniform coat with brass buttons and white piping, white gloves, peaked cap with a **blank** badge, clipboard out, palm raised to refuse | 105 KB |
| `people/tunnel-walker.jpg` | `tunnel-walker` | Uses the Underground Path daily | **Woman of thirty-five**: brisk, dark curly hair pinned up, spectacles pushed back on her head, mustard raincoat, muddy boots, shopping bag, an **unlit** brass lantern held up | 120 KB |
| `people/tunnel-lamplighter.jpg` | `tunnel-lamplighter` | Lights the tunnel lamps | **Man of sixty**: wiry, long white beard tucked into his coat, cloth cap, soot on one cheek, dark green work coat, fingerless gloves, a long brass lighter pole with a live flame | 141 KB |
| `people/route5-jogger.jpg` | `route5-jogger` | Out of breath on the hill | **Man of forty-eight**: soft around the middle, flushed, towel round his neck, hands on his knees, rueful grin, faded red tracksuit top | 139 KB |
| `people/route5-gardener.jpg` | `route5-gardener` | Tends the hedges by the gate | **Man of fifty-five**: weathered, flat cap, green canvas waistcoat with many pockets, striped apron, rubber clogs, hedge shears closed in one hand | 160 KB |
| `people/fence-child.jpg` | `fence-child` | Watches the tall grass and hopes | **Boy of nine**, child proportions: skinny, skinned knees, hair in tufts, oversized jumper with the sleeves over his hands, one sock up and one down, red wellingtons, leaning on his toes | 103 KB |
| `people/route5-courier.jpg` | `route5-courier` | Runs the city deliveries | **Woman of twenty-two**: teal cropped hair under a backwards cycling cap, cropped navy windbreaker, padded shorts, bulky delivery satchel, one hand on her bicycle's handlebars | 189 KB |
| `people/route5-picnicker.jpg` | `route5-picnicker` | Eating lunch in the meadow | **Man of thirty**: broad and cheerful, curly hair and a short beard, lilac shirt, sandals with socks, tartan blanket under one arm and a basket in the other, straw hat pushed back | 134 KB |

**Wiring** — ten `Person(...)` and ten `PORTRAITS` lines at `"kanto-route-5"`:

```python
"daycare-man": "kanto-route-5", "daycare-lady": "kanto-route-5", "gate-guard": "kanto-route-5",
"tunnel-walker": "kanto-route-5", "tunnel-lamplighter": "kanto-route-5", "route5-jogger": "kanto-route-5",
"route5-gardener": "kanto-route-5", "fence-child": "kanto-route-5", "route5-courier": "kanto-route-5",
"route5-picnicker": "kanto-route-5",
```

None of them needs a `Trainer(...)` entry — that is the point of this route. `daycare-man` needs the Day Care service
hook (₽100 to leave, ₽100 a level to collect) and `gate-guard` needs the gate's `requires` gated on the Tea.

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
| 3 | Story beats — the ₽100 deal, collecting a levelled Pokémon, the guard's refusal, the walk down, the tunnel lit — plus **both battle fields, including the missing `kanto-route-5`** | ~7 |
| 4 | Route maps, both region views ringed, the labelled reference | ~5 |

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten route scenes |
| `review/_sheet-batch-2.jpg` | Batch 2 contact sheet — the ten portraits |
