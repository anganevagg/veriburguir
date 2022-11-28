from flask import Blueprint

complement = Blueprint("complements", __name__, static_folder="templates")

@complement.route("/", methods = ['GET', 'POST'])
@complement.route("/<id>", methods = ['GET', 'DELETE', 'UPDATE'])
def complements(id=None):
 return "complements"