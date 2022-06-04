from appInitialize import db
from datetime import datetime 

class Client(db.Model):
    __tablename__ = "client"
    
    clientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    document = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(10), default="activo")
    created_at = db.Column(db.Date, default=datetime.now())    

    def __init__(self, name, document):
        self.name = name
        self.document = document

    def __str__(self):
        return f"Client :" \
               f"{self.name}"

db.create_all()
