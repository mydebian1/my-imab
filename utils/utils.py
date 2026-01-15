from flask import current_app
from models import Companies

def get_company_by_id(id):
    company = Companies.query.filter_by(id=id).first()
    current_app.logger.info("company check by ID")
    return company

def get_company(company_name, company_email):
    company = Companies.query.filter_by(company_name=company_name, company_email=company_email).first()
    current_app.logger.info("company check by ID")
    return company
