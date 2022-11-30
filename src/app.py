
from routes.root import root
from routes.api.order import order
from routes.api.item import item

from flask import Flask
from database import db

from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/Veriburguir"

db.init_app(app)
CORS(app, resources={r"/*": {"origins": "*"}})
Migrate(app, db)


app.register_blueprint(root, url_prefix = "/")
app.register_blueprint(order, url_prefix = "/api/orders")
app.register_blueprint(item, url_prefix = "/api/items")


if __name__ == "__main__":
	app.run(debug=True, port=8000)