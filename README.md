# Kanto Assets

Public image repository for PokéBot's Kanto locations and story interactions.

## Repository reset — 13 November 2026

**This repository currently contains no assets.** Every image and every location folder has been removed on
purpose, to rebuild the whole Kanto set from scratch.

| Removed | Count |
|---|---|
| Image files (`.jpg` / `.png`) | **588** |
| Files under `assets/` | 351 |
| Files under `requests/` | 253 |
| Total files removed | 604 |
| Disk freed | ~235 MB |

The previous set is **not lost**. It is intact in git history at commit **`87e8892`** — the last commit before the
reset — and can be read back at any time:

```bash
git show 87e8892:requests/route-6/README.md          # a location's spec and wiring notes
git checkout 87e8892 -- requests/route-6             # restore one location's files
```

That commit holds the finished sets for Route 1, Viridian City, Viridian Forest, Route 2, Route 3, Pewter City,
Mt. Moon, Route 4, Cerulean City, Route 5, Saffron City, Route 6 and Vermilion City, plus every location README,
the `BATTLE_ART.md` field-key table, and the nine Viridian starter variants.

## What comes next

The rebuild runs in journey order, one location at a time, roughly 35 assets each:

`Route 1` → `Viridian City` → `Viridian Forest` → `Route 2` → `Route 3` → `Pewter City` → `Mt. Moon` →
`Route 4` → `Cerulean City` → `Route 5` → `Saffron City` → `Route 6` → `Vermilion City` → onward.

Each location will carry the same shape as the sets it replaces: place scenes, NPC portraits, story beats,
battle backgrounds, route maps, both ringed region views, contact sheets and a README with the wiring it needs.

Fresh work is staged under `requests/<location>/` until it is verified, then installed.

## Layout

The path conventions the bot expects are documented in [`ASSET_LAYOUT.md`](ASSET_LAYOUT.md).

Scene images are backgrounds and art only: dialogue, quest text, buttons and UI are rendered by code.
