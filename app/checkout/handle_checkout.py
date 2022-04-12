import json
import os
from flask import url_for
import requests


def handle_checkout():
    '''
    Handles checkout process
    parameters: none
    returns: json object
    '''
    # Get access token
    # client_id and secret are claimed from paypal sandbox website
    oauth_response = requests.post("https://api-m.sandbox.paypal.com/v1/oauth2/token", 
                            auth=(os.getenv('client_id'), os.getenv('secret')),
                            headers= {'Accept': 'application/json',  
                                        'Accept-Language': 'en_US'},
                            params={'grant_type': 'client_credentials'}).json()

    token = oauth_response['access_token']

    headers = {"Content-Type" : "application/json", "Authorization" : ("Bearer " + token)}
    data = {
        "intent": "CAPTURE", 
        "purchase_units": [
            {
                "reference_id": "1", 
                "amount": {
                    "currency_code": "CAD", 
                    "value": "100.00"
                }
            }
        ],
        "application_context": {
            "return_url": url_for('order_success',_external=True)
        }
    }
    
    # Make request to paypal checkout sandbox to get retrieve approve_url
    # Create button template in messenger that redirect to the approve_url for customer checkout experience
    # After customer finishes checkout, paypal redirects to the return_url (pages/order-success.html)
    result = requests.post("https://api-m.sandbox.paypal.com/v2/checkout/orders", headers = headers, data = json.dumps(data)).json()
    redirect_link = result["links"][1]["href"]
    response = {
        "fulfillmentMessages": [
            {
                "payload": {
                    "facebook": {
                        "attachment":{
                            "type":"template",
                            "payload":{
                                "template_type":"button",
                                "text":"Please checkout!",
                                "buttons":[
                                    {
                                        "type":"web_url",
                                        "url": redirect_link,
                                        "title": "Paypal",
                                        "webview_height_ratio": "full",
                                    }
                               ]
                            }
                        }
                    }
                }
            }
        ]
    }

    return response
    # return str(hhh)
