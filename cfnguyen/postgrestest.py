from flask import Flask
import os
import models as appmod 
from setting import app, db


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os
# from config import Config
# from sqlalchemy import update
from models import Result, User, Todo

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://postgres:123@localhost/wordcount_dev"
# # app.config.from_object(os.environ['APP_SETTINGS'])
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# from datetime import datetime
# from flask import Flask, request, flash, url_for, redirect, \
#      render_template
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://postgres:123@localhost/wordcount_dev"
# db = SQLAlchemy(app)

# from models import User

# def update_done(num):    
#     one = User.query.filter_by(id=2).first()
#     print(one.balance)
#     one.balance = 123
#     db.session.commit()
    
# connection = db.engine.connect()
# transaction = connection.begin()
        
import time

def bal():
    try:
        print("go get row")
        # one = User.query.filter_by(id=2).first()        
        # one = db.session.query(User).with_lockmode('update').filter_by(id=2).first()
        one = db.session.query(User).with_for_update(nowait=True, of=User).filter_by(id=2).first()
        print("see balance is %s"%one.balance)
        one.balance = one.balance + 1
        print("update to balance: %s" % one.balance)
        time.sleep(10)
        db.session.commit()
        print("commit of %s"%one.balance)
    except Exception as exc:
        # debugs an exception
        db.session.rollback()
        raise 
        
    
def balance(num):        
    try:
        # get current        
        one = User.query.filter_by(id=2).first()        
        one.balance = one.balance + num
        print(one.balance)
        time.sleep(10)
        db.session.commit()
        print("request finish")
        
        # u = User(id=2, balance=200)
        # db.session.add(u)
        # db.session.commit()
        
        # # first query.  a Connection is acquired
        # # from the Engine, and a Transaction
        # # started.
        # item1 = session.query(Item).get(1)

        # # second query.  the same Connection/Transaction
        # # are used.
        # item2 = session.query(Item).get(2)

        # # pending changes are created.
        # item1.foo = 'bar'
        # item2.bar = 'foo'

        # # commit.  The pending changes above
        # # are flushed via flush(), the Transaction
        # # is committed, the Connection object closed
        # # and discarded, the underlying DBAPI connection
        # # returned to the connection pool.
        # session.commit()
    except:
        # on rollback, the same closure of state
        # as that of commit proceeds.
        db.session.rollback()
        raise
    finally:
        # close the Session.  This will expunge any remaining
        # objects as well as reset any existing SessionTransaction
        # state.  Neither of these steps are usually essential.
        # However, if the commit() or rollback() itself experienced
        # an unanticipated internal failure (such as due to a mis-behaved
        # user-defined event handler), .close() will ensure that
        # invalid state is removed.
        db.session.close()
        # raise
        

@app.route('/add')
def add():
    todo = Todo('title', 'text')
    db.session.add(todo)
    db.session.commit()
    return "hello"

@app.route('/')
def upd():
    bal()
    return "hello"


if __name__ == '__main__':
    app.run()
