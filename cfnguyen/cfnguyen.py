# ca phe nguyen
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, app, request, jsonify, make_response, abort
import requests
import cfsetting as setting
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://postgres:123@localhost/wordcount_dev"
# db = SQLAlchemy(app)

app = setting.app
db = setting.db


bill_id = "bill123"
PoPServer = "http://localhost:1234"

@app.route('/')
def home():
    return "cf nguyen"

bill_data = {'bill_id': bill_id, "price": "1000000", "callback_url": "http://localhost:5000/callback", "data": {"price": 1000000, "items": [{"title": "bot tret tuong"}]}}

@app.route('/register', methods=["POST"])
def register_bill():
    """ client send a request for register a bill"""
    
    r = requests.post(PoPServer+"/pc", json = bill_data)
    return make_response(jsonify(r.json()))

@app.route('/bill/<string:id>', methods=["GET"])
def bill(id):
    """ get bill id
    """    
    if id == bill_id:        
        return make_response(jsonify(bill_data))
    abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
