from flask import current_app
from models import Companies, Employee, Payroll
from sqlalchemy.orm import joinedload

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

def get_payroll_by_id(id):
    payroll = Payroll.query.filter_by(id=id).first()
    current_app.logger.info("Payroll check by ID")
    return payroll

def get_payroll(employee_id, batch_name):

    payroll = (
        Payroll.query.options(
        joinedload(Payroll.employee),
        joinedload(Payroll.company)).filter_by(employee_id=employee_id, batch_name=batch_name).first()
    )

    return payroll

#Get hourly rate
def get_hourly_rate(basic_salary, contract_hours):
    return basic_salary / contract_hours

#Get over below
def get_over_below(worked_hours, contract_hours):
    return worked_hours - contract_hours

#Get score
def get_score(late, early, leaves):
    return 100 - (late * 10 + early * 5 + leaves * 15)

#Get addition
def get_addition(over_below, hourly_rate):
    if over_below > 0:
        return abs(over_below) * hourly_rate
    else:
        return 0

#Get deduction
def get_deduction(over_below, hourly_rate):
    if over_below < 0:
        return abs(over_below) * hourly_rate
    else:
        return 0

#Get gross
def get_gross(basic_salary, addition, deduction):
    return basic_salary + addition - deduction

#Get tax
def get_tax(gross):
    return gross * 0.15

#Get total net
def get_total_net(gross, tax):
    return gross - tax

#Get total net orion
def get_net_orion(gross):
    return gross

#Checking Enum Format 
def check_enum_format(value):
    return value.lower()



