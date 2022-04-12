from app.database import STORE_INFO
import re

def handle_store_info(message: str) -> str:
    # Call parser
    kwargs = parse(message=message)

    # If there is a topic detected, we find the response
    # By calling the handler with the message (for convenience) and its necessary arguments
    response = None
    if kwargs:
        response = fetch_info(message, **kwargs)

    return response

def parse(message) -> dict:
    request = None

    # Store-related patterns    
    name_pattern = re.compile(
        r"(name)", re.IGNORECASE)
    location_pattern = re.compile(
        r"(where|location|address|street)", re.IGNORECASE)
    opening_pattern = re.compile(
        r"(when|open|close|opening|closing|hours)", re.IGNORECASE)
    phone_pattern = re.compile(r"(phone|number)", re.IGNORECASE)
    website_pattern = re.compile(r"(website|url|web)", re.IGNORECASE)
    city_pattern = re.compile(r"(city|town)", re.IGNORECASE)
    province_pattern = re.compile(r"(province|state)", re.IGNORECASE)
    country_pattern = re.compile(r"(country)", re.IGNORECASE)
    postal_code_pattern = re.compile(r"(postal|zip)", re.IGNORECASE)

    if location_pattern.search(message):
        request = "address"
    elif opening_pattern.search(message):
        request = "opening_hours"
    elif phone_pattern.search(message):
        request = "phone"
    elif website_pattern.search(message):
        request = "website"
    elif city_pattern.search(message):
        request = "city"
    elif province_pattern.search(message):
        request = "province"
    elif postal_code_pattern.search(message):
        request = "postal_code"
    elif country_pattern.search(message):
        request = "country"
    elif name_pattern.search(message):
        request = "name"

    return {"request": request} if request else None

def fetch_info(message=None, **kwargs) -> str:
    # kwargs are arguments such as product_name, price, operators (<. >)
    # This really depends on how you define your parser
    reply = "It is {}".format(STORE_INFO[kwargs["request"]])
    return reply

