# Kanto region — accurate layout, painted art

23 pictures: the region overview, one overview per town with that town ringed in red, and one
close-up map for every town. Same filenames and sizes the bot asks for, so they drop straight into
`assets/region/`.

This replaces the two earlier attempts in this folder. Both were rejected for the same reason and
this set answers it: **the geography is no longer drawn by an image model**. Every coastline, road,
building, cave and bridge is placed by code from the coordinates the game itself uses
(`bot/world.py` → `KANTO_TOWNS`, `KANTO_ROUTES`); the *art* is painted — a library of AI-painted
GBA sprites and seamless terrain textures, composited onto that skeleton. Nothing can be misplaced,
because placement is arithmetic.

## The thirteen things that were wrong last time, and where each one now is

| Was wrong | Now |
| --- | --- |
| Celadon, Saffron and Vermilion merged into one megacity | Three separate towns: Celadon west at (4,3), Saffron landlocked centre at (6,3), Vermilion a coastal port at (6,5) with its own harbour wall, pier and moored ferry |
| Cycling Road ran south through the megacity into Fuchsia | Cycling Road leaves Celadon west, turns south down the bay's west shore on its concrete spans, and crosses to Fuchsia — never through a city |
| Fuchsia on an island, cut off from the mainland | Fuchsia is part of the mainland; only the bay separates it from the west |
| Safari Zone east of Fuchsia | Safari Zone is the fenced reserve directly **north** of Fuchsia, with gate, ponds and trees |
| Diglett's Cave wedged between city blocks | Two tunnel mouths: one on Route 2 north-west of Viridian, one east of Vermilion on Route 11 — the real pair |
| Underground Path inside Viridian | Both pairs of huts where they belong: on Route 5 south of Saffron and on Route 7 west of it |
| Silence Bridge pointing into empty ocean | Silence Bridge spans the inlet on Route 12, directly south of Lavender on the east coast |
| Rock Tunnel opening into the Power Plant | Rock Tunnel is bored through the cliff ridge on Routes 9/10; the Power Plant stands beside it, reached by surfing the river there |
| Nugget Bridge on a path going east, Sea Cottage on a random dock | Nugget Bridge crosses the Cerulean river north of the city, then the cape road runs east to Bill's Sea Cottage |
| Cerulean Cave on a random lake south of the city | Cerulean Cave is the cave mouth north-west of Cerulean, across the water |
| Mt. Silver and Tohjo Falls labelled as Kanto | No Johto labels at all. One landmark only: Tohjo Falls, where Routes 26/27 visibly leave the map west |
| A north-south train track beside Saffron | No rail line. The Magnet Train has no visible track on this map |
| Pokémon Tower as a lighthouse, empty Safari Zone | Lavender's tower stands inside the town; the Safari Zone has its gate, two ponds and scattered trees |

Everything else the bot knows is present and correct: Route 1 Pallet→Viridian, Route 2 through
Viridian Forest, Routes 3/4 through Mt. Moon, Route 5, 6, 7 and 8 radiating from Saffron, Routes
9/10 via Rock Tunnel, Routes 11/12, Routes 12–15 down the east coast, Routes 16–18 over the Cycling
Road, Routes 19/20 as a sea lane west past the Seafoam Islands, Route 21 north from Cinnabar to
Pallet, Routes 22/23 up to Indigo Plateau through Victory Road, Routes 24/25 to Sea Cottage, and
Routes 26/27/28 leaving west.

## How it is built

`build_map.py` (layout + compositing) and `label_map.py` (lettering), both Python, both driven by
`bot/world.py`:

- **Land** is a hand-traced polygon of Kanto's real silhouette, with the central bay and Vermilion's
  harbour cut into it, a western landmass for the Johto road, Cinnabar's island and the Seafoam
  islets offshore.
- **Terrain** is seamless AI-painted grass, ocean, sand and rock, masked by that shape, with a sand
  fringe and shallow-water band on every coast.
- **Towns** are clusters of AI-painted GBA buildings (house, Pokémon Center, Poké Mart, Gym, museum,
  department store, corporate tower, stone tower, laboratory, mansion) on paved ground.
- **Landmarks** are AI-painted sprites: cave mouths, mountain ridges, plank bridges, the concrete
  span, the stone pier, the ferry, the volcano, the waterfall.
- **Ground cover** — pines, bushes, boulders, tall grass and flowers — is scattered along every land
  route, so the countryside reads like Kanto rather than a lawn.
- **Lettering** is Jersey15 (the bot's own font) on ink plates, placed from the same coordinates as
  the towns, so a label can only sit on the thing it names.

## Files (23)

Overview — 1536 wide:

| File | Shows |
| --- | --- |
| `kanto-map.jpg` | all of Kanto, every town and landmark named |
| `kanto-map-pallet-town.jpg` | …with Pallet Town ringed |
| `kanto-map-viridian-city.jpg` | …with Viridian City ringed |
| `kanto-map-pewter-city.jpg` | …with Pewter City ringed |
| `kanto-map-cerulean-city.jpg` | …with Cerulean City ringed |
| `kanto-map-vermilion-city.jpg` | …with Vermilion City ringed |
| `kanto-map-lavender-town.jpg` | …with Lavender Town ringed |
| `kanto-map-celadon-city.jpg` | …with Celadon City ringed |
| `kanto-map-saffron-city.jpg` | …with Saffron City ringed |
| `kanto-map-fuchsia-city.jpg` | …with Fuchsia City ringed |
| `kanto-map-cinnabar-island.jpg` | …with Cinnabar Island ringed |
| `kanto-map-indigo-plateau.jpg` | …with Indigo Plateau ringed |

Close-up per town — 1280×940:

| File | Shows |
| --- | --- |
| `kanto-pallet-town.jpg` | Pallet on its cape: two houses, the lab, Route 1 north, Route 21 sea lane south |
| `kanto-viridian-city.jpg` | Viridian: Center, Mart, Gym, Trainers' School, the road west to the League |
| `kanto-pewter-city.jpg` | Pewter: museum, Gym, Diglett's Cave mouth, the Mt. Moon wall east |
| `kanto-cerulean-city.jpg` | Cerulean: Gym, river, bridges, Nugget Bridge and the cape road north |
| `kanto-vermilion-city.jpg` | Vermilion: harbour, pier, ferry, Diglett's Cave, Silence Bridge east |
| `kanto-lavender-town.jpg` | Lavender: Pokémon Tower, the Route 12 coast south, the inlet |
| `kanto-celadon-city.jpg` | Celadon: department store, Game Corner block, mansion, Route 7 and the bay south-west |
| `kanto-saffron-city.jpg` | Saffron: Silph tower, Gym, Underground Paths on Routes 5 and 7 |
| `kanto-fuchsia-city.jpg` | Fuchsia: town, Safari Zone north, Routes 15 and 19 |
| `kanto-cinnabar-island.jpg` | Cinnabar: volcano, mansion, lab, harbour, Route 21 north |
| `kanto-indigo-plateau.jpg` | Indigo Plateau: the League on its shelf, Victory Road below |

Review sheets, not for shipping: `review/before-after.jpg`, `review/town-windows.jpg`,
`review/labels-and-routes.jpg` (overview with route numbers 1–28).

## Wiring

Only Pallet Town's map is fetched from this repo today
(`bot/plugins/region.py` → `kanto_asset("region", "kanto-pallet-town.jpg")` → `assets/region/`);
the other ten still come from the legacy Pika host. To go live: copy these 23 files into
`assets/region/`, and point `_map_asset` plus the two overview name-builders at `kanto_asset`.

Until then these pictures live only under `requests/`, where the bot cannot see them.
