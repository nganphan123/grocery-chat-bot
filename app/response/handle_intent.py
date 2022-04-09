# from app.products.access_info import AccessHandler
from app.concerns.other_concern import handle_feedback, handle_refund_request
from app.products.product_info import handle_prod_info
from app.products.store_info import handle_store_info

def handle_intent(request):
    req = request.get_json()
    intent = req["queryResult"]["intent"]["displayName"]
    response = None
    # if user asks about product, 
    # pass to store-info in route_to_handle. 
    # Set the undetected intent count to 0
    if("product" in intent):# intent can be product-stock or product-nutrition or product-price
        productName = req["queryResult"]["parameters"]["product-name"]
        # TODO: change ProductInfoHandler to function
        response = {"fulfillmentMessages": [{"text": {"text": [handle_prod_info(productName, intent)]}}]}
    # if user asks about store, 
    # pass to store-info in route_to_handle. 
    # Set the undetected intent count to 0
    elif(intent == "store-info"):
        response = {"fulfillmentMessages": [{"text": {"text": [handle_store_info(req["queryResult"]["queryText"])]}}]}
    elif(intent == "feedback"):
        response = handle_feedback(req["queryResult"]["queryText"],req["queryResult"]["sentimentAnalysisResult"]["queryTextSentiment"]["score"])
    elif(intent == "refund-request"):
        response = {"fulfillmentMessages": [{"text": {"text": [handle_refund_request(req["queryResult"]["queryText"])]}}]}
    # # if user asks for directions to store
    # elif(intent == "access-request"):
    #     access_handler = AccessHandler()
    #     access_handler.handle()
        # self.undetected_intent_count = 0
    return response