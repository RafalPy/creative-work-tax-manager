from flask import Blueprint, jsonify, request
from app.models import db
from app.models.evidence import Evidence


evidence_bp = Blueprint('evidence', __name__)



@evidence_bp.route('/', methods=['GET'])
def get_evidence():
    evidence = db.session.query(Evidence).all()
    evidence_list = [e.to_dictionary() for e in evidence]
    return jsonify(evidence_list) #chat gtp zapytać jaka różnica z jsonify i bez

@evidence_bp.route('/<int:evidence_id>', methods=['GET'])
def get_evidence_by_id(evidence_id):
    evidence = db.session.get(Evidence, evidence_id)
    if not evidence:
        return jsonify({"error": "Evidence not found"}), 404
    return jsonify(evidence.to_dictionary())

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

@evidence_bp.route('/<int:evidence_id>', methods=['DELETE'])
def delete_evidence(evidence_id):
    evidence = db.session.get(Evidence, evidence_id)
    if not evidence:
        return jsonify({"error": "Evidence not found"}), 404

    db.session.delete(evidence)
    db.session.commit()
    return jsonify({"message": f"Evidence {evidence_id} deleted"}), 200

@evidence_bp.route('/<int:evidence_id>', methods=['PUT'])
def update_evidence(evidence_id):
    evidence = db.session.get(Evidence, evidence_id)
    if not evidence:
        return jsonify({"error": "Evidence not found"}), 404
    data = request.get_json()

    # Update fields if they exist in the payload
    evidence.name = data.get('name', evidence.name)
    evidence.description = data.get('description', evidence.description)
    evidence.date = data.get('date', evidence.date)

    db.session.commit()
    return jsonify({"message": f"Evidence {evidence_id} updated"}), 200

#curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Sample Evidence\",\"description\":\"This is a sample description.\",\"date\":\"2025-04-27\"}" http://127.0.0.1:5000/api/evidence/

