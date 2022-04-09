from flask import jsonify, make_response


def handle_feedback(message, sentimentNum = None): 
    """
    Handles responses for other concerns such as refunds, exchanges and anything that the bot does not understand.
    parameters: 
                sentimentNum - denotes whether the text from customer is a positive or negative sentiment.
                intent - holds a string representing the intent detected.
    returns: Nothing
    """
    response = None
    # If sentimentNum is a negative number then the text denotes a negative sentiment. 
    # If sentimentNum is a positive number then the text denotes a positive sentiment.
    # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
    # print("test: ",sentimentNum)
    if(sentimentNum<0):     
        response = "Bot: Sorry to hear that!"
    if(sentimentNum>0):
        response = "Bot: That's great! Thank you for your feedback!"
    
    # If the user input is negative or the bot does not understand the user intent, then resolve user concern.
    if(sentimentNum <= 0):
        response = response + '''\n
Here is our contact information:
1) Walmart\n 123 Main Street\n Toronto, Ontario\n M5V 2K7.
2) 416-555-1234
Please let us know your concerns!
        '''

    return {"fulfillmentMessages": [{"text": {"text": [response]}}]}

def handle_exchange_request(sentimentNum):
    """
    Handles requests for exchanges
    parameters: None
    returns: Nothing
    """
    # If sentimentNum is a negative number then the text denotes a negative sentiment. 
    # If sentimentNum is a positive number then the text denotes a positive sentiment.
    # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
    # print("test: ",sentimentNum)
    if(sentimentNum<0):     
        print("Bot: Sorry to hear that!")
    return "Bot: You can exchange the product within 2 weeks (if perishable, then within 1-2 days) of purchase by visiting our store.\nPlease ensure that: \n1. the product is unused \n2. the price tags are intact \n3. you bring the bill along with the product."


def handle_refund_request(sentimentNum):
    """
    Handles requests for refunds
    parameters: None
    returns: Nothing
    """
    # If sentimentNum is a negative number then the text denotes a negative sentiment. 
    # If sentimentNum is a positive number then the text denotes a positive sentiment.
    # If sentimentNum is equal to zero, it's a neutral sentiment so print nothing.
    # print("test: ",sentimentNum)
    if(sentimentNum<0):     
        print("Bot: Sorry to hear that!")
    return "You can request for a refund or return in 2 ways:\n1. place a request on our website(our agent will come to pick up the product)\n2. directly visit our store\nNote that all requests for refunds or returns have to be made within 2 weeks of purchasing.\nAfter your refund/return is processed, the money will be refunded either:\n1. To your original payment method (if paid by credit/debit card\n2. Or as store credit"
