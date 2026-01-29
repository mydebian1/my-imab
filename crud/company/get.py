from database import db
from utils.utils import get_company_by_id
from models import Companies
from sqlalchemy.exc import IntegrityError

def get_company_id_crud(id):
    try: 
        get_company = get_company_by_id(id)
        print(get_company)
        return get_company
    
    except IntegrityError as error:
        print(f"error: {error}")
        return error
    
    except Exception as error:
        print(f"error: {error}")
        return error


def get_all_company_crud():
    try: 
        get_company = Companies.query.all()
        db.session.commit()
        return get_company
    
    except IntegrityError as error:
        print(f"error: {error}")
        return error
    
    except Exception as error:
        print(f"error: {error}")
        return error
    
def get_short_company_crud():
    try:
        companies = Companies.query.with_entities(Companies.id, Companies.company_name, Companies.company_email, Companies.company_joined).all()
        db.session.commit()
        return companies
    
    except IntegrityError as error:
        print(f"error: {error}")
        raise error
    
    except Exception as error:
        raise error