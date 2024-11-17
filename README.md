
# fiboa Datasets

This repository provides you with all information about existing fiboa datasets.

## List of datasets

| Title | License | Provider |
| ----- | ------- | -------- |
| [Austria](https://source.coop/repositories/fiboa/austria/description/) | CC-BY-4.0 | Agrarmarkt Austria |
| [BRP Crop Field Boundaries for The Netherlands (CAP-based)](https://source.coop/repositories/fiboa/nl-crop/description/) | CC0-1.0 |  |
| [Denmark Crop Fields (Marker)](https://source.coop/repositories/fiboa/denmark/description/) | CC-0 |  |
| [Field boundaries for Belgium Wallonia](https://source.coop/repositories/fiboa/be-wa/description/) | No conditions apply to access and use |  |
| [Field boundaries for Cambodia and Vietnam (AI4SmallFarms)](https://source.coop/repositories/fiboa/ai4sf/description/) | CC-BY-4.0 |  |
| [Field boundaries for Catalonia, Spain](https://source.coop/repositories/fiboa/es-cat/description/) | Open Information Use License - Catalonia |  |
| [Field boundaries for Croatia](https://source.coop/repositories/fiboa/croatia/description/) | Publicly available data |  |
| [Field boundaries for Czech](https://source.coop/repositories/fiboa/czech/description/) | CC-0 |  |
| [Field boundaries for Estonia](https://source.coop/repositories/fiboa/estonia-ec/description/) | CC-BY-SA-3.0 | Põllumajanduse Registrite ja Informatsiooni Amet |
| [Field boundaries for Flanders, Belgium](https://source.coop/repositories/fiboa/be-vlg/description/) | Licentie modellicentie-gratis-hergebruik/v1.0 |  |
| [Field boundaries for France from Eurocrops (2018)](https://source.coop/repositories/fiboa/france-ec/description/) | CC-BY-SA-4.0 | Institut National de l'Information Géographique et Forestière |
| [Field boundaries for Latvia from EuroCrops (2021)](https://source.coop/repositories/fiboa/ec-lv/description/) | CC-BY-4.0 | Lauku atbalsta dienests |
| [Field boundaries for Luxembourg](https://source.coop/repositories/fiboa/luxembourg/description/) | CC-BY-4.0 | Luxembourg ministry of Agriculture |
| [Field boundaries for Mecklenburg-Western Pomerania, Germany](https://source.coop/repositories/fiboa/de-mv/description/) | No restrictions apply |  |
| [Field boundaries for Portugal](https://source.coop/repositories/fiboa/portugal/description/) | No conditions apply |  |
| [Field boundaries for Saarland, Germany](https://source.coop/repositories/fiboa/de-sl/description/) | cc-by-4.0 | © GDI-SL 2024 |
| [Field boundaries for Saxony, Germany](https://source.coop/repositories/fiboa/de-sax/description/) | dl-de/by-2-0 | Sächsisches Landesamt für Umwelt, Landwirtschaft und Geologie |
| [Field boundaries for Slovakia](https://source.coop/repositories/fiboa/slovakia/description/) | Publicly available data |  |
| [Field boundaries for Slovenia](https://source.coop/repositories/fiboa/slovenia/description/) | Publicly available data |  |
| [Field boundaries for Slovenia from EuroCrops (2021)](https://source.coop/repositories/fiboa/slovenia-ec/description/) | CC-BY-SA-4.0 | Ministrstvo za kmetijstvo, gozdarstvo in prehrano |
| [Field boundaries for Sweden](https://source.coop/repositories/fiboa/sweden/description/) | CC0-1.0 | Jordbruksverket |
| [Field boundaries for Switzerland](https://source.coop/repositories/fiboa/switzerland/description/) | Open BY |  |
| [Field boundaries for The Netherlands](https://source.coop/repositories/fiboa/nl-ref/description/) | CC0-1.0 |  |
| [Field boundaries for ireland](https://source.coop/repositories/fiboa/ireland/description/) | CC-BY-4.0 | Ireland Department of Agriculture, Food and the Marine |
| [Field boundaries for the west of Bahia state, Brazil](https://source.coop/repositories/fiboa/br-ba-lem/description/) | CC-BY-4.0 |  |
| [Fields of the World](https://source.coop/repositories/kerner-lab/fields-of-the-world/description/) | various |  |
| [Finnish Crop Fields (Maatalousmaa)](https://source.coop/repositories/fiboa/finland/description/) | CC-BY-4.0 | Finnish Food Authority |
| [Germany, Berlin / Brandenburg](https://source.coop/repositories/fiboa/de-bb/description/) | dl-de/by-2-0 | Land Brandenburg |
| [Germany, Lower Saxony](https://source.coop/repositories/fiboa/de-nds/description/) | dl-de/by-2-0 | Land Niedersachsen |
| [Germany, North Rhine-Westphalia](https://source.coop/repositories/fiboa/de-nrw/description/) | dl-de/by-2-0 | Land Nordrhein-Westfalen / Open.NRW |
| [Germany, Schleswig-Holstein](https://source.coop/repositories/fiboa/de-sh/description/) | dl-de/zero-2-0 | Land Schleswig-Holstein |
| [Germany, Thuringia](https://source.coop/repositories/fiboa/de-th/description/) | dl-de/by-2-0 | Thüringer Landesamt für Landwirtschaft und Ländlichen Raum |
| [Lacuna labels](https://source.coop/repositories/fiboa/lacunalabels/description/) | Participant license agreement for the NICFI contract |  |
| [UKFields](https://zenodo.org/records/11110206) | CC-BY-4.0 | Bancroft S, Wilkins J |

* **Last updated:** Nov 17 2024, 01:36 
* **Count:** 34

## Add your dataset

If you want, follow the [How To](HOWTO.md) to create a new dataset using fiboa CLI.

Once your dataset is ready, you have two options to add your dataset:
1. If it has a STAC Collection for it, edit [this file](https://github.com/fiboa/fiboa.github.io/edit/main/stac/catalog.json), add your Collection as a child to the STAC catalog, and lastly create a PR.
2. In all other cases, edit [this file](https://github.com/fiboa/data/edit/main/README.md.jinja), add your dataset to the table (after the `endfor %}`), and lastly create a PR.

Once the PR is merged your data will be listed here shortly after (it's updated every night).