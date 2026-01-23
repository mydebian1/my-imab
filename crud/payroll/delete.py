from database import db
from models import Payroll
from sqlalchemy.exc import IntegrityError

def delete_payroll_crud(id):
    try:
        delete_query = Payroll.query.filter_by(id=id).first()

        db.session.delete(delete_query)
        db.session.commit()

        return delete_query
    
    except IntegrityError:
        raise

    except Exception:
        raise