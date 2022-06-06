from flask import Flask, request

app = Flask(__name__)
 
import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
import requests

write_token = "6408eab7199940528fd17e193b7c7f5e"

@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        '3c4fed617abb463caab073397f26507a',
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/items')
def get_items():
    x = requests.get("http://api.rollbar.com/api/1/items", headers={"X-Rollbar-Access-Token":"29b05bd130e14b27822d17787597ce72"})
    return x.text

@app.route('/items/<int:id>')
def get_item(id):
    x = requests.get(f"http://api.rollbar.com/api/1/item/{id}", headers={"X-Rollbar-Access-Token":"29b05bd130e14b27822d17787597ce72"})
    return x.text
    
@app.route('/items', methods=['POST'])
def post_item():
    x = requests.post("http://api.rollbar.com/api/1/item/", data=request.data, headers={"X-Rollbar-Access-Token":"3c4fed617abb463caab073397f26507a"})
    return x.text

@app.route('/items/<int:id>', methods=['PUT', 'PATCH'])
def put_item(id):
    x = requests.patch(f"http://api.rollbar.com/api/1/item/{id}", data=request.data, headers={"X-Rollbar-Access-Token":"6408eab7199940528fd17e193b7c7f5e"})
    return x.text
