from config import db
from sqlalchemy import *

class BurgerOrder(db.Model):
	id = Column(Integer, primary_key = True, autoincrement = True)
	order_id = Column(Integer, ForeignKey('Order.id'), nullable = False)
	burger_id = Column(Integer, ForeignKey('Burger.id'), nullable = False)
