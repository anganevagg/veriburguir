from database import db
from sqlalchemy import *
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.models.burger import Burger

BurgerOrder = db.Table('burger_order', db.metadata,
	db.Column('order_id', db.Integer, db.ForeignKey('Order.id'), primary_key = True),
	db.Column('burger_id', db.Integer, db.ForeignKey('Burger.id'), primary_key = True)
)

class Order(db.Model):
	__tablename__ = "Order"
	id = Column(Integer, primary_key=True, autoincrement = True)
	total = Column(DECIMAL(2), default=0)
	# client_id = Column(Integer, ForeignKey('client.id'))
	burguers = db.relationship(Burger, secondary = BurgerOrder)

class OrderSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Order
		include_fk = True
		load_instance = True
		include_relationships = True
