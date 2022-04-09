from operator import concat
import os
import re
import requests
from PIL import Image
import io
class AccessHandler:
    """
    A handler class to handle directions
    """

    def handle(self):
        print("Bot: What is your address?\n     Please provide street number, city, state and country.")
        address = input("You: ")
        address.replace(",", " ")
        address = re.sub(r'\s+', '+', address)
        # TODO: Better way to store api key
        # Directions
        # regenerate key
        params = {'key' : os.getenv('API_KEYs'), 'origin' : address, 'destination' : '1555+Banks+Rd+Kelowna+BC',}
        response = requests.get("https://maps.googleapis.com/maps/api/directions/json?", params=params).json()
        # Get static map
        polylines = response['routes'][0]['overview_polyline']['points']
        params = {'key' : os.getenv('API_KEYs'), 'path' : concat('enc:',polylines), 'size' :'500x400','format': 'jpeg'}
        response = requests.get("https://maps.googleapis.com/maps/api/staticmap?", params=params, stream=True)
        img = Image.open(io.BytesIO(response.content))
        img.show()   