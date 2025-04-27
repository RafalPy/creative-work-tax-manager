from app.app import create_app
from app.models import db
from app.models.evidence import Evidence

# Initialize the app context
app = create_app()

# Start app context (useful when running outside of a route)
with app.app_context():
    def delete_evidence_by_id(evidence_id):
        evidence_to_delete = Evidence.query.filter(Evidence.id == evidence_id).first()

        if evidence_to_delete:
            db.session.delete(evidence_to_delete)
            db.session.commit()
            print(f"Evidence with ID {evidence_id} deleted.")
        else:
            print(f"No evidence found with ID {evidence_id}")

    # Call the function to delete evidence with ID 1 (or whichever ID you want)
    delete_evidence_by_id(3)