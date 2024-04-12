# How to create a cloud-native fiboa dataset using fiboa CLI

**WORK IN PROGRESS**

## Once when starting with fiboa

The following steps you usually only need to do once:

1. Install Python 3.9 or later, GDAL 3.8 or later, [tippecanoe](https://github.com/felt/tippecanoe) and AWS CLI
2. Clone the [fiboa CLI repository](https://github.com/fiboa/cli):
   `git clone https://github.com/fiboa/cli`
   and `cd cli` to switch into the new folder.
3. Install the dependencies of the fiboa cli repo and the CLI itself:
   `pip install -e .`
4. Check whether the CLI works: `fiboa --version`

## Once when creating a new dataset

5. Create a converter using fiboa CLI converters, see the the
   [template](https://github.com/fiboa/cli/blob/main/fiboa_cli/datasets/template.py).
   Create a PR for it.
6. Register at Source Cooperative and ask Michelle for permission to publish in the fiboa organization.
7. [Create a new repository](https://beta.source.coop/repositories/new/) in the fiboa organization, e.g. `@fiboa/xx-yy`.
   You'll find it at `https://beta.source.coop/fiboa/xx-yy/`
8. Create a new folder for your data, e.g. data
   `mkdir data`
9. Create a README file at `data/README.md` and a license file at `data/LICENSE.txt`
   An example repository with a README etc. can be found here:
   <https://beta.source.coop/fiboa/de-nrw/>

## Everytime you update the dataset

10. Go to the parent folder of the folder that contains your data (e.g. `data`) in CLI
11. Run the converter, e.g. `xx_yy`:
    `fiboa convert xx_yy -o data/xx-yy.parquet -h https://beta.source.coop/fiboa/xx-yy/ --collection`
12. Validate the result, e.g. `fiboa validate data/xx-yy.parquet --data`
13. Move the collection.json into a stac folder:
    `mkdir data/stac` and `mv data/collection.json data/stac`
14. Update the README file at `data/README.md`
15. Create PMTiles file:
    `ogr2ogr -t_srs EPSG:4326 geo.json data/xx-yy.parquet`
    and
    `tippecanoe -zg --projection=EPSG:4326 -o data/xx-yy.pmtiles -l xx-yy geo.json --drop-densest-as-needed`
16. Edit the STAC Collection, update the paths and everything else that you want to customize.
    Also don't forget to add a link to the PMTiles file using the
    [corresponding STAC extension](https://github.com/stac-extensions/web-map-links?tab=readme-ov-file#pmtiles).
17. Create new credentials for S3, at: `https://beta.source.coop/repositories/fiboa/xx-yy/download/`
18. Copy the credentials.
    Windows users may need to change the commands slightly. Use e.g.
    `$env:AWS_DEFAULT_REGION="us-west-2"` instead of `export AWS_DEFAULT_REGION=us-west-2`
19. Upload to AWS:
    `aws s3 sync data s3://us-west-2.opendata.source.coop/fiboa/xx-yy/`