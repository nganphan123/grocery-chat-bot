from app.database import Database

def handle_prod_info(product: str, intent=None) -> str:
    if intent is not None:

        # Connect database
        db = Database.instance()
        db.connect()  # Start a connection
        db.init_database()  # Initialize the database

        intent = intent.split("-")[1] # hardcoded to filter intent: product-<intent> Ex. product-price -> intent = price

        request = None

        cursor = db.execute_query(
            "SELECT product.id FROM product WHERE product.name = ? OR product.names = ?", 
                params=tuple([product, product]))
        data = cursor.fetchone()
        if (not data):
            return None
        
        request = {"request": intent, "id": data[0]}

        return fetch_info(db, **request)

def fetch_info(db, **kwargs) -> str:
    # kwargs are arguments such as product_name, price, operators (<. >)
    # This really depends on how you define your parser
    prod_id = kwargs["id"]

    # Get the product information
    products = db.get_product("id", prod_id)

    # Since id is unique, we can assume there is only one product
    product = products[0]

    reply = None

    prod_msg_type = kwargs.get("request")
    if prod_msg_type == "price":
        reply = "%s cost $%s %s." % (
            product['names'].capitalize(), product['price'], product['price_scale'])
    elif prod_msg_type == "stock":
        if product['in_stock']:
            reply = "%s are in stock." % (product['names'].capitalize())
        else:
            reply = "%s are out of stock." % (
                product['names'].capitalize())
    elif prod_msg_type == "nutrition":
        reply = "%s Nutrition Facts: Calories = %s, Protein = %s, Carbs = %s, Sugar = %s, Fat = %s." % (
            product['name'].capitalize(), product['calories'], product['protein'], product['carbs'], product['sugar'], product['fat'])

    return reply       