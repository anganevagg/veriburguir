from database import db
from sqlalchemy import *
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Burger(db.Model):
	__tablename__ = "Burger"
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	price = Column(DECIMAL(2), nullable = False)
	selled = Column(Integer, default = 0)

class BurguerSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Burger
		include_fk = True
		load_instance = True
