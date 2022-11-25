from config import db
from sqlalchemy import *
from sqlalchemy.orm import *

from burger_order import BurgerOrder

class Client(db.Model):
	id = Column(Integer, primary_key = True, autoincrement = True)
	full_name = Column(String(50), nullable = True)
	child = relationship("order", secondary=BurgerOrder)
