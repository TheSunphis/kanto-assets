# Vermilion City — asset request (Kanto)

Vermilion City for PokéBot, in the **Pokémon Fire Ash** (GBA FireRed tileset) style.

**10 of ~40 — batch 1: the city.** Everything here is staged for review; nothing is installed.

---

## Style & spec

| Property | Value |
|---|---|
| Style | Game Boy Advance 32-bit, FireRed / Fire Ash tileset, top-down overworld |
| Pixel grid | Hard pixel edges, no anti-aliasing, no gradients |
| Palette | 64 colours for scenes, 48 for portraits |
| Scenes | 1408 × 768 JPEG q95 — fitted to `card.town()`'s 1280 × 796 field, sides cropped |
| Portraits | 1376 × 768 JPEG q95, cream `(244,245,227)`, single figure 726 px, bottom-flush |
| Content rule | **Places** carry no people and no Pokémon. **Story** beats may and should contain people |
| No text | No signage, no shop names, no prices, no lettering of any kind — `card.py` draws the plate |

### The design thesis

Each Kanto set so far has been built on one material. Pewter is stone. Cerulean is water. Saffron is height and
walls. **Vermilion is iron over salt water**: corrugated sheds, cranes, rope, brass lamps, navy roofs, and paint
that has been repainted badly over rust. It is a working port, not a resort.

---

## Where Vermilion sits in the bot

Vermilion is **almost entirely unwired** — one line in `world.py` and nothing else:

```python
"vermilion-city": ("Vermilion City", "A busy harbour city where ships come and go.", 6, 5, "left"),
```

| Missing | Detail |
|---|---|
| `BUILDINGS["vermilion-city"]` | no entry at all — the city has no buildings to walk into |
| `PEOPLE` | nothing located there; no portraits, no trainers |
| `card.FIELDS` | no Vermilion field — no gym, no harbour battle |
| `spawns.py` | no hunting area |
| `assets/vermilion-city/` | only `region/kanto-vermilion-city.jpg` and `region/kanto-map-vermilion-city.jpg` |

It is on two roads already — `("saffron-city", "vermilion-city", "Route 6", [])` and
`("vermilion-city", "lavender-town", "Routes 11 and 12", [(8, 5)])` — and it is `SEVII_PORT`, the harbour the
ferry to the Sevii Islands leaves from and returns to. That makes the docks the one building in Kanto with a job
beyond scenery.

### Proposed buildings

| Key | Name | Scene | Blurb | People |
|---|---|---|---|---|
| `pc` | Pokémon Center | `town/vermilion-center` | A whitewashed Center under a navy roof, awnings over the doors. | nurse |
| `pm` | Poké Mart | `town/vermilion-mart` | The Mart's awning snaps in the wind off the water. | clerk |
| `gy` | Vermilion Gym | `town/vermilion-gym` | An old brick warehouse with a bolt painted over the door. | Lt. Surge, gym guide |
| `hb` | Vermilion Harbour | `town/vermilion-harbour` | The ferry to the Sevii Islands loads at the far pier. | harbour master, sailor |
| `fc` | Pokémon Fan Club | `town/vermilion-fan-club` | A comfortable house where people talk about their favourites. | chairman, member |
| `fg` | Fishing Guru's House | `town/vermilion-fishing-guru` | Rods lean against a tar-paper shack by the channel. | the guru |
| `lh` | The Lighthouse | `town/vermilion-lighthouse` | A red-banded tower at the end of the breakwater. | keeper |
| `mk` | Fish Market | `town/vermilion-market` | Four stalls, crushed ice, brass scales. | fishmonger |
| `wh` | Warehouse Row | `town/vermilion-warehouses` | Corrugated sheds, loading bays, a hand hoist. | dock worker |
| `sq` | Harbour Square | `town/vermilion-square` | An old anchor on a plinth, a bandstand, benches facing the water. | — |

---

## Files — batch 1: place scenes (10)

| File | Key | Weight |
|---|---|---|
| `town/vermilion-center.jpg` | `pc` | 509 KB |
| `town/vermilion-mart.jpg` | `pm` | 585 KB |
| `town/vermilion-gym.jpg` | `gy` | 544 KB |
| `town/vermilion-harbour.jpg` | `hb` | 488 KB |
| `town/vermilion-fan-club.jpg` | `fc` | 727 KB |
| `town/vermilion-fishing-guru.jpg` | `fg` | 454 KB |
| `town/vermilion-lighthouse.jpg` | `lh` | 515 KB |
| `town/vermilion-market.jpg` | `mk` | 607 KB |
| `town/vermilion-warehouses.jpg` | `wh` | 595 KB |
| `town/vermilion-square.jpg` | `sq` | 603 KB |

Notes on three of them:

- **`vermilion-gym`** is a converted brick warehouse, not a stadium — canon puts Lt. Surge's Gym behind a rolling
  steel door with a bolt on the wall. The bolt is an angular shape only; no letters anywhere.
- **`vermilion-harbour`** carries the liner, the crane and the lighthouse in one frame, because `SEVII_PORT` means
  this is where a player leaves Kanto entirely.
- **`vermilion-market`** is deliberately the busiest composition in the set — the one scene where the emptiness is
  doing work rather than just obeying the rule.

---

## Still to come

| Batch | Contents | Count |
|---|---|---|
| 2 | Portraits — Lt. Surge, the nurse, the clerk, the Fan Club chairman and member, the Fishing Guru, a sailor, the harbour master, a dock worker, the lighthouse keeper | ~10 |
| 3 | Story beats — the ferry at dawn, the parked bike, the gym door, the Fan Club's favourite — plus `vermilion-gym` and harbour battle fields | ~8 |
| 4 | Area maps of the quays and the city, both region views ringed, the labelled reference | ~10 |

**One cross-set note:** the `fan-club-chairman` portrait already staged in
[`requests/saffron-city/`](../saffron-city/) is canonically a **Vermilion** character — the Pokémon Fan Club is
here, not in Saffron. Batch 2 draws the chairman for this set properly. The Saffron file can be dropped, or kept as
a second face for a Saffron club, but it should not ship as Saffron's only chairman.

---

## Review

| File | What |
|---|---|
| `review/_sheet-batch-1.jpg` | Batch 1 contact sheet — the ten city scenes |
