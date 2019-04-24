from sqlalchemy import Column, Integer, String
# from yourapplication.database import Base
import re
from popsetting import db
from sqlalchemy import func

PC_PATTERN = re.compile("^[a-z2-9]{8}$")
# 2-9a-z
# 22222222, 22222223, 22222224

PC_TABLE = {
    '222':1,
    '223':1    
}
class PaymentCode():
    # __tablename__ = '22222222'
    # code = Column(String(8), primary_key=True)
    # status = Column(String(50))
    # bill_id = Column(String(120))
    # price = Column(String(120))
    # merchain_url = Column(String(120))
    # max = Column(Integer, defautl=1) # -1 = unlimit
    

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
        # result = db.session.execute("SELECT alloc_pc('%s', '%s', '%s', '%s')"%(tblname, bill_id, price, callback_url)).fetchall()
        # result = db.session.execute("select public.alloc_pc('c222', 'bill_123', '100', 'abc.com');").fetchone()
        # print(result)
        return result[0]        
        
    @classmethod
    def get_pc(cls, code):
        code = code.lower()
        if not PC_PATTERN.match(code):
            raise Exception("bad pc code")
        
        table = code[:3]
        if PC_TABLE.get(table) is None:
            raise Exception("invalid code")
        
        sql = text("select * from %s where code='%s' limit 1"%(table, code))
        result = db.engine.execute(sql)
        if len(result) > 0:
            return result[0]
        return None

                