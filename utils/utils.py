from flask import current_app
from models import Companies

def get_company_by_id(company_id):
    company = Companies.query.filter_by(company_id=company_id).first()
    current_app.logger.info("company check by ID")
    return company
