from datetime import date
from app.models import Base, engine, Session
from app.models import db
from app.models.evidence import Evidence
from app import app

session =Session()

# extract all evidence
evidence = session.query(Evidence).all()

#print evidence details

for element in evidence:
    print(f"ID {element.id} has name {element.name} is for {element.description} and created on {element.date}")

'''deleting query by id'''
session.query(Evidence).filter_by(id=4).delete()
session.commit()

help()