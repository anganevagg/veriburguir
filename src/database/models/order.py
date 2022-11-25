from config import db
from sqlalchemy import *

class Order(db.Model):
	id = Column(Integer, primary_key=True, autoincrement = True)
	client_id = Column(Integer, ForeignKey('client.id'))