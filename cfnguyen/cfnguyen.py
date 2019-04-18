# ca phe nguyen

from flask import Flask, app, request, jsonify, make_response, abort
import requests
app = Flask(__name__)

bill_id = "bill123"
PoPServer = "http://localhost:1234"

@app.route('/')
def home():
    return "cf nguyen"

bill_data = {'id': bill_id, "price": 1000000, "data": {"price": 1000000, "items": [{"title": "bot tret tuong"}]}}

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
