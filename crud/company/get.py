from database import db
from controller.company.create import get_company_by_id
from models import Companies
from sqlalchemy.exc import IntegrityError

def get_company_id_crud(company_id):
    try: 
        get_company = get_company_by_id(company_id)
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
        Companies = Companies.query.with_entities(Companies.id, Companies.name).all()
        db.session.commit()
        return Companies
    
    except IntegrityError as error:
        print(f"error: {error}")
        raise error
    
    except Exception as error:
        raise error