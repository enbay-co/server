from sqlalchemy import Column, Integer, String
import requests
# from yourapplication.database import Base
import re
from popsetting import db
from sqlalchemy import func

PC_PATTERN = re.compile("^[a-z2-9]{8}$")
# 2-9a-z
# 22222222, 22222223, 22222224

PC_TABLE = {
    'c222':1,
    'c223':1    
}
class PaymentCode():
    # __tablename__ = '22222222'
    # code = Column(String(8), primary_key=True)
    # status = Column(String(50))
    # bill_id = Column(String(120))
    # price = Column(String(120))
    # merchain_url = Column(String(120))
    # max = Column(Integer, defautl=1) # -1 = unlimit
    
    def __init__(self, code, bill_id, price, callback_url, status):
        self.code = code
        self.bill_id = bill_id
        self.price = price
        self.callback_url = callback_url
        self.status = status
        
    def setStatus(self, status):        
        tbl = 'c'+self.code[:3]
        
        sql = "update %s set status=%s where code='%s'"%(tbl, status, self.code)
        result = db.engine.execute(sql)
        db.session.commit()
        self.status = status
        
    def to_json(self):
        return {
            "code": self.code,
            "bill_id": self.bill_id,
            "price": self.price,
            "callback_url": self.callback_url,
            "status": self.status
        }
        
    @classmethod
    def alloc_pc(cls, bill_id, price, callback_url):
        """ merchant request a payment code
        """
        # sql = text("update c223 set status=1 where code=(select code from c223 where status=0 ORDER BY random() limit 1 for UPDATE  SKIP LOCKED)")
        
        tblname = 'c222'
        params = {"tblname": tblname, "bill_id": bill_id, "price": price, "callback_url": callback_url}
        # result = db.session.execute('alloc_pc :tblname, :bill_id, :price, :callback_url', params)
        # result = db.session.execute("select alloc_pc(?, ?, ?, ?)", params).fetchall()
        # result = db.session.func("alloc_pc", [tblname, bill_id, price, callback_url])
        
        result = db.session.query(func.alloc_pc(tblname, bill_id, price, callback_url)).all()
        db.session.commit()
        # result = db.session.execute("SELECT alloc_pc('%s', '%s', '%s', '%s')"%(tblname, bill_id, price, callback_url)).fetchall()
        # result = db.session.execute("select public.alloc_pc('c222', 'bill_123', '100', 'abc.com');").fetchone()
        # print(result)
        return result[0]        
        
    @classmethod
    def get(cls, code):
        code = code.lower()
        if not PC_PATTERN.match(code):
            raise Exception("bad pc code")
        
        table = 'c'+code[:3]
        if PC_TABLE.get(table) is None:
            raise Exception("invalid code")
        
        sql = "select * from %s where code='%s' limit 1"%(table, code)
        # print(sql)
        result = db.engine.execute(sql)
        row = result.fetchone()
        if row:
            plo = PaymentCode(code=row["code"], bill_id=row["bill_id"], price=row["price"], callback_url=row["callback_url"], status=row["status"])
            return plo
        # if len(result) > 0:
        #     return result[0]
        return None

                