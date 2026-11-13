# Kanto region — full map set, painted GBA art

The whole Kanto map set as **hand-painted 32-bit GBA regional art**, not procedural geometry:
23 pictures — the region overview, one overview per town with the town marked, and one close-up
map for every town. Same filenames the bot asks for, so they drop into `assets/region/` unchanged.

This replaces the earlier set in this folder, which was drawn by `tools/make_region_images.py`
out of polygons and looked like it. That version is still in the git history if you want to
compare; the review sheet `review/before-after.jpg` puts the two side by side.

## How the set was made

One master painting of the whole region — the full continent, every town, every road, cave, bridge,
forest and island in a single coherent illustration — then everything else derived from it:

- `kanto-map.jpg` — the master with every town and landmark named.
- `kanto-map-<town>.jpg` ×11 — the same master with that town ringed in red.
- `kanto-<town>.jpg` ×11 — a close-up of the master around that town, at 2× zoom (nearest
  neighbour, so the pixels stay square and it matches the rest of the art), framed and titled.

Because every picture comes from one painting, the coastline, roads and landmarks line up exactly
between the overview and the close-ups. Nothing is invented twice and nothing contradicts.

## What's on the map

The layout follows Kanto's real geography, and every place the bot knows is on it:

- **North:** the mountain wall behind Indigo Plateau, with the League's stone plateau on its shelf
  and the long road down through Victory Road.
- **West:** Viridian Forest's pines, Viridian City's crossroads, and the Tohjo Falls gorge with the
  road running west toward Johto and Mt. Silver's snow peak beyond it.
- **North-centre:** Pewter City and its domed museum under the Mt. Moon range, with cave mouths,
  fallen boulders and the grassy road east.
- **North-east:** Cerulean City's rivers, bridges and three lakes, Nugget Bridge, Sea Cottage on its
  cape, Cerulean Cave, and the Power Plant on the far coast.
- **East:** Rock Tunnel bored through the cliff ridge, and Lavender Town with its stone tower.
- **Centre:** Celadon's department store, Game Corner and mansion, and Saffron's Silph skyscraper,
  Fighting Dojo and railway station, four roads meeting between them.
- **South-east:** Vermilion's harbour wall, pier and moored ferry, Diglett's Cave inland, and the
  Silence Bridge over the coast inlet.
- **South:** Fuchsia City beside the Safari Zone's fenced grasslands.
- **Centre-south:** the great bay, with the Cycling Road bridge on its pilings straight across it.
- **South-west:** Pallet Town alone on its cape, the Route 21 sea lane south to Cinnabar Island's
  volcano, and the Seafoam Islands in between.
- Roads, ledges, tall grass, boulders, flower patches, gatehouses, signposts, lakes, boats and
  beach shallows throughout.

`review/labels-and-routes.jpg` is the same overview with all 28 route numbers added, if you want to
check the road network by number.

## Files (23)

Overview — 1536×1536:

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
| `kanto-pallet-town.jpg` | Pallet Town: the houses and the lab on the cape, beach, Route 1 north |
| `kanto-viridian-city.jpg` | Viridian City: crossroads, forest edge, the road down to Pallet |
| `kanto-pewter-city.jpg` | Pewter City: the museum, the city, the mountain foot |
| `kanto-cerulean-city.jpg` | Cerulean City: rivers, bridges, lakes, the cape road north |
| `kanto-vermilion-city.jpg` | Vermilion City: streets, harbour, pier and the moored ferry |
| `kanto-lavender-town.jpg` | Lavender Town: the stone tower, the cliff coast, the inlet |
| `kanto-celadon-city.jpg` | Celadon City: department store, Game Corner, mansion, parks |
| `kanto-saffron-city.jpg` | Saffron City: Silph tower, dojo, station, the four-way crossing |
| `kanto-fuchsia-city.jpg` | Fuchsia City: the town, the Safari Zone fence, the bay |
| `kanto-cinnabar-island.jpg` | Cinnabar Island: volcano, mansion, harbour, sea lanes |
| `kanto-indigo-plateau.jpg` | Indigo Plateau: the League plateau and Victory Road |

Review sheets, not for shipping:

- `review/before-after.jpg` — the old python-painted map next to this one.
- `review/town-windows.jpg` — all eleven close-ups on one sheet.
- `review/labels-and-routes.jpg` — the overview with route numbers 1–28 added.
- `review/unlabelled-map.jpg` — the master with no labels at all, for reuse.

## Wiring

Same as before: only Pallet Town's map is currently fetched from this repo
(`bot/plugins/region.py` → `kanto_asset("region", "kanto-pallet-town.jpg")`, i.e. `assets/region/`);
the other ten towns still come from the legacy Pika host. To make the whole set live:

1. Copy these 23 files into `assets/region/` of this repo — Pallet Town updates with no code change.
2. Point the rest here too, in `bot/plugins/region.py`:

   ```python
   def _map_asset(region: str, place: str) -> str:
       picture = world.picture_place(place)
       if region == "Kanto":
           return kanto_asset("region", f"kanto-{picture}.jpg")
       return asset("region", f"{world.MAPS[region]['prefix']}-{picture}.jpg")
   ```

   and the same swap where the overview names are built (`kanto-map.jpg` / `kanto-map-<town>.jpg`).

Until step 1 these pictures live only under `requests/`, where the bot cannot see them.
