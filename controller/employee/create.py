from flask import Blueprint, request, jsonify, current_app
from crud.employee.create import create_employee_crud
from utils.utils import get_employee
from sqlalchemy.exc import IntegrityError
from schemas.employee import CreateEmployeeRequest, EmployeeResponse
from auth import require_auth

employee_create_bp = Blueprint("employee_create_bp", __name__, url_prefix="/employee")

@employee_create_bp.route("/create", methods=["POST"])
@require_auth
def create_employee():

    data = CreateEmployeeRequest(request.json)
    valid, message = data.is_valid()

    current_app.logger.info(f"Checking Data By Employee Name And Email {data.employee_name, data.employee_email, data.employee_cnic}")

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400

    
    employee = get_employee(data.employee_name, data.employee_email, data.employee_cnic)

    if employee:
        current_app.logger.error("Employee Already Exists")
        return jsonify({
                "code": "EMPLOYEE_ALREADY_EXISTS",
                "message": f"This Employee Name {data.employee_name} And {data.employee_email} And {data.employee_cnic} Are Already Exists, Please Try Again With New Of Them"
        }), 403

    try:
        new_employee = create_employee_crud(
            employee_company_id = data.employee_company_id,
            employee_department = data.employee_department,
            employee_name = data.employee_name,
            employee_status = data.employee_status,
            employee_email = data.employee_email,
            employee_phone_number_main = data.employee_phone_number_main,
            employee_phone_number_secondary = data.employee_phone_number_secondary,
            employee_dob = data.employee_dob,
            employee_cnic = data.employee_cnic,
            employee_gender = data.employee_gender,
            employee_address_permanent = data.employee_address_permanent,
            employee_address_current = data.employee_address_current,
            employee_basic_salary = data.employee_basic_salary
        )

        return jsonify({
            "code": "EMPLOYEE_CREATED",
            "data": EmployeeResponse(new_employee).to_dict()
        }), 201

    except IntegrityError as e:
        current_app.logger.error(f"Integrity Error {e}")
        return jsonify({"code": "INTEGRITY_ERROR", "message": str(e)}), 409

    except Exception:
        current_app.logger.error("Exception Error")
        return jsonify({"code": "ERROR"}), 500