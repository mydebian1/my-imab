from database import db
from sqlalchemy import UniqueConstraint, CheckConstraint, Enum
from sqlalchemy.orm import relationship
from datetime import date
from base import BaseModel
import enum

class DepartmentEnum(enum.Enum):
    hr = "hr"
    accounts = "accounts"
    tech = "tech"
    guest = "guest"

class StatusEnum(enum.Enum):
    permanent = "permanent"
    probation = "probation"
    trainee = "trainee"

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"

class Login(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)


    __table_args__ = (
        UniqueConstraint("username", name="unique_employee_username"),
        CheckConstraint("length(username) > 6", name="check_username_min_length"),
        CheckConstraint("length(password) > 8", name="check_password_min_length"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "username": self.username,
            "password": self.password,
        }
    
    @classmethod
    def to_dict_list(cls, logins):
        return [login.to_dict() for login in logins]


class Companies(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), nullable=False)
    company_email = db.Column(db.String(255), nullable=False)
    company_joined = db.Column(db.Date, nullable=False)
    company_address = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint("company_email", name="unique_company_email"),
    )
    
    def to_dict(self):
        return {
            "id": self.id,
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
    employee_company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    employee_department = db.Column(Enum(DepartmentEnum, name="employee_department_enum"), nullable=False,)
    employee_name = db.Column(db.String(100), nullable=False)
    employee_status = db.Column(Enum(StatusEnum, name="employee_status_enum"), nullable=False)
    employee_email = db.Column(db.String(150), nullable=False)
    employee_phone_number_main = db.Column(db.String(255), nullable=False)
    employee_phone_number_secondary = db.Column(db.String(255), nullable=False)
    employee_dob = db.Column(db.Date, nullable=False)
    employee_cnic = db.Column(db.String(255), nullable=False)
    employee_gender = db.Column(Enum(GenderEnum, name="employee_gender"), nullable=False)
    employee_address_permanent = db.Column(db.String(255), nullable=False)
    employee_address_current = db.Column(db.String(255), nullable=False)
    employee_basic_salary = db.Column(db.Integer, nullable=False)
    

    __table_args__ = (
        UniqueConstraint("employee_email", name="unique_employee_email"),
        UniqueConstraint("employee_phone_number_main", name="unique_employee_phone_number_main"),
        UniqueConstraint("employee_cnic", name="unique_employee_cnic"),
    )
        
    def to_dict(self):
        return {
            "id": self.id,
            "employee_company_id": self.employee_company_id,
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
            "employee_address_current": self.employee_address_current,
            "employee_basic_salary": self.employee_basic_salary
        }
    
    @classmethod
    def to_dict_list(cls, employees):
        return [employee.to_dict() for employee in employees]
    

class Payroll(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    batch_name = db.Column(db.Integer, nullable=False)
    batch_status = db.Column(db.String, nullable=False)
    employee_basic_salary = db.Column(db.Integer, nullable=False)
    employee_hourly_rate = db.Column(db.Integer, nullable=False)
    employee_contract_hours = db.Column(db.Float, nullable=False)
    employee_rota_hours = db.Column(db.Float, nullable=False)
    employee_worked_hours = db.Column(db.Float, nullable=False)
    employee_net_hours = db.Column(db.Float, nullable=False)
    employee_over_below = db.Column(db.Float, nullable=False)
    employee_lates = db.Column(db.Integer, nullable=False)
    employee_early = db.Column(db.Integer, nullable=False)
    employee_leaves = db.Column(db.Integer, nullable=False)
    employee_score = db.Column(db.Integer, nullable=False)
    total_addition = db.Column(db.Integer, nullable=False)
    total_deduction = db.Column(db.Integer, nullable=False)
    total_gross = db.Column(db.Integer, nullable=False)
    total_tax = db.Column(db.Integer, nullable=False)
    total_net_employee = db.Column(db.Integer, nullable=False)
    total_net_orion = db.Column(db.Integer, nullable=False)

    employee = relationship('Employee', foreign_keys=[employee_id])
    company = relationship('Companies', foreign_keys=[company_id])

    __table_args__ = (
        UniqueConstraint("employee_id", "batch_name", name="unique_employee_id_batch_name"),
        CheckConstraint("employee_basic_salary >= 0", name="min_employee_basic_salary_check"),
        CheckConstraint("employee_hourly_rate >= 0", name="min_employee_hourly_rate_check"),
        CheckConstraint("employee_contract_hours >= 0", name="min_employee_contract_hours_check"),
        CheckConstraint("employee_rota_hours >= 0", name="min_employee_rota_hours_check"),
        CheckConstraint("employee_worked_hours >= 0", name="min_employee_worked_hours_check"),
        CheckConstraint("employee_net_hours >= 0", name="min_employee_net_hours_check"),
        CheckConstraint("employee_lates >= 0", name="min_employee_lates_check"),
        CheckConstraint("employee_early >= 0", name="min_employee_early_check"),
        CheckConstraint("employee_leaves >= 0", name="min_employee_leaves_check"),
        CheckConstraint("employee_score >= 0", name="min_employee_score_check"),
        CheckConstraint("total_addition >= 0", name="min_total_addition_check"),
        CheckConstraint("total_deduction >= 0", name="min_total_deduction_check"),
        CheckConstraint("total_gross >= 0", name="min_total_gross_check"),
        CheckConstraint("total_tax >= 0", name="min_total_tax_check"),
        CheckConstraint("total_net_employee >= 0", name="min_total_net_employee_check"),
        CheckConstraint("total_net_orion >= 0", name="min_total_net_orion_check"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "employee_id": self.employee_id,
            "batch_name": self.batch_name,
            "batch_status": self.batch_status,
            "employee_basic_salary": self.employee_basic_salary,
            "employee_hourly_rate": self.employee_hourly_rate,
            "employee_contract_hours": self.employee_contract_hours,
            "employee_rota_hours": self.employee_rota_hours,
            "employee_worked_hours": self.employee_worked_hours,
            "employee_net_hours": self.employee_net_hours, 
            "employee_over_below": self.employee_over_below,
            "employee_lates": self.employee_lates,
            "employee_early": self.employee_early,
            "employee_leaves": self.employee_leaves,
            "employee_score": self.employee_score,
            "total_addition": self.total_addition,
            "total_deduction": self.total_deduction,
            "total_gross": self.total_gross,
            "total_tax": self.total_tax,
            "total_net_employee": self.total_net_employee,
            "total_net_orion": self.total_net_orion
        }
    
    @classmethod
    def to_dict_list(cls, payrolls):
        return [payroll.to_dict() for payroll in payrolls]



