from database import db
from utils.utils import get_company_by_id
from sqlalchemy.exc import IntegrityError

def update_company_crud(id, company_name, company_email, company_address, company_joined):
    company = get_company_by_id(id)

    if not company:
        return company == False

    try:
        if id:
            company.id = id

        if company_name:
            company.company_name = company_name

        if company_email:
            company.company_email = company_email

        if company_address:
            company.company_address = company_address

        if company_joined:
            company.company_joined = company_joined

        db.session.commit()

        return company

    except IntegrityError:
        raise
    
    except Exception:
        raise