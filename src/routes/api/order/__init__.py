from flask import request, Blueprint
from database.models.order import Order
from config import app
from marshmallow import Schema, fields

class OrderCreateValidator(Schema):
	burguer = fields.List(fields.Int())
	complement = fields.List(fields.Int())

order = Blueprint("orders", __name__, static_folder="templates")

@app.route("/api/order", methods = ['GET', 'POST'])
@app.route("/api/order/<id>", methods = ['GET', 'DELETE', 'UPDATE'])
def orders(id=None):
	if request.method == "GET":
		# /api/order/<id> READ BY ID
		if(id):
			result = Order.query.get({"id": id})
			if(result):
				return result
			return "Order not found"
		
		# /api/order READ ALL
		result = Order.query.all()
		return result
	
	# /api/order CREATE
	if request.method == "POST":
		content = request.get_json()
		if(content['data']):
			return "correct"
		return "POST"
	
	# /api/order/<id> UPDATE
	if request.method == "PUT":
		return "PUT"