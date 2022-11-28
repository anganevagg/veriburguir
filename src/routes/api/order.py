from flask import request, Blueprint
from database.models.order import Order, OrderSchema
from database import db

order = Blueprint("orders", __name__, static_folder="templates")

order_validator = OrderSchema()

@order.get('/')
def getAll():
	result = Order.query.all()
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
	burguers = request.json.get('burguers')
	# complements = request.json.get('complements')

	if burguers is None:
		burguers=[]
	if complements is None:
		complements = []
	order = Order(burguers = burguers, complements = complements)
	db.session.add(order)