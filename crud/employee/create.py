from database import db
from models import Employee
from sqlalchemy.exc import IntegrityError
from utils.utils import check_enum_format


def create_employee_crud(employee_id, employee_department, employee_name, employee_status, employee_email, employee_phone_number_main, employee_phone_number_secondary, employee_dob, employee_cnic, employee_gender, employee_address_permanent, employee_address_current):
    try:
        create_employee = Employee(
            employee_id = employee_id,
            employee_department = check_enum_format(employee_department),
            employee_name = employee_name,
            employee_status = check_enum_format(employee_status),
            employee_email = employee_email,
            employee_phone_number_main = employee_phone_number_main,
            employee_phone_number_secondary = employee_phone_number_secondary,
            employee_dob = employee_dob,
            employee_cnic = employee_cnic,
            employee_gender = check_enum_format(employee_gender),
            employee_address_permanent = employee_address_permanent,
            employee_address_current = employee_address_current
        )
        
        db.session.add(create_employee)
        db.session.commit()

        return create_employee

    except IntegrityError:
        raise

    except Exception:
        raise