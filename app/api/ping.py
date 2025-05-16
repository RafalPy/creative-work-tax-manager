from flask import Blueprint

ping_blueprint = Blueprint('pong', __name__)

@ping_blueprint.route("/")
def hello_world():
    return "Hello, World!"

