import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                  # L1
app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://postgres:123@localhost/ebpc"
# app.config.from_object(os.environ['APP_SETTINGS'])     # L2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # L3
database = SQLAlchemy(app)                             # L4
db = database                                          # L5
