import json
import osm_nominatim_api
from pprint import pprint
import logging
import pandas as pd

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':

    query_params = {
        "namedetails": 1,
        "polygon_geojson": 1,
        "hierarchy": 1,
    }

    df_extract = pd.read_csv("unique_address.csv", index_col=False)


    with open("unique_address.csv") as original_file:
        lines = original_file.read().splitlines()

    for line in lines:
        res = osm_nominatim_api.fetch_osm_search(query=f"{line}"+",SINGAPORE", params=query_params)
        with open("unique_address_lat_lon.csv", "a") as output_file:
            try:
                lat = json.dumps(res[0]["lat"])
                lon = json.dumps(res[0]["lon"])
                output_file.write(line + "," + lat + "," + lon + "\n")
            except:
                output_file.write(line + "," + "========== ERROR PLEASE TRY AGAIN ==========" + "\n")
