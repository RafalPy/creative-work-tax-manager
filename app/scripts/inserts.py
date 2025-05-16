from datetime import date
from app.models import Base, engine, Session
from app.models import db
from app.models.evidence import Evidence

Base.metadata.create_all(engine)

#  generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()

# create evidence
new_evidence = Evidence("BLE BLE2", "BLE BLE BLE BLE2", date(2001, 12, 1))

# persists data
session.add(new_evidence)

# commit and close session
session.commit()
session.close()

