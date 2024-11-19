# How to create a cloud-native fiboa dataset using fiboa CLI

**WORK IN PROGRESS**

## Once when starting with fiboa

The following steps you usually only need to do once:

1. Install Python 3.9 or later, GDAL 3.8 or later, [tippecanoe](https://github.com/felt/tippecanoe), and AWS CLI
   - If you have trouble installing Python, GDAL, etc., consider using the conda environment.
   Install Anaconda and run the following commands using the env.yml file provided in this repository:
      - `conda env create -f env.yml`
      - `conda activate ftw`
2. Clone the [fiboa CLI repository](https://github.com/fiboa/cli):
   `git clone https://github.com/fiboa/cli`
   and `cd cli` to switch into the new folder.
3. Install the dependencies of the fiboa cli repo and the CLI itself:
   `pip install -e .`
4. Check whether the CLI works: `fiboa --version`

## Once when creating a new dataset

5. Create a converter using fiboa CLI converters, see the
   [template](https://github.com/fiboa/cli/blob/main/fiboa_cli/datasets/template.py).
6. If the dataset is available under an open license, we also want to create a test assuming the converter is named `xx_yy`:
   1. Install development dependencies: `pip install -r /path/to/requirements.txt`
   2. Create a new folder for the test data: `mkdir tests/data-files/convert/xx_yy`
   3. Create a subset of the dataset: `ogr2ogr tests/data-files/convert/xx_yy/input_file.gpkg -limit 100 /path/to/input_file.gpkg`
   4. Update the test file `tests/test_convert.py` to include your converter
   5. Run the tests: `pytest`. Iterate on 4 and 5 until the tests succeed.
7. Register at Source Cooperative and email `hello@source.coop` for permission to publish in the fiboa organization. 
8. [Create a new repository](https://source.coop/repositories/new/) in the fiboa organization, e.g. `@fiboa/xx-yy`.
   You'll find it at `https://source.coop/fiboa/xx-yy/`
9. Create a new folder for your data, e.g. data
   `mkdir data`
10. Create a README file at `data/README.md` and a license file at `data/LICENSE.txt`
    An example repository with a README etc. can be found here:
    <https://source.coop/fiboa/de-nrw/>

## Each time you update the dataset

11. Go to the parent folder of the folder that contains your data (e.g. `data`) in CLI
12. Run the converter, e.g. `xx_yy`:
    `fiboa convert xx_yy -o data/xx-yy.parquet -h https://source.coop/fiboa/xx-yy/ --collection`
    Make sure there are no errors (usually in red) or warnings (usually in yellow)
13. Validate the result, e.g. `fiboa validate data/xx-yy.parquet --data` and run the tests `pytest`
14. Move the collection.json into a stac folder:
    `mkdir data/stac` and `mv data/collection.json data/stac`
15. Update the README file at `data/README.md`
16. Create PMTiles file:
    `ogr2ogr -t_srs EPSG:4326 geo.json data/xx-yy.parquet`
    and
    `tippecanoe -zg --projection=EPSG:4326 -o data/xx-yy.pmtiles -l xx-yy geo.json --drop-densest-as-needed`
17. Edit the STAC Collection, update the paths, and everything else that you want to customize.
    Also don't forget to add a link to the PMTiles file using the
    [corresponding STAC extension](https://github.com/stac-extensions/web-map-links?tab=readme-ov-file#pmtiles).
18. Create a new API key, at: `https://source.coop/repositories/fiboa/xx-yy/manage`
19. Set the environment variables as follows (Linux/MacOS):

    ```bash
    export AWS_ENDPOINT_URL=https://data.source.coop
    export AWS_ACCESS_KEY_ID=<Access Key ID>
    export AWS_SECRET_ACCESS_KEY=<Secret Access Key>
    ```

    Note: Windows users may need to change the commands slightly. Use e.g.
    `$env:AWS_ENDPOINT_URL="[us-west-2](https://data.source.coop)"` instead of `export AWS_ENDPOINT_URL=https://data.source.coop`.
20. Upload to AWS:
    `aws s3 sync data s3://fiboa/xx-yy/`

If you've created and published a STAC Collection for your dataset, make sure to add it to the
STAC catalog that combines all datasets into a single STAC catalog
It will also publish your dataset to the
[fiboa data overview page](https://github.com/fiboa/data/blob/main/README.md).
Create a PR to add your STAC Collection as child link to the following file:
<https://github.com/fiboa/fiboa.github.io/blob/main/stac/catalog.json>
See also the [README](README.md#add-your-dataset) for an alternative.
