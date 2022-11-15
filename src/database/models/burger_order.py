from src.database.base import Base
from sqlalchemy import *

class BurgerOrder(Base):
	id = Column(Integer, primary_key = True, autoincrement = True)
	order_id = Column(Integer, ForeignKey('Order.id'), nullable = False)
	burger_id = Column(Integer, ForeignKey('Burger.id'), nullable = False)
