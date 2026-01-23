from database import db
from utils.utils import get_payroll_by_id
from models import Payroll, Employee, Companies
from sqlalchemy.exc import IntegrityError

def get_payroll_id_crud(id):
    try: 
        get_payroll = get_payroll_by_id(id)
        print(get_payroll)
        return get_payroll
    
    except Exception as error:
        print(f"error: {error}")
        return error


def get_all_payroll_crud():
    try:  
        get_payroll = Payroll.query.all()
        db.session.commit()
        return get_payroll
    
    except Exception as error:
        print(f"error: {error}")
        raise error
    
def get_short_payroll_crud():
    try:
        payrolls = Payroll.query.with_entities(Payroll.id, Payroll.batch_name, Employee.employee_name, Companies.company_name).all()
        db.session.commit()
        return payrolls
    
    except IntegrityError as error:
        print(f"error: {error}")
        raise error
    
    except Exception as error:
        raise error