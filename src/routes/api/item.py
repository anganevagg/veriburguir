from flask import request, Blueprint
from database import Item, ItemSchema
from database import db

item = Blueprint("items", __name__, static_folder="templates")


@item.get('/')
def getAll():
	result = Item.query.all()
	return {
		"data": ItemSchema(many=True).dump(result)
	}

@item.get('/<int:id>')
def getOne(id: int):
	result = Item.query.get({"id": id})
	print(result)
	if(result):
		return {
			"data": ItemSchema().dump(result)
		}
	return {
		'error': "Order not found"
	}, 404

@item.post('/')
def create():
	errors = ItemSchema().validate(request.get_json(), session = db.session)
	if errors:
		return {
			"errors": errors
		}
	name = request.json.get('name')
	price = request.json.get('price')
	order = Item(name = name, price = price)
	db.session.add(order)
	db.session.commit()
	return {
		"message": "created"
	}, 200
@item.delete("/<int:id>")
def delete(id):
	item = Item.query.get({"id": id})
	if item:
		item.delete()
		return {
			"message": "success"
		}, 200
	return {
		"error": "item not found"
	}, 400