from config import app
from flask import Blueprint

complement = Blueprint("complements", __name__, static_folder="templates")

@app.route("/api/complement", methods = ['GET', 'POST'])
@app.route("/api/complement/<id>", methods = ['GET', 'DELETE', 'UPDATE'])
def complements(id=None):
 return "complements"