from flask import Blueprint, render_template

root = Blueprint("root", __name__, static_folder="templates")

@root.route("/")
def index():
	return render_template('index.html')