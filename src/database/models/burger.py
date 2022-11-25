from config import db
from sqlalchemy import *

class Burger(db.Model):
	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable = False)