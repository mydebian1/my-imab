from database import db
from models import Employee
from sqlalchemy.exc import IntegrityError

def delete_employee_crud(id):
    try:
        delete_query = Employee.query.filter_by(id=id).first()

        db.session.delete(delete_query)
        db.session.commit()

        return delete_query
    
    except IntegrityError:
        raise
        
    except Exception:
        raise