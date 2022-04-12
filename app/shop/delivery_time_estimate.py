import os
import re

import requests


def delivery_time_estimate(params):
    '''
    Handles requests for estimated delivery time
    parameters: dictionary or json object
    returns: json object (of reply message)
    '''
    # Parse the address
    address = str(params["street-address"]["street-address"]) + " " + str(params["geo-city"]) + " " + str(params["geo-state"]) + " " + str(params["geo-country"])
    address.replace(",", " ")
    address = re.sub(r'\s+', '%20', address)

    params = {'key' : os.getenv('API_KEY'), 'origins' : 'c', 'destinations' : address, 'departure_time': 'now'}
    result = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?", params=params).json()
    info = result["rows"][0]["elements"]
    # If the info is not empty, the given addresses are valid 
    if len(info) > 0:
        response = "It will take " + str(info[0]["duration_in_traffic"]["text"])
    else:
        response = "Sorry, I could not find your address"
    return {"fulfillmentMessages": [{"text": {"text": [response]}}]}