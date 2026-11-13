# Kanto asset layout

Kanto-specific runtime art is organized as `assets/<location>/<category>/<file>`. Location folders include Pallet Town, Routes 1, 2, 3, 4 and 5, Viridian City, Viridian Forest, Pewter City, Cerulean City, Sea Cottage, Mt. Moon, and the remaining Kanto towns.

Categories include `town`, `people`, `battle/bg`, `story`, `region`, `region-maps`, and `routeinfo`. The `region` subfolder contains location overview art; `region-maps` contains area maps. Battlefields are location-specific and live under each location's `battle/bg/`.

New location artwork is sourced from `requests/<location>/` and installed under its matching `assets/<location>/` folder. Do not borrow shared Pika artwork or art from another location. Route 1/2 map attribution is stored in each location's `town/`.
