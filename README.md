# google-maps-geocoding-api-script

## Purpose

- The scripts in this repo take in a input CSV file with 1 column of location address

- Request is made to map API service for location codes (latitude, longitude)

- Results are returned in a new output CSV file with 1 column of the original location address, 1 column of latitude and 1 column of logitude  

## Setup

1. Adapted from https://github.com/googlemaps/google-maps-services-python for project use. Follow setup instructions here in the google repo.

2. Requires setup of Google Cloud Platform, APIs and services, credentials API key. Key needs to be provided in google_map_api.py

## Google Maps API Usage

1. Update the input CSV filename and output CSV filename in google_map_api.py

2. Update GCP API key

3. $ python3 google_map_api.py

## OpenStreetMap Nominatim API Usage

Script in the nominatim-openmaps-api folder works, although suggest not to use unless understand limitations in Additional Details

1. Update the input CSV filename and output CSV filename in main.py

2. $ python3 main.py

## Additional Info

1. google_map_api.py can be used directly in jupyter notebook as well. 

2. Resources for OpenMap search Nominatim API:

-  https://peterhaas-me.medium.com/how-to-geocode-with-python-and-pandas-4cd1d717d3f7 (get latitude and longitude data columns for location dataset, and put those longitude and latitude on a map)

- https://github.com/eddymio/bulk-api-request

- https://gist.github.com/adrianespejo/5df28ce987db64ba753619502ee3d812

- https://linkstraffic.net/from-csv-to-api-python-3-parsing/

3. Nominatim geocoding API does not recognise abbreviations in addresses, and will return error if in request body. Google Maps geocoding API recognises abbreviations

4. abbreviations_cleaning.ipynb contains suggested regex to cleanup abbreviations before constructing the input CSV file.

5. Nominatim API geocoding data may not be complete for newer locations. A number of required locations were not available and returned error when tried.
