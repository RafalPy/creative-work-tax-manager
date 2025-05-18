from app.models import db

from app.models import Base

class Evidence(Base):
    __tablename__= 'evidence'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    date = db.Column(db.Date)

    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date

    def to_dictionary(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date
        }
    def __repr__(self):
        return f'<Evidence {self.name}>'