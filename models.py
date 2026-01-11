from database import db
from sqlalchemy import UniqueConstraint, CheckConstraint, Enum
from base import BaseModel


class Companies(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, nullable=True)
    company_name = db.Column(db.String(150), nullable=False)
    company_email = db.Column(db.String(255), nullable=False)
    company_joined = db.Column(db.Date, nullable=False)
    company_address = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "company_name": self.company_name,
            "company_email": self.company_email,
            "company_joined": self.company_joined.isoformat(),
            "company_address": self.company_address
        }

    
    @classmethod
    def to_dict_list(cls, companies):
        return [company.to_dict() for company in companies]


