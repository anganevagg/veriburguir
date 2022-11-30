from flask import request, Blueprint
from database import Order, OrderSchema
from database import db
from database import Item, ItemSchema

order = Blueprint("orders", __name__, static_folder="templates")

order_validator = OrderSchema()

@order.get('/')
def getAll():
	result = Order.query.all()
	print(OrderSchema(many=True).dump(result))
	return {
		"data": OrderSchema(many=True).dump(result)
	}
@order.get('/<int:id>')
def getOne(id: int):
	result = Order.query.get({"id": id})
	if(result):
		return {
			"data": OrderSchema().dump(result)
		}
	return {
		'error': "Order not found"
	}, 404

@order.post('/')
def create():
	items = request.json.get('items')
	order = Order()
	for item in items:
		order.items.append(Item.query.get({"id": item}))
		sum = 0
		for found_item in order.items:
			sum = sum + found_item.price
			found_item.selled = found_item.selled + 1
		order.total = sum
	db.session.add(order)
	db.session.commit()
	return {
		"message": "created"
	}