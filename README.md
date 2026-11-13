# Kanto Assets

Public image repository for PokéBot’s Kanto locations and story interactions.

## Layout

- `assets/region/` — existing regional map artwork; revise the source map in place and preserve route geography.
- `assets/town/` — reusable building and location scenes.
- `assets/people/` — individual NPC portraits.
- `assets/story/` — story-state scenes (starter choice, lab revisit, handoffs).
- `assets/drafts/` — alternates not yet selected for active use.

Scene images are backgrounds/art only: dialogue, quest text, buttons, and UI are rendered by code. Region maps retain their cartographic labels and location markers. The Pallet Town story uses Fire Ash-inspired locations and NPCs while keeping the bot’s four starter choices and an open-world progression.

## Current Pallet Town inventory

The 13-image set staged under `requests/pallet-town/` is installed in `assets/`; the request folder was removed after verification. The active images use the FireRed / Fire Ash pixel-art style and are wired into `/region`, Pallet Town buildings, NPC portraits, `/start`, and quest epilogues.

| Path | Intended use |
|---|---|
| `assets/region/kanto-pallet-town.jpg` | Pallet Town overview/map |
| `assets/town/ash-home.jpg` | Ash’s Home and the home-rest scene |
| `assets/town/oak-corral.jpg` | Oak’s Corral |
| `assets/town/rival-house.jpg` | Rival’s House |
| `assets/town/outside-lab.jpg` | Distinct scene outside Oak’s Lab |
| `assets/story/pallet-lab-revisit.jpg` | Oak’s Lab on revisits |
| `assets/story/pallet-starter-choice-4.jpg` | `/start` four-starter choice |
| `assets/story/pallet-oak-corral.jpg` | Oak’s Corral quest-completion scene |
| `assets/story/pallet-rival-training.jpg` | Gary’s training-quest thank-you scene |
| `assets/people/delia.jpg` | Delia portrait |
| `assets/people/professor-oak.jpg` | Professor Oak portrait |
| `assets/people/gary.jpg` | Gary portrait |
| `assets/people/daisy.jpg` | Daisy portrait |
| `assets/drafts/town/pallet-home-alternative.jpg` | Earlier home-interior alternate; archived, not used as a second building |

The public raw asset base URL is `https://raw.githubusercontent.com/TheSunphis/kanto-assets/main/assets`.
