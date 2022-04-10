# from app.products.access_info import AccessHandler
from app.concerns.other_concern import handle_exchange_request, handle_feedback, handle_refund_request
from app.products.product_info import handle_prod_info
from app.products.store_info import handle_store_info

def handle_intent(request):
    """
    Handles request for different intents
    Intents: product_info, store_info, exchange_request, refund_request, feedback, access_request
    Parameters: request (json object)
    Returns: json object
    """
    req = request.get_json()
    intent = req["queryResult"]["intent"]["displayName"]
    response = None
    # Depends on the intent, call the appropriate handle sub-function
    if("product" in intent):# intent can be product-stock or product-nutrition or product-price
        productName = req["queryResult"]["parameters"]["product-name"]
        # TODO: change ProductInfoHandler to function
        response = {"fulfillmentMessages": [{"text": {"text": [handle_prod_info(productName, intent)]}}]}
    elif(intent == "store-info"):
        response = {"fulfillmentMessages": [{"text": {"text": [handle_store_info(req["queryResult"]["queryText"])]}}]}
    elif(intent == "feedback"):
        response = handle_feedback(req["queryResult"]["queryText"],req["queryResult"]["sentimentAnalysisResult"]["queryTextSentiment"]["score"])
    elif(intent == "refund-request"):
        response = {"fulfillmentMessages": [{"text": {"text": [handle_refund_request(req["queryResult"]["sentimentAnalysisResult"]["queryTextSentiment"]["score"])]}}]}
    elif(intent == "exchange-request"):
        response = {"fulfillmentMessages": [{"text": {"text": [handle_exchange_request(req["queryResult"]["sentimentAnalysisResult"]["queryTextSentiment"]["score"])]}}]}
    # # if user asks for directions to store
    # elif(intent == "access-request"):
    #     access_handler = AccessHandler()
    #     access_handler.handle()
        # self.undetected_intent_count = 0
    return response