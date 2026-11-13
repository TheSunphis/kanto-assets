# Battle art — location-unique, never shared

**The rule: a battlefield picture belongs to one location. No location borrows another's.**

That means battle art lives with its location, not in a shared pool:

```
assets/<location>/battle/bg/<field-key>.jpg   e.g. assets/viridian-forest/battle/bg/kanto-viridian-forest.jpg
```

`card.py` looks a picture up by **field key** — `FIELDS` in `bot/card.py` holds the sprite-anchor coordinates and the key doubles as the file name. So the file name must be the field key, exactly.

---

## Where the repo stands

`49b2987` ("Keep region and battle artwork in shared assets") deleted the per-location `battle/` folders. Under this rule that was backwards for battles — the deletions to revisit are:

| Deleted in `49b2987` | Field key | Status |
|---|---|---|
| `assets/route-1/battle/kanto-route-1.jpg` | `kanto-route-1` | art still exists in `requests/route-1/battle/` — 5 variants (base, south, middle, north, bridge) |
| `assets/route-2/battle/kanto-route-2-and-viridian-forest.jpg` | `kanto-route-2-and-viridian-forest` | art still exists in `requests/route-2/battle/bg/` — also a `-north` variant |
| `assets/pewter-city/battle/pewter-gym.jpg` | `pewter-gym` | **gone — no art anywhere** |
| `assets/cerulean-city/battle/cerulean-gym.jpg` | `cerulean-gym` | **gone — no art anywhere** |
| `assets/cerulean-city/battle/nugget-bridge.jpg` | `nugget-bridge` | **gone — no art anywhere** |
| `assets/route-5/battle/kanto-route-5.jpg` | `kanto-route-5` | **gone — no art anywhere** |
| `assets/region/kanto-map.jpg` | — (region art, not battle) | separate question, shared-ness there is fine |

## Coverage of every field key in `card.FIELDS`

| Field key | Used by | Art in `requests/` | Anchor `(far x, far y, near x, near y)` | Scale |
|---|---|---|---|---|
| `kanto-route-1` | Route 1 | ✅ `route-1/battle/` × 5 | `987, 336, 392, 654` | 0.75 |
| `kanto-route-2-and-viridian-forest` | Route 2 road | ✅ `route-2/battle/bg/` × 2 | `987, 336, 392, 654` | 0.75 |
| `kanto-route-3-mt-moon-and-route-4` | Route 3 | ✅ `route-3/battle/bg/` × 3 | `976, 392, 458, 648` | 1.0 |
| `kanto-viridian-forest` | **not in `FIELDS` yet** | ✅ `viridian-forest/battle/bg/` × 1 | — needs an entry | — |
| `kanto-viridian-gym` | **not in `FIELDS` yet** | ✅ `viridian-city/battle/` × 1 | — needs an entry | — |
| `grass` | fallback when a place has no field | ❌ | `976, 392, 458, 648` | 1.0 |
| `pewter-gym` | Pewter Gym (Camper Liam, Brock) | ❌ | `976, 392, 458, 648` | 1.0 |
| `cerulean-gym` | Cerulean Gym (Swimmer Luis, Picnicker Diana, Misty) | ❌ | `976, 392, 458, 648` | 1.0 |
| `nugget-bridge` | Nugget Bridge (6 trainers) | ❌ | `976, 375, 430, 625` | 1.0 |
| `kanto-route-5` | Route 5 | ❌ | `976, 380, 480, 640` | 1.0 |

So four field keys have no art at all, and two of the battlefields we have have no `FIELDS` entry to be drawn with.

---

## What each battle picture has to respect

The anchors are where the sprites stand, so the art must leave those two zones clear:

- **far** Pokémon stands at `(987, 336)` on a `1376 × 768` picture
- **near** Pokémon stands at `(392, 654)`

Keep both areas free of foreground clutter — tall grass, logs, bushes. Scenery belongs in the mid-ground and at the edges. `grass`, `kanto-route-1` and `kanto-route-2-and-viridian-forest` are drawn at `FIELD_SCALE` **0.75** because their scenery is small; the rest are 1.0.

Style is the same as every other set: GBA 32-bit pixel art, Fire Ash / FireRed tileset, hard pixel edges, 2 px grid, no anti-aliasing, ~64 colours, no creatures and no people in frame.
