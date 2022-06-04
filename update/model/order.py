from appInitialize import db
from datetime import datetime 

class Order(db.Model):
    __tablename__ = "order"
    
    orderid = db.Column(db.Integer, primary_key=True)
    clientid = db.Column(db.Integer)
    productid = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default=1)
    total = db.Column(db.Float(), default=0)
    state = db.Column(db.String(10), default="pendiente")
    created_at = db.Column(db.Date, default=datetime.now())    

    def __init__(self, clientid, productid, quantity, total):
        self.clientid = clientid
        self.productid = productid
        self.quantity = quantity
        self.total = total

    def __str__(self):
        return f"Order :" \
               f"{self.total}"

db.create_all()
