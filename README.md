# google-maps-geocoding-api-script

## Setup

1. Adapted from https://github.com/googlemaps/google-maps-services-python for project use. Follow setup instructions here in the google repo.

2. Requires setup of Google Cloud Platform, APIs and services, credentials API key. Key needs to be provided in google_map_api.py

## Usage

1. Update the input file and output file in google_map_api.py

2. $ python google_map_api.py

## Additional Info

1.Resources for OpenMap search Nominatim API:

- Doing directly in jupyter notebook. Get latitude and longitude data columns for location dataset, and put those longitude and latitude on a map https://peterhaas-me.medium.com/how-to-geocode-with-python-and-pandas-4cd1d717d3f7

- https://github.com/eddymio/bulk-api-request

- https://gist.github.com/adrianespejo/5df28ce987db64ba753619502ee3d812

- https://linkstraffic.net/from-csv-to-api-python-3-parsing/

2. Nominatim geocoding API does not recognise abbreviations in addresses, and will return error if in request. Google API does recognise abbreviations.

3. Did not use Nominatim API as some geocoding data was not complete for a number of required locations when tried
