from urllib import response
from flask import Flask, render_template, request

from app.response.handle_intent import handle_intent

app = Flask(__name__,template_folder='./app/pages')

@app.route("/", methods = ['GET', 'POST'])
def index():
    return "<h1>Seashore seashell shop</h1>"

@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    return handle_intent(request)

@app.route('/order-success', methods = ['GET','POST'])
def order_success():
    # handle payment execute
    return render_template('confirm-payment.html')

if __name__ == '__main__':
    app.run()
