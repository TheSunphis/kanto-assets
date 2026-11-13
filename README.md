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

| Path | Intended use | Status |
|---|---|---|
| `assets/region/kanto-pallet-town.jpg` | Existing `/region` map source | Reworked in place to show Oak’s Corral behind the Lab; original map geography and existing labels preserved |
| `assets/town/ash-home.jpg` | Ash’s Home scene | Used by Ash’s Home; one home location |
| `assets/town/oak-corral.jpg` | Oak’s Corral/Pasture | Used by the Pallet Town scene |
| `assets/town/rival-house.jpg` | Rival’s House scene | Used by the Pallet Town scene |
| `assets/people/delia.jpg` | Delia NPC portrait | Used by Ash’s Home |
| `assets/story/pallet-lab-revisit.jpg` | Oak in the lab on revisits | Used by the Pallet Town scene |
| `assets/story/pallet-starter-choice-4.jpg` | Oak’s lab with four starter options | Used by `/start`; matches current four choices |
| `assets/drafts/town/pallet-home-alternative.jpg` | Earlier home interior alternate | Archive/draft; not a second building |

The public raw asset base URL is `https://raw.githubusercontent.com/TheSunphis/kanto-assets/main/assets`.
