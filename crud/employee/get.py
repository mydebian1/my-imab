from database import db
from utils.utils import get_employee_by_id
from models import Employee
from sqlalchemy.exc import IntegrityError

def get_employee_id_crud(id):
    try: 
        get_employee = get_employee_by_id(id)
        print(get_employee)
        return get_employee
    
    except IntegrityError as error:
        print(f"error: {error}")
        return error
    
    except Exception as e:
        print(f"error: {e}")
        return e


def get_all_employee_crud():
    try: 
        get_employee = Employee.query.all()
        db.session.commit()
        return get_employee
    
    except IntegrityError as error:
        print(f"error: {error}")
        return error
    
    except Exception as error:
        print(f"error: {error}")
        return error
    
def get_short_employee_crud():
    try:
        employees = Employee.query.with_entities(Employee.id, Employee.employee_name, Employee.employee_email, Employee.employee_status).all()
        db.session.commit()
        return employees
    
    except IntegrityError as error:
        print(f"error: {error}")
        raise error
    
    except Exception as error:
        raise error