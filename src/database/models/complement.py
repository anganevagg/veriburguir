from config import db
from sqlalchemy import *

class Complement(db.Model):
	id = Column(Integer, primary_key=True, autoincrement = True)
	name = Column(String(50), nullable = False)
	category_id = Column(Integer)

