from database import db
from sqlalchemy import UniqueConstraint, Enum
from base import BaseModel
import enum

class DepartmentEnum(enum.Enum):
    Permanent = "Permanent"
    Probation = "Probation"
    Trainee = "Trainee"

class GenderEnum(enum.Enum):
    Male = "Male"
    Female = "Female"

class Companies(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, nullable=False)
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

    class Employee(BaseModel):
        id = db.Column(db.Integer, primary_key=True)
        employee_id = db.Column(db.Integer, nullable=False)
        employee_department = db.Column(Enum(DepartmentEnum), nullable=False, default=DepartmentEnum)
        employee_name = db.Column(db.String(100), nullable=False)
        employee_status = db.Column(db.String(50), nullable=False)
        employee_email = db.Column(db.String(150), nullable=False)
        employee_phone_number_main = db.Column(db.String(255), nullable=False)
        employee_phone_number_secondary = db.Column(db.String(255), nullable=False)
        employee_dob = db.Column(db.Date, nullable=False)
        employee_cnic = db.Column(db.String(255), nullable=False)
        employee_gender = db.Column(Enum(GenderEnum), nullable=False, default=GenderEnum)
        employee_address_permanent = db.Column(db.String(255), nullable=False)
        employee_address_current = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint("employee_email", name="unique_employee_email"),
        UniqueConstraint("employee_phone_number_main", name="unique_employee_phone_number_main"),
        UniqueConstraint("employee_cnic", name="unique_employee_cnic"),
    )
        
    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "employee_department": self.employee_department,
            "employee_name": self.employee_name,
            "employee_status": self.employee_status,
            "employee_email": self.employee_email,
            "employee_phone_number_main": self.employee_phone_number_main,
            "employee_phone_number_secondary": self.employee_phone_number_secondary,
            "employee_dob": self.employee_dob.isoformat(),
            "employee_cnic": self.employee_cnic,
            "employee_gender": self.employee_gender,
            "employee_address_permanent": self.employee_address_permanent,
            "employee_address_current": self.employee_address_current
        }
    
    @classmethod
    def to_dict_list(cls, employees):
        return [employee.to_dict() for employee in employees]


