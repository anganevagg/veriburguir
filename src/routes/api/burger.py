from flask import request, Blueprint
from database.models.burger import Burger, BurguerSchema
from database import db

burger = Blueprint("burgers", __name__, static_folder="templates")


@burger.get('/')
def getAll():
	result = Burger.query.all()
	return {
		"data": BurguerSchema(many=True).dump(result)
	}

@burger.get('/<int:id>')
def getOne(id: int):
	result = Burger.query.get({"id": id})
	print(result)
	if(result):
		return {
			"data": BurguerSchema().dump(result)
		}
	return {
		'error': "Order not found"
	}, 404

@burger.post('/')
def create():
	errors = BurguerSchema().validate(request.get_json(), session = db.session)
	if errors:
		return {
			"errors": errors
		}
	name = request.json.get('name')
	price = request.json.get('price')
	order = Burger(name = name, price = price)
	db.session.add(order)
	db.session.commit()
	return {
		"message": "created"
	}, 200
@burger.delete("/<int:id>")
def delete(id):
	burger = Burger.query.get({"id": id})
	if burger:
		burger.delete()
		return {
			"message": "success"
		}, 200
	return {
		"error": "burguer not found"
	}, 400