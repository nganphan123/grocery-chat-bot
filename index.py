from flask import Flask, request
from app.database import Database

from app.response.handle_intent import handle_intent

app = Flask(__name__)

@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    return handle_intent(request)

if __name__ == '__main__':
    app.run()
