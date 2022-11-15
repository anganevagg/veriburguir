from src.database.base import Base
from sqlalchemy import *

class Client(Base):
	id = Column(Integer, primary_key = True, autoincrement = True)
	full_name = Column(String(50), nullable = True)
