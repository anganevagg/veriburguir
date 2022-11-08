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

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
app.debug = True


"""
db definition
"""
db = SQLAlchemy(app)

@app.route("/", methods = ['GET'])
def index():
	db.reflect()
	return render_template('index.html')

@app.route("/api/order", methods = ['GET'])
@app.route("/api/order/<id>", methods = ['GET', 'POST', 'DELETE', 'UPDATE'])
def orders(id=None):
	if(id):
		return id
	return "orders"
