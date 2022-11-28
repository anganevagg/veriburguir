
from routes.root import root
from routes.api.order import order
from routes.api.complement import complement
from routes.api.burger import burger

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
app.register_blueprint(complement, url_prefix = "/api/complements")
app.register_blueprint(burger, url_prefix = "/api/burgers")


if __name__ == "__main__":
	app.run(debug=True, port=8000)