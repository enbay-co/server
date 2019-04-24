# Payment code server

# from flask import Flask, app, request, jsonify, make_response, abort
# import requests
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://postgres:123@localhost/wordcount_dev"
# database = SQLAlchemy(app)                             # L4
# db = database                                          # L5
from flask import redirect, url_for, request, make_response, jsonify
import popsetting as setting
from popdb import PaymentCode

app = setting.app
db = setting.db

PC_EMPTY=0      # emptry
PC_PAYED="PAYED" # da thanh toan
PC_DELETED="DELETED" # host da xoa

class PC():
    def __init__(self, code, status, bill_id, merchant_url):
        self.code = code
        self.status = status
        self.bill_id = bill_id
        self.merchant_url = merchant_url
    def to_json(self):
        return {
            "code": self.code, 
            "status": self.status,
            "bill_id": self.bill_id, 
            "merchant_url": self.merchant_url
        }
    

# thePC1 = PC(code="22345678", status=PC_EMPRY, bill_id="bill123", merchant_url="http://localhost:5000")
# thePC2 = PC(code="22345679", status=PC_PAYED, bill_id="bill124", merchant_url="http://localhost:5000")
# thePC3 = PC(code="22345670", status=PC_DELETED, bill_id="bill125", merchant_url="http://localhost:5000")

# PC_ALLOC = [
#     thePC1,
#     thePC2,
#     thePC3,
# ]

def get_pc(pc):
    for i in PC_ALLOC:
        if i.code == pc:
            return i
    return None
            
@app.route('/')
def home():
    return "Pop"

@app.route('/pc', methods=["POST"])
def ppc():
    """merchant register payment code """
    form = request.get_json()    
    # data = form.get("data")
    bill_id = form.get("bill_id")
    price = form.get("price")    
    callback_url = form.get("callback_url")
    
    result = PaymentCode.alloc_pc(bill_id, price, callback_url)
    return make_response(jsonify(result))


@app.route('/pc/<string:pc>', methods=["GET"])
def get_ppc(pc):
    """ client scan bill
    1. return ppc status/bill info
    """
    # pc = get_pc(pc)
    # merchant = {"id":"cfnguyen", "url": "http://localhost:5000"}
    # bill_of_pcc =  "bill123"
    code = PaymentCode.get_pc(pc)
    if code:
        r = requests.get(code)           
        res = {
            "pc": pc,
            "bill": r.json() 
        }
        return make_response(jsonify( res ))

    abort(404)

@app.route('/payment', methods=["POST"])
def payment() :
    """ client payment for bill """
    # check 
    form = request.get_json()
    code = form.get("code")    
    bill_id = form.get("bill_id")    
    
    pc = get_pc(code)
    if pc:
        # check all here
        if pc.status == PC_EMPRY:
            return jsonify( pc.to_json() )
        else:
            return make_response(jsonify(pc.to_json()), 406)
    
    return abort(404)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='1234', debug=True)
