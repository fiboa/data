
# fiboa Datasets

This repository provides you with all information about existing fiboa datasets.

## List of datasets

| Title | License | Provider |
| ----- | ------- | -------- |
| [Austria](https://beta.source.coop/repositories/fiboa/austria/description/) | CC-BY-4.0 | Agrarmarkt Austria |
| [BRP Crop Field Boundaries for The Netherlands (CAP-based)](https://beta.source.coop/repositories/fiboa/nl-crop/description/) | CC0-1.0 |  |
| [Field boundaries for Cambodia and Vietnam (AI4SmallFarms)](https://beta.source.coop/repositories/fiboa/ai4sf/description/) | CC-BY-4.0 |  |
| [Field boundaries for Flanders, Belgium](https://beta.source.coop/repositories/fiboa/be-vlg/description/) | Licentie modellicentie-gratis-hergebruik/v1.0 |  |
| [Field boundaries for France from Eurocrops (2018)](https://beta.source.coop/repositories/fiboa/france-ec/description/) | CC-BY-SA-4.0 | Institut National de l'Information Géographique et Forestière |
| [Field boundaries for Latvia from EuroCrops (2021)](https://beta.source.coop/repositories/fiboa/ec-lv/description/) | CC-BY-4.0 | Lauku atbalsta dienests |
| [Field boundaries for Portugal](https://beta.source.coop/repositories/fiboa/portugal/description/) | No conditions apply |  |
| [Field boundaries for Slovenia from EuroCrops (2021)](https://beta.source.coop/repositories/fiboa/slovenia-ec/description/) | CC-BY-SA-4.0 | Ministrstvo za kmetijstvo, gozdarstvo in prehrano |
| [Field boundaries for The Netherlands](https://beta.source.coop/repositories/fiboa/nl-ref/description/) | CC0-1.0 |  |
| [Field boundaries for the west of Bahia state, Brazil](https://beta.source.coop/repositories/fiboa/br-ba-lem/description/) | CC-BY-4.0 |  |
| [Finnish Crop Fields (Maatalousmaa)](https://beta.source.coop/repositories/fiboa/finland/description/) | CC-BY-4.0 | Finnish Food Authority |
| [Germany, Berlin / Brandenburg](https://beta.source.coop/repositories/fiboa/de-bb/description/) | dl-de/by-2-0 | Land Brandenburg |
| [Germany, Lower Saxony](https://beta.source.coop/repositories/fiboa/de-nds/description/) | dl-de/by-2-0 | Land Niedersachsen |
| [Germany, North Rhine-Westphalia](https://beta.source.coop/repositories/fiboa/de-nrw/description/) | dl-de/by-2-0 | Land Nordrhein-Westfalen / Open.NRW |
| [Germany, Schleswig-Holstein](https://beta.source.coop/repositories/fiboa/de-sh/description/) | dl-de/zero-2-0 | Land Schleswig-Holstein |
| [Germany, Thuringia](https://beta.source.coop/repositories/fiboa/de-th/description/) | dl-de/by-2-0 | Thüringer Landesamt für Landwirtschaft und Ländlichen Raum |
| [UKFields](https://zenodo.org/records/11110206) | CC-BY-4.0 | Bancroft S, Wilkins J |

* **Last updated:** Sep 06 2024, 01:16 
* **Count:** 17

## Add your dataset

If you want, follow the [How To](HOWTO.md) to create a new dataset using fiboa CLI.

Once your dataset is ready, you have two options to add your dataset:
1. If it has a STAC Collection for it, edit [this file](https://github.com/fiboa/fiboa.github.io/edit/main/stac/catalog.json), add your Collection as a child to the STAC catalog, and lastly create a PR.
2. In all other cases, edit [this file](https://github.com/fiboa/data/edit/main/README.md.jinja), add your dataset to the table (after the `endfor %}`), and lastly create a PR.

Once the PR is merged your data will be listed here shortly after (it's updated every night).