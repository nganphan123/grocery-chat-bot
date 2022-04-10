from flask import jsonify, make_response


def handle_feedback(message, sentimentNum = None): 
    """
    Handles feedback from users and gives appropriate response based on sentiment
    Parameters: message, sentimentNum
    Return: json object
    """
    response = None
    # If sentimentNum is a negative number then the text denotes a negative sentiment. 
    # If sentimentNum is a positive number then the text denotes a positive sentiment.
    # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
    if(sentimentNum>0):
        return {"fulfillmentMessages": [{"text": {"text": ["That's great! Thank you for your feedback!"]}}]}
    
    # Sending quick replies message to user
    response = {
        "fulfillmentMessages": [
            {
                "payload": {
                    "facebook": {
                           "text": "Sorry to hear that! Would you like to call us or visit our store to resolve your concerns ?",
                            "quick_replies":[
                                {
                                    "content_type":"text",
                                    "title":"Phone dial",
                                    "payload":"phone"
                                },{
                                    "content_type":"text",
                                    "title":"Visit store",
                                    "payload":"visit"
                                }
                            ]
                    },
                }
            }
        ]
    }

    return make_response(jsonify(response))

def handle_exchange_request(sentimentNum):
    """
    Handles requests for exchanges
    parameters: None
    returns: Nothing
    """
    # If sentimentNum is a negative number then the text denotes a negative sentiment. 
    # If sentimentNum is a positive number then the text denotes a positive sentiment.
    # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
    response = "You can exchange the product within 2 weeks (if perishable, then within 1-2 days) of purchase by visiting our store.\nPlease ensure that: \n1. the product is unused \n2. the price tags are intact \n3. you bring the bill along with the product."
    if(float(sentimentNum)<0):     
        response = "Sorry to hear that!" + response
    return response


def handle_refund_request(sentimentNum):
    """
    Handles requests for refunds
    parameters: None
    returns: Nothing
    """
    # If sentimentNum is a negative number then the text denotes a negative sentiment. 
    # If sentimentNum is a positive number then the text denotes a positive sentiment.
    # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
    response = "You can request for a refund or return in 2 ways:\n1. place a request on our website(our agent will come to pick up the product)\n2. directly visit our store\nNote that all requests for refunds or returns have to be made within 2 weeks of purchasing.\nAfter your refund/return is processed, the money will be refunded either:\n1. To your original payment method (if paid by credit/debit card\n2. Or as store credit"
    if(float(sentimentNum)<0):     
        response = "Sorry to hear that!" + response
    return response
