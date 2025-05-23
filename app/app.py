from ctypes import pydll

from flask import Flask, render_template
from app.api.evidence import evidence_bp
from app.api.ping import ping_blueprint
from app.models import db
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from app.api import ping
from app.models.evidence import Evidence

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    app.register_blueprint(evidence_bp, url_prefix='/api/evidence')
    app.register_blueprint(ping_blueprint)
    return app

app = create_app()



@app.route("/evidence/")
def return_evidence():
    evidence = db.session.query(Evidence).all()
    evidence_list = [e.to_dictionary() for e in evidence]
    return render_template("evidence.html", evidence_list= evidence_list)

@app.route("/add-evidence/")
def add_new_evidence():
    return render_template("form.html")

#flask --app app run --debug
#https://auth0.com/blog/developing-restful-apis-with-python-and-flask/