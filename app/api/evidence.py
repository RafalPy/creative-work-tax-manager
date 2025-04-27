from flask import Blueprint, jsonify, request
from app.models import db
from app.models.evidence import Evidence

evidence_bp = Blueprint('evidence', __name__)



@evidence_bp.route('/', methods=['GET'])
def get_evidence():
    evidence = db.session.query(Evidence).all()
    evidence_list = [e.to_dict() for e in evidence]
    return jsonify(evidence_list) #chat gtp zapytać jaka różnica z jsonify i bez

@evidence_bp.route('/', methods=['POST'])
def add_evidence():
    data = request.get_json()
    new_evidence = Evidence(
        name=data['name'],
        description=data['description'],
        date=data['date']
    )
    db.session.add(new_evidence)
    db.session.commit()
    return jsonify({'id': new_evidence.id}), 201


#curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Sample Evidence\",\"description\":\"This is a sample description.\",\"date\":\"2025-04-27\"}" http://127.0.0.1:5000/evidence/
