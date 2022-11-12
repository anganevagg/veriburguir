from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

"""
app definition
"""
app = Flask(__name__)

"""
app config
"""

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/Veriburguir"
app.debug = True

"""
db definition
"""
db = SQLAlchemy(app)
db.init_app(app)

class Client(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	full_name = db.Column(db.String(50), nullable = True)

class Complement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable = False)
	category_id = db.Column(db.Integer)

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey("client.id"),  nullable = False)

class Burger(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable = False)

with app.app_context():
    db.create_all()

@app.route("/", methods = ['GET'])
def index():
	db.reflect()
	return render_template('index.html')

@app.route("/api/order", methods = ['GET'])
@app.route("/api/order/<id>", methods = ['GET', 'POST', 'DELETE', 'UPDATE'])
def orders(id=None):
	if(id):
		return id
	
	return []