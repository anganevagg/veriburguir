from config import app

from routes.root import root
from routes.api.order import order
from routes.api.complement import complement

app.register_blueprint(root, url_prefix = "/")
app.register_blueprint(order, url_prefix = "/api/order")
app.register_blueprint(complement, url_prefix = "/api/complement")

if __name__ == "__main__":
	app.run(debug=True)