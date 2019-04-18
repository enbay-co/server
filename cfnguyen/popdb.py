from sqlalchemy import Column, Integer, String
from yourapplication.database import Base

# 2-9a-z
# 22222222, 22222223, 22222224
class PCTable():
    # __tablename__ = '22222222'
    code = Column(String(8), primary_key=True)
    status = Column(String(50))
    bill_id = Column(String(120))
    price = Column(String(120))
    merchain_url = Column(String(120))

    @classmethod
    def get_pc(cls, code):
        
    # def __init__(self, name=None, email=None):
    #     self.name = name
    #     self.email = email

    # def __repr__(self):
    #     return '<User %r>' % (self.name)