import requests
from pprint import pprint
 
def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    resp = requests.get(url, params = {'address': address})
    return resp.json()
 
# calling geocode function
data = geocode('India gate')
 
# pretty-printing json response
pprint(data)
