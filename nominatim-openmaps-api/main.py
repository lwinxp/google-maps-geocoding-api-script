# import argparse
import json

# import template_reader
# import csv_reader
# import yaml
# import api
import osm_nominatim_api
from pprint import pprint
import logging
import pandas as pd

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)


# def merge(template_data, csv_data):
#     for cd in csv_data:
#         for td in template_data:
#             td['type'] = cd.get('tradeType')
#             td['date'] = cd.get('dateOfTrade')
#             td['amount'] = cd.get('tradeAmount')
#             td['trader']['id'] = cd.get('personId')
#             td['trader']['name'] = cd.get('personName')

#     return template_data


# def get_config(args):
#     with open(args.config, 'r') as stream:
#         try:
#             return yaml.safe_load(stream)
#         except yaml.YAMLError as exc:
#             logger.error(exc)


# def parse_cli():
#     parser = argparse.ArgumentParser(description='Send CSV over to API')
#     parser.add_argument('--csv', help='csv data file path', required=False, default='data.csv')
#     parser.add_argument('--json', help='data template file path', required=False, default='template.json')
#     parser.add_argument('--config', help='Config file path', required=False, default='config.yml')
#     return parser.parse_args()


if __name__ == '__main__':

    # cli_args = parse_cli()
    # config = get_config(cli_args)

    # data = csv_reader.read_csv(cli_args.csv)
    # template = template_reader.json_reader('template.json')

    # multi_json_to_post = merge(template, data)

    query_params = {
        "namedetails": 1,
        "polygon_geojson": 1,
        "hierarchy": 1,
    }

    # query_to_post = "423 Serangoon Central, Singapore"

    # df = pd.read_csv("train_subset.csv")
    # block = df.block
    # street = df.street_name

    # cols = ['block','street_name']

    # pd.read_csv("train_subset.csv", usecols=cols).to_csv("train_subset_extract.csv", index=False, header=None)


    # list_to_post = ["328,UBI AVE 1", "271,TOH GUAN RD", "205,TOA PAYOH NORTH" ]

    # df_extract = pd.read_csv("train_subset_extract.csv")

    df_extract = pd.read_csv("unique_address.csv", index_col=False)


    with open("unique_address.csv") as original_file:
        lines = original_file.read().splitlines()

    # with open("train_subset.csv") as original_file:
    #     lines = original_file.read().splitlines()

    # for i in range(len(df_extract.index)):
    for line in lines:
        # res = osm_nominatim_api.fetch_osm_search(query=list_to_post[i]+",SINGAPORE", params=query_params)
        res = osm_nominatim_api.fetch_osm_search(query=f"{line}"+",SINGAPORE", params=query_params)
        with open("unique_address_lat_lon.csv", "a") as output_file:
            try:
                lat = json.dumps(res[0]["lat"])
                lon = json.dumps(res[0]["lon"])
                output_file.write(line + "," + lat + "," + lon + "\n")
            except:
                output_file.write(line + "," + "========== ERROR PLEASE TRY AGAIN ==========" + "\n")


    # for query_to_post in list_to_post:
    # # for json_to_post in multi_json_to_post:
    #     # res = api.post('http://mockbin.com/request', '', '', json_to_post)
    #     res = osm_nominatim_api.fetch_osm_search(query=query_to_post+",SINGAPORE", params=query_params)

    #     # logger.info('Results %s', json.dumps(res, indent=4, sort_keys=True))
    #     pprint(res)


    #     with open("train_subset_lat_lon.csv", "a") as output_file:
    #         for line in lines:
    #         # for i in range(len(lines)):

    #             lat = json.dumps(res[0]["lat"])
    #             lon = json.dumps(res[0]["lon"])
    #             output_file.write(line + f",{lat},{lon}" + "\n")
    #         # output_file.write(json.dumps(result[0]["lat"], ensure_ascii=False))
    #         # output_file.write(json.dumps(res, ensure_ascii=False))
