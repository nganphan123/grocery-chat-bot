import re
import requests
class AccessHandler:
    """
    A handler class to handle directions
    """

    def handle(self):
        print("Bot: What is your address?")
        address = input("You: ")
        address.replace(",", " ")
        address = re.sub(r'\s+', '+', address)
        # TODO: Better way to store api key
        params = {'key' : 'AIzaSyDxkAgIWYDlA35vQp8HVwjO8DRroy-tkx4', 'origin' : address, 'destination' : '1555+Banks+Rd+Kelowna+BC',}
        response = requests.get("https://maps.googleapis.com/maps/api/directions/json?", params=params)
        print(response.text)