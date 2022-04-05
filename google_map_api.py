import googlemaps
from datetime import datetime
import pprint
import logging
import json
import pandas as pd



logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# df = pd.read_csv("original_unique_address_subset.csv", index_col=False)

gmaps = googlemaps.Client(key='<Place your Google Maps API key here>')

from csv import reader
# skip first line i.e. read header first and then iterate over each row od csv as a list
with open('original_unique_address.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            query = row[0] + ", SINGAPORE"
            print(query)

            # logger.info(type(str(row[0])))

            with open("original_unique_address_latlng.csv", "a") as output_file:
              try:
                res = gmaps.geocode(query)
                lat = res[0]['geometry']['location']['lat']
                lng = res[0]['geometry']['location']['lng']
                output_file.write(row[0] + "," + str(lat) + "," + str(lng) + "\n")
              except Exception as e:
                logger.error(row[0] + "," + "========== ERROR PLEASE TRY AGAIN ========== :" + f"{e}")

# with open("original_unique_address_subset.csv") as original_file:
#   lines = original_file.read().splitlines()
#   for line in lines:
#     logger.info('Type of line:', type(line))

# for line in lines:
#   query = f"{line}"
#   logger.info('Query:', str(query))
#   res = gmaps.geocode(query)
#   with open("original_unique_address_subset_latlng.csv", "a") as output_file:
#     try:
#       lat = res[0]['geometry']['location']['lat']
#       lng = res[0]['geometry']['location']['lng']
#       output_file.write(line + "," + lat + "," + lng + "\n")
#     except Exception as e:
#       logger.error(line + "," + "========== ERROR PLEASE TRY AGAIN ========== :" + str(e))
#       output_file.write(line + "," + "========== ERROR PLEASE TRY AGAIN ========== :" + str(e))
#   # except Exception as e: # work on python 3.x
#   #     logger.error('Failed to upload to ftp: '+ str(e))

# =====================


# gmaps = googlemaps.Client(key='')

# # Geocoding an address
# geocode_result = gmaps.geocode('205 TOA PAYOH NTH, SINGAPORE')

# # Look up an address with reverse geocoding
# # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# # now = datetime.now()
# # directions_result = gmaps.directions("Sydney Town Hall",
# #                                      "Parramatta, NSW",
# #                                      mode="transit",
# #                                      departure_time=now)


# # full = json.loads(geocode_result)

# # lat = full['location']['lat']

# # lng = full['location']['lng']

# logger.info('Full Results %s', geocode_result)

# logger.info('Results %s', geocode_result[0]['geometry']['location'])

# # logger.info('Results %s', json.dumps(geocode_result, indent=4, sort_keys=True))

# # pprint(full)