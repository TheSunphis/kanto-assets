# Pallet Town — extra scenes (3)

The three images missing from the Pallet Town set in `requests/pallet-town/`. That set covered every
file the bot actually fetches; these close the gaps against the fuller standard used for Route 3.

Style and spec match the rest of the Kanto work: **Game Boy Advance 32-bit, Fire Ash / FireRed
tileset, top-down overworld**, 2 px pixel grid, no anti-aliasing, no gradients, 64-colour palette,
JPEG q95, 1408 × 768 (fitted to `card.town()`'s 1280 × 796 field, sides cropped by the card).
No characters and no Pokémon in any scene — `card.py` draws dialogue and sprites at runtime.

---

## Files

| File | Shows | Weight | Install to |
|---|---|---|---|
| `outside-lab.jpg` | The front of Oak's Lab: red tiled roof, two skylights, glass entrance on stone steps, hedges, picket fence, mailboxes, bike rack, the windmill at the right edge | 363 KB | `town/outside-lab.jpg` |
| `pallet-oak-corral.jpg` | The corral behind the lab: post-and-rail fence with gate, hay bales, water trough, lean-to shelter, worn tracks in the paddock | 433 KB | `story/pallet-oak-corral.jpg` |
| `pallet-rival-training.jpg` | The training clearing north of town: scuffed dirt, chalked circle, roped post, practice dummy, stacked crates, open bag | 366 KB | `story/pallet-rival-training.jpg` |

All three are 1408 × 768, JPEG q95.

---

## Wiring

### `outside-lab` — ready to use, one line

The building currently borrows the whole-town region map, so walking outside the lab shows the same
picture as the town overview. In `bot/people.py`:

```python
# BUILDINGS["pallet-town"], the outside-lab entry
Building("outside-lab", "Outside Oak's Lab", "kanto/town/outside-lab", requires=("first-pokemon",)),
```

`_scene_url()` in `bot/plugins/town.py` resolves `kanto/town/outside-lab` to
`kanto_asset("town", "outside-lab.jpg")`, so no other change is needed.

### The two story scenes — art only, no consumer yet

`help-oak-corral` and `rival-training` are quest *actions*. Both fire inside buildings that already
have their own scenes (Oak's Corral, Rival's House), and `Quest` in `bot/quests/model.py` has no
image field — epilogues render as text over the building's scene. These two files do nothing until
that changes:

```python
# bot/quests/model.py — Quest dataclass
picture: str = ""          # optional kanto/story scene drawn with the epilogue

# bot/plugins/town.py — where the epilogue card is redrawn
if quest.picture:
    scene = _scene_url(quest.picture)

# Quests/Kanto/PalletTown/side.py
picture="kanto/story/pallet-oak-corral",     # on oak-corral-check
picture="kanto/story/pallet-rival-training", # on rival-training
```

---

## Also still unwired from the original Pallet set

`gary.jpg`, `daisy.jpg` and `professor-oak.jpg` exist in `requests/pallet-town/people/` but are not
in `KANTO_PORTRAITS`, so `scene_of()` ignores them and the bot never requests those files:

```python
KANTO_PORTRAITS |= {'professor-oak', 'gary', 'daisy'}   # delia is already registered
```
