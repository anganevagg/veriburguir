from src.database.base import Base
from sqlalchemy import *

class Complement(Base):
	id = Column(Integer, primary_key=True, autoincrement = True)
	name = Column(String(50), nullable = False)
	category_id = Column(Integer)
