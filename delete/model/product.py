from appInitialize import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "product"
    
    productid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Float())
    state = db.Column(db.String(10), default="activo")
    created_at = db.Column(db.Date, default=datetime.now())    

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product :" \
               f"{self.name}"

db.create_all()
