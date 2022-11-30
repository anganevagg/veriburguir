from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine
from sqlalchemy import *
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import backref
import marshmallow
from marshmallow_sqlalchemy.fields import Nested

db = SQLAlchemy()

OrderItem = db.Table('order_item', db.metadata,
	db.Column('order_id', db.ForeignKey('Order.id'), primary_key = True),
	db.Column('item_id', db.ForeignKey('Item.id'), primary_key = True)
)

class Item(db.Model):
	__tablename__ = "Item"
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	price = Column(DECIMAL(5, 2), nullable = False)
	selled = Column(Integer, default = 0)

class Order(db.Model):
	__tablename__ = "Order"
	id = Column(Integer, primary_key=True, autoincrement = True)
	total = Column(DECIMAL(5, 2), default=0)
	# client_id = Column(Integer, ForeignKey('client.id'))
	items = db.relationship("Item", secondary = OrderItem)

class ItemSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Item
		include_fk = True
		load_instance = True
		include_relationships = True
	

class OrderSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Order
		include_fk = True
		load_instance = True
		include_relationships = True
	items = Nested(ItemSchema, many=True)