from src.database.base import Base
from sqlalchemy import *

class Burger(Base):
	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable = False)