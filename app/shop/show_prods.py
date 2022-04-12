from flask import url_for


def show_prods():
    '''
    Show category of products with checkout button
    '''
    response = {
        "fulfillmentMessages": [
            {
                "payload":{
                    "facebook":{
                        "attachment":{
                            "type":"template",
                            "payload":{
                                "template_type":"generic",
                                "elements":[
                                {
                                    "title":"Shiloah",
                                    "image_url":"https://i.pinimg.com/originals/39/a0/ca/39a0caa2248ef5c7ee73ce7662943990.jpg",
                                    "subtitle":"This is collected from the Copacabana Beach, Brazil, one of the world's most famous beaches.",
                                    "buttons":[
                                    {
                                        "type":"postback",
                                        "title":"Checkout",
                                        "payload":"trigger checkout"
                                    }          
                                    ]      
                                },
                                {
                                    "title":"Shaquille",
                                    "image_url":"https://i.pinimg.com/originals/3b/78/7d/3b787d827698aa4941feee09f34256e2.jpg",
                                    "subtitle":"This is collected from Santa Monica Beach, where nostalgia meets California living.",
                                    "buttons":[
                                    {
                                        "type":"postback",
                                        "title":"Checkout",
                                        "payload":"trigger checkout"
                                    }          
                                    ]      
                                }
                                ]
                            }
                        }
                    }
                }
            }
        ]
    }

    return response