from flask import Flask
from app.api.users import users_bp
from app.api.evidence import evidence_bp
from app.models import db
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(evidence_bp, url_prefix='/evidence')
    return app



#flask --app app run --debug
#https://auth0.com/blog/developing-restful-apis-with-python-and-flask/