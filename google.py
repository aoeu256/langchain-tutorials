import os
api_key = 'AIzaSyANFnvMv8_fJvAmdm2y4F1FSfCalVXMaO4'
os.environ['GOOGLEAPI'] = api_key
os.environ['GOOGLECSX'] = 'a229f6e2ff2824c73'

import requests
import os
api_key = os.environ['GOOGLEAPI']

endpoint = 'https://www.googleapis.com/customsearch/v1'
params = {
    'key': api_key,
    'cx': os.environ['GOOGLECSX'],
    'q': 'linux'
}

response = requests.get(endpoint, params=params)
rs = response.json()
