import os
from urllib import response
from requests import request
import requests


def handle_checkout():

    # Get access token
    oauth_response = requests.post("https://api-m.sandbox.paypal.com/v1/oauth2/token", 
                            auth=(os.getenv('client_id'), os.getenv('secret')),
                            headers= {'Accept': 'application/json',  
                                        'Accept-Language': 'en_US'},
                            params={'grant_type': 'client_credentials'}).json()
    token = oauth_response['access_token']

    headers = {"Content-Type" : "application/json", "Authorization" : ("Bearer " + token)}
    data = '''{
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
            "return_url": "https://www.facebook.com/",
            "cancel_url": "https://www.facebook.com/"
        }
    }'''
    result = requests.post("https://api-m.sandbox.paypal.com/v2/checkout/orders", headers = headers, data = data).json()
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

    # return {"fulfillmentMessages": [{"text": {"text": [str(redirect_link)]}}]}
    return response
