from flask import current_app
from models import Companies, Employee

def get_company_by_id(id):
    company = Companies.query.filter_by(id=id).first()
    current_app.logger.info("company check by ID")
    return company

def get_company(company_name, company_email):
    company = Companies.query.filter_by(company_name=company_name, company_email=company_email).first()
    current_app.logger.info("company check by Name and Email")
    return company

def get_employee_by_id(id):
    employee = Employee.query.filter_by(id=id).first()
    current_app.logger.info("Employee check by ID")
    return employee

def get_employee(employee_name, employee_email, employee_cnic):
    employee = Employee.query.filter_by(employee_name=employee_name, employee_email=employee_email, employee_cnic=employee_cnic).first()
    current_app.logger.info("Employee check by Name and Email")
    return employee

#Checking Enum Format 
def check_enum_format(value):
    return value.lower()
