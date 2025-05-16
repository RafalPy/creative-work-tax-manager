from ctypes import pydll

from flask import Flask
from app.api.evidence import evidence_bp
from app.api.ping import ping_blueprint
from app.models import db
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from app.api import ping

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    app.register_blueprint(evidence_bp, url_prefix='/evidence')
    app.register_blueprint(ping_blueprint)
    return app

app = create_app()

#flask --app app run --debug
#https://auth0.com/blog/developing-restful-apis-with-python-and-flask/