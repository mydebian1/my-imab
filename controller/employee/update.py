from flask import Blueprint, Flask, request, jsonify, current_app
from crud.employee.update import update_employee_crud
from utils.utils import get_employee_by_id
from sqlalchemy.exc import IntegrityError
from schemas.employee import UpdateEmployeeRequest, EmployeeResponse
from auth import require_auth

employee_update_bp = Blueprint("employee_update_bp", __name__, url_prefix="/employee")


@employee_update_bp.route("/update", methods=["PUT"])
@require_auth
def update_require_employee():

    data = UpdateEmployeeRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400

    if not data.has_any_updates():
        return jsonify({
            "code": "DATA_MISSING", 
            "error": "Required fields for data update not provided"
            }), 400
    
    employee = get_employee_by_id(data.id)

    if not employee:
        current_app.logger.error(f"Error. {employee}")
        return jsonify({
            "code": "EMPLOYEE_NOT_FOUND", 
            "error": "Required fields for data update not provided"
        }), 404

    try:
        employee = update_employee_crud(
            id=data.id,
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
            employee_address_current = data.employee_address_current
        )

        return jsonify({
            "code": "Employee_Updated",
            "data": EmployeeResponse(employee).to_dict()
        }), 200
    

    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for '{data.id}' creation, please try again {error}"
        })
    
        
    except Exception:
        current_app.logger.error("Exceptional Error Occured")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{data.id}' creation, please try again"
        })
    

