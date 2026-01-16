from flask import Blueprint, Flask, request, jsonify, current_app
from utils.utils import get_employee_by_id
from crud.employee.delete import delete_employee_crud
from sqlalchemy.exc import IntegrityError
from schemas.employee import DeleteEmployeeRequest

employee_delete_bp = Blueprint("employee_delete_bp", __name__, url_prefix="/employee")


@employee_delete_bp.route("/delete", methods=["POST"])
def delete_employee():

    data = DeleteEmployeeRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400
    
    employee_delete = get_employee_by_id(data.id)

    if not employee_delete:
        current_app.logger.info("Employee Doesnt Exist")
        return jsonify({
            "CODE": "EMPLOYEE_DOESNT_EXIST",
            "message": "Employee Doesnt Exist, Please Enter a Valid ID"
        })

    try:
        delete = delete_employee_crud(id=data.id)

        if delete:
            return jsonify({
                "CODE": "EMPLOYEE_DELETED",
                "message": f"Employee '{data.id}' is Deleted"
            }), 200
        
    except IntegrityError as error:
        current_app.logger.error(f"Error: {error}")
        return jsonify({
            "code": "IntegrityError",
            "message": f"IntegrityError Error Occured for Employee {data.id} deletion {error}"
    })

    except Exception:
        current_app.logger.error("Exception Error")
        return jsonify({
            "code": "EXCEPTION",
            "message": f"Exception Error Occured For Employee {data.id} Deletion!"
        })