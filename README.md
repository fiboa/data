
# fiboa Datasets

This repository provides you with all information about existing fiboa datasets.

## List of datasets

| Title | License | Provider |
| ----- | ------- | -------- |
| [Austria](https://data.source.coop/fiboa/austria/stac/collection.json) | CC-BY-4.0 | Agrarmarkt Austria |
| [Germany, Berlin / Brandenburg](https://data.source.coop/fiboa/de-bb/stac/collection.json) | dl-de/by-2-0 | Land Brandenburg |
| [Germany, Lower Saxony](https://data.source.coop/fiboa/de-nds/stac/collection.json) | dl-de/by-2-0 | Land Niedersachsen |
| [Germany, North Rhine-Westphalia](https://data.source.coop/fiboa/de-nrw/stac/collection.json) | dl-de/by-2-0 | Land Nordrhein-Westfalen / Open.NRW |
| [Germany, Schleswig-Holstein](https://data.source.coop/fiboa/de-sh/stac/collection.json) | dl-de/zero-2-0 | Land Schleswig-Holstein |

* **Last updated:** May 03 2024, 21:44 
* **Count:** 5

## Add your dataset

If you want, follow the [How To](HOWTO.md) to create a new dataset using fiboa CLI.

Once your dataset is ready, you have two options to add your dataset:
1. If it has a STAC Collection for it, edit [this file](https://github.com/fiboa/fiboa.github.io/edit/main/stac/catalog.json), add your Collection as a child to the STAC catalog, and lastly create a PR.
2. In all other cases, edit [this file](https://github.com/fiboa/data/edit/main/README.md.jinja), add your dataset to the table (after the `endfor %}`), and lastly create a PR.

Once the PR is merged your data will be listed here shortly after (it's updated every night).