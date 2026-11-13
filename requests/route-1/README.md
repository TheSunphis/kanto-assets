# Route 1 — asset request (Kanto)

Kanto Route 1 for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**26 files staged** — 25 installable assets plus one labelled reference. One scene is still
outstanding (see *Still to come*). Everything here is staged for review; nothing has been
installed into the live asset folders.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | 2 px blocks, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes and battlefields, 160 for maps |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, sprite 726 px, centred at x = 688 |
| Region maps | 1280 × 796 PNG with a gold position ring |
| Content rule | No characters or Pokémon in scenes; dialogue and sprites are drawn by `card.py` at runtime |

---

## Files

### 1. Place scenes — 9

One per building in `BUILDINGS["kanto-route-1"]`, so each stop on the route shows its own ground
instead of all five sharing `town/route-1`.

| File | Shows | Weight | Install to |
|---|---|---|---|
| `town/route-1-south.jpg` | The south entrance where the path leaves Pallet Town | 551 KB | `town/route-1-south.jpg` |
| `town/route-1-middle.jpg` | The roadside Poké Mart stall with its striped awning | 452 KB | `town/route-1-middle.jpg` |
| `town/route-1-bridge.jpg` | The plank footbridge over the stream | 611 KB | `town/route-1-bridge.jpg` |
| `town/route-1-bush.jpg` | The clearing on the far bank, dominated by the big bush | 626 KB | `town/route-1-bush.jpg` |
| `town/route-1-north.jpg` | The climb to Viridian's stone wall and gate | 505 KB | `town/route-1-north.jpg` |
| `town/route-1-ledges.jpg` | The terraced ledge steps west of the path | 545 KB | `town/route-1-ledges.jpg` |
| `town/route-1-fishing.jpg` | The stream bank where the route's fishing happens | 598 KB | `town/route-1-fishing.jpg` |
| `town/route-1-tall-grass.jpg` | The deep encounter grass, path splitting it | 506 KB | `town/route-1-tall-grass.jpg` |
| `town/route-1-gate.jpg` | Arriving at Viridian's wall and gateway | 474 KB | `town/route-1-gate.jpg` |

### 2. Story scenes — 5

Art for the two scripted quest actions in `Quests/Kanto/Route1/side.py`.

| File | Shows | Weight | Install to |
|---|---|---|---|
| `story/route-1-story-clerk.jpg` | The stall counter up close, the sample bottle front and centre | 652 KB | `story/route-1-story-clerk.jpg` |
| `story/route-1-story-bush.jpg` | The big bush with something hidden among the leaves | 600 KB | `story/route-1-story-bush.jpg` |
| `story/route-1-story-hooh.jpg` | A golden feather lying in parted grass — the 1% Ho-Oh slot's find | 512 KB | `story/route-1-story-hooh.jpg` |
| `story/route-1-story-fishing.jpg` | The float dipping, rings spreading on the water | 610 KB | `story/route-1-story-fishing.jpg` |
| `story/route-1-story-signpost.jpg` | Reading the route marker at the Pallet end | 570 KB | `story/route-1-story-signpost.jpg` |

### 3. Route map — 1

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `town/route-1.jpg` | `1584 × 672` | 383 KB | `town/route-1.jpg` |

### 4. `/routeinfo` backdrop — 1

Deliberately calmer in the centre so the encounter table stays readable.

| File | Dimensions | Weight | Install to |
|---|---|---|---|
| `region/route-1.jpg` | `1376 × 768` | 331 KB | `routeinfo/route-1.jpg` |

### 5. `/region` area maps — 4

Marked crops of `town/route-1.jpg`, one per `spawns.ROUTE_AREAS` entry. Consumed by
`_route_map_asset()` once area markers are registered.

| File | Area | Weight | Install to |
|---|---|---|---|
| `town/kanto-route-1-map-south.png` | South Grass | 986 KB | `town/kanto-route-1-map-south.png` |
| `town/kanto-route-1-map-middle.png` | Roadside Stop | 1.1 MB | `town/kanto-route-1-map-middle.png` |
| `town/kanto-route-1-map-bridge.png` | Footbridge & Bush | 1.0 MB | `town/kanto-route-1-map-bridge.png` |
| `town/kanto-route-1-map-north.png` | North Grass | 962 KB | `town/kanto-route-1-map-north.png` |

### 6. Battlefield backgrounds — 4

Keys must exist in `card.FIELDS` with fighter coordinates.

| File | Shows | Weight | Install to |
|---|---|---|---|
| `battle/kanto-route-1.jpg` | Open clearing, rolling hills behind | 262 KB | `battle/bg/kanto-route-1.jpg` |
| `battle/kanto-route-1-north.jpg` | The Viridian gate on the skyline | 268 KB | `battle/bg/kanto-route-1-north.jpg` |
| `battle/kanto-route-1-south.jpg` | Pallet's rooftops and the low fence behind | 238 KB | `battle/bg/kanto-route-1-south.jpg` |
| `battle/kanto-route-1-bridge.jpg` | The footbridge over the stream | 256 KB | `battle/bg/kanto-route-1-bridge.jpg` |

`kanto-route-1` is **already registered** in `card.FIELDS`, so that file is expected today and
currently 404s.

### 7. Portrait — 1

| File | Character | Weight | Install to |
|---|---|---|---|
| `people/route1-clerk.jpg` | Poké Mart Employee (`route1-clerk`) | 121 KB | `people/route1-clerk.jpg` |

### Reference (not installable)

| File | Purpose |
|---|---|
| `review/_route-1-labeled-reference.jpg` | The route map with all six locations numbered and named, for orientation only |

---

## Still to come

- `town/route-1-signpost.jpg` — the route marker scene at the Pallet end. The generation failed and
  the ten-image budget for that batch was already spent; everything else from that batch landed.
- A Kanto overview with Route 1 ringed. The previous region set was removed from this repo in
  `c92f24c`, so there is no base map to crop from at the moment.

---

## Code changes these assets expect

```python
# people.py — give each Route 1 building its own scene instead of the shared town/route-1
Building("r1",       "South Grass",     "kanto/town/route-1-south",  area="route-1-south"),
Building("employee", "Roadside Stop",   "kanto/town/route-1-middle", area="route-1-middle"),
Building("bridge",   "Footbridge",      "kanto/town/route-1-bridge", area="route-1-bridge"),
Building("bush",     "Far-side Bush",   "kanto/town/route-1-bush",   area="route-1-bridge"),
Building("north",    "North Grass",     "kanto/town/route-1-north",  area="route-1-north"),

# people.py — the portrait is ignored until it is registered
PORTRAITS |= {'route1-clerk'}

# card.py — the extra battlefield needs fighter coordinates
FIELDS["kanto-route-1-north"]  = (976, 392, 458, 648)
FIELDS["kanto-route-1-south"]  = (976, 392, 458, 648)
FIELDS["kanto-route-1-bridge"] = (976, 392, 458, 648)

# region.py — area markers so the four region maps are used
markers[ROUTE1] = ({'route-1-south': 'south', 'route-1-middle': 'middle',
                    'route-1-bridge': 'bridge', 'route-1-north': 'north'},
                   'kanto-route-1-map')

# Quests/Kanto/Route1/side.py — the two story scenes need a Quest.picture field
picture="kanto/story/route-1-story-clerk",   # on route1-super-potion
picture="kanto/story/route-1-story-bush",    # on route1-hidden-candy
```

Route 1 has no trainers in `trainers.py`, so there are no trainer portraits or trainer battlefields
in this set — unlike Route 3's eight trainers.
