# from app.products.access_info import AccessHandler
from app.products.product_info import handle_prod_info
from app.products.store_info import StoreInfoHandler

def handle_intent(request):
    req = request.get_json()
    intent = req["queryResult"]["intent"]["displayName"]
    response = ""
    # if user asks about product, 
    # pass to store-info in route_to_handle. 
    # Set the undetected intent count to 0
    if("product" in intent):# intent can be product-stock or product-nutrition or product-price
        productName = req["queryResult"]["parameters"]["product-name"]
        # TODO: change ProductInfoHandler to function
        response = handle_prod_info(productName, intent)
    # if user asks about store, 
    # pass to store-info in route_to_handle. 
    # Set the undetected intent count to 0
    elif(intent == "store-info"):
        store_handler = StoreInfoHandler()
        response = store_handler.handle(req["queryResult"]["queryText"])
    # if user asks for exchange or refund or feedback, 
    # direct to other concerns handler in route_to_handle
    # elif(intent == "exchange-request" or intent == "refund-request" or intent == "feedback"):
    #         sentimentScore = response.sentiment_analysis_result.query_text_sentiment.score
    #         if("other-concerns" not in self.intents):     
    #             self.intents["other-concerns"] = OtherConcerns() 
    #         self.intents["other-concerns"].handle(sentimentScore, intent)
    #         self.undetected_intent_count = 0 # reset the undetected intent count if bot already responded the intent
    # # if user asks for directions to store
    # elif(intent == "access-request"):
    #     access_handler = AccessHandler()
    #     access_handler.handle()
        # self.undetected_intent_count = 0
    return response