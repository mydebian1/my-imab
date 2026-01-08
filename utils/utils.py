from flask import current_app
from models import Companies

def get_company_by_name(name):
    company = Companies.query.filter_by(company_name=name).first()
    current_app.logger.info("company check by name")
    return company
