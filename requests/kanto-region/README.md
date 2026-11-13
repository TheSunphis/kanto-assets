# Kanto region — full map set (repainted, corrected geography)

The whole Kanto map set redrawn: **23 pictures**, one overview, one full-region map per town,
and one close-up window per town. Same filenames, same sizes and same painter as before, so these
files drop straight into `assets/region/` with no code change.

The old map was painted from a six-point hexagon of land with a notch cut out of it. Kanto came out
as a blob floating in the sea, with a gulf that does not exist and towns sitting in the wrong place
relative to the coast. That land shape is the thing this set fixes.

## What changed geographically

`tools/make_region_images.py` holds Kanto's geography as constants. The patch in this folder
(`kanto_geography.patch`) replaces them; the pictures here are what the patched script renders.

| Before | After |
| --- | --- |
| Land was a 6-point hexagon: `(2,1) (8,1) (8,7) (3.2,7) (3.2,4.6) (2,6.2)` | 40-point tracing of Kanto's real silhouette |
| A large fake gulf filled the west, so Viridian's country was sea | The west is land, coasted at the mountains behind Indigo Plateau and Viridian; the sea only reaches Kanto from the south and south-west |
| North edge was a straight line | Mountain wall along the whole north: Victory Road, the Mt. Moon range, the Rock Tunnel crags |
| No central bay | **The bay is back** — the inlet between Viridian's country and Fuchsia, with the Cycling Road running down its west shore and bridging it south of the Safari Zone |
| Vermilion was inland | **Vermilion is a port** — its harbour is cut into the coast, open to the sea, with the pier and the S.S. Anne floating in it |
| Pallet sat on a flat edge | Pallet is on its own little south-west cape, sea to the west, south and east |
| Cinnabar floated alone | Cinnabar is an island off the south coast, reached by the Route 21 sea lane, with the Seafoam Islands sitting in the mouth of the bay to its east |
| Routes 26/27/28 ran out over open water to the map edge | A western landmass carries them off-map toward Johto, over Tohjo Falls, the way the land border really runs |
| Town grass stamps were 300 px and swelled the coast | 215 px for Kanto (`TOWN_R`), so the coastline is the map's shape instead of the towns' |
| Sea route ends left land strips stitched over the water | Islets off the south-east coast, boats riding in the new bay |

Everything else the painter already had is kept and re-seated on the new coast: Viridian Forest,
Mt. Moon and its tunnel mouths, Rock Tunnel, Victory Road, Tohjo Falls, Nugget Bridge, the Silence
Bridge over the east inlet, Diglett's Cave, the Power Plant, the Day Care, Sea Cottage, the Safari
Zone, Vermilion Harbour, Cinnabar's volcano and the Seafoam rocks.

Town positions are untouched — every town stays on the coordinates in `bot/world.py`
(`KANTO_TOWNS`), so route links, markers and the region menu all still line up.

## Files (23)

Region overview and per-town region maps — 1280×963:

| File | Shows |
| --- | --- |
| `kanto-map.jpg` | all of Kanto, every town named, for a trainer who is elsewhere |
| `kanto-map-pallet-town.jpg` | all of Kanto with Pallet Town marked and highlighted |
| `kanto-map-viridian-city.jpg` | …with Viridian City marked |
| `kanto-map-pewter-city.jpg` | …with Pewter City marked |
| `kanto-map-cerulean-city.jpg` | …with Cerulean City marked |
| `kanto-map-vermilion-city.jpg` | …with Vermilion City marked |
| `kanto-map-lavender-town.jpg` | …with Lavender Town marked |
| `kanto-map-celadon-city.jpg` | …with Celadon City marked |
| `kanto-map-saffron-city.jpg` | …with Saffron City marked |
| `kanto-map-fuchsia-city.jpg` | …with Fuchsia City marked |
| `kanto-map-cinnabar-island.jpg` | …with Cinnabar Island marked |
| `kanto-map-indigo-plateau.jpg` | …with Indigo Plateau marked |

Close-up windows — 1280×940, the picture the bot shows when the trainer is standing in the town:

| File | Shows |
| --- | --- |
| `kanto-pallet-town.jpg` | Pallet: Your Home, Rival's House, the Lab, Route 1 north, Route 21 south to Cinnabar |
| `kanto-viridian-city.jpg` | Viridian: Gym, Trainers' School, Route 1, Route 2 north, the Johto road west |
| `kanto-pewter-city.jpg` | Pewter: Museum, Gym, Route 2 south, the Mt. Moon wall east |
| `kanto-cerulean-city.jpg` | Cerulean: Gym, Bike Shop, Nugget Bridge and Route 24 north, Rock Tunnel east |
| `kanto-vermilion-city.jpg` | Vermilion: Gym, Fan Club, the harbour with the pier and the S.S. Anne, Silence Bridge |
| `kanto-lavender-town.jpg` | Lavender: Pokémon Tower, Name Rater, Route 8, the coast south |
| `kanto-celadon-city.jpg` | Celadon: Dept. Store, Game Corner, Mansion, the bay to the south-west |
| `kanto-saffron-city.jpg` | Saffron: Silph Co., Fighting Dojo, Magnet Train station, Route 6 south |
| `kanto-fuchsia-city.jpg` | Fuchsia: Gym, Warden's House, the Safari Zone, the bay to the west |
| `kanto-cinnabar-island.jpg` | Cinnabar: Mansion, Gym, Research Lab, Lab, the volcano, Route 21 north |
| `kanto-indigo-plateau.jpg` | Indigo Plateau: Pokémon League, Victory Road, the road down to Viridian |

Review sheets, not for shipping:

- `review/before-after.jpg` — the old hexagon map next to this one.
- `review/town-windows.jpg` — all eleven town windows on one sheet.

## Regenerating them

The set is drawn, not hand-painted. Apply the patch, then run the tool for Kanto only:

```bash
cd ~/Pokebot
git apply /path/to/kanto_geography.patch          # swaps the geography constants
./.venv/bin/python tools/make_region_images.py Kanto
```

That writes all 23 files into `assets/region/` in about eight seconds. Always pass `Kanto` —
running the tool with no arguments repaints every region and the nine region boards as well.

`kanto_geography.patch` touches only constants: the coastline `LAND`, the two water cuts (`BAY` for
Vermilion Harbour, `BAY_E` for the central bay), the western landmass in `MORE_LAND`, `TOWN_R` for
Kanto's town stamps, two boats in the bay, and one label ("Pond" in Viridian) that was hiding
behind the Pokémon Center / Poké Mart key.

## Wiring, if you want the game to use them

Only one file here is already live. `bot/plugins/region.py` fetches
`kanto-pallet-town.jpg` from this repo (`kanto_asset("region", …)` → `assets/region/`), and every
other town still comes from the legacy Pika host (`asset("region", "kanto-<town>.jpg")`). So:

1. **Copy the 23 files into `assets/region/`** of this repo — that is the folder
   `KANTO_ASSETS_URL` points at, and it is exactly where the tool writes them. Pallet Town's map
   then updates with no code change at all.
2. **Point the other ten towns here too**, in `bot/plugins/region.py`:

   ```python
   def _map_asset(region: str, place: str) -> str:
       picture = world.picture_place(place)
       if region == "Kanto":
           return kanto_asset("region", f"kanto-{picture}.jpg")
       return asset("region", f"{world.MAPS[region]['prefix']}-{picture}.jpg")
   ```

   and the same swap for the whole-region board (`kanto-map.jpg` / `kanto-map-<town>.jpg`) at the
   two places that build those names further down the file.

Until step 1 is done these pictures live only under `requests/`, where the bot cannot see them.
