from flask import current_app
from database import db
from models import Companies
from sqlalchemy.exc import IntegrityError

def create_company_crud(company_name, company_email, company_address, company_joined):
    current_app.logger.info("checking company crud 0")
    try:
        current_app.logger.info("checking company crud 1")

        create_company = Companies(
            company_name=company_name,
            company_email=company_email,
            company_address=company_address,
            company_joined=company_joined
        )

        current_app.logger.info("checking company crud 2")

        db.session.add(create_company)
        db.session.commit()

        return create_company

    except IntegrityError:
        raise

    except Exception:
        raise