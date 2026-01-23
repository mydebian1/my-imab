from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll.update import update_payroll_crud
from utils.utils import get_payroll_by_id
from sqlalchemy.exc import IntegrityError
from schemas.payroll import UpdatePayrollRequest, PayrollResponse

payroll_update_bp = Blueprint("payroll_update_bp", __name__, url_prefix="/payroll")

@payroll_update_bp.route("/update", methods=["PUT"])
def update_payroll():

    data = UpdatePayrollRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400
    
    if not data.has_any_updates():
        return jsonify({
            "code": "DATA_MISSING", 
            "error": "Required fields for data update not provided"
            }), 400
    
    payroll = get_payroll_by_id(data.id)

    if not payroll:
        return jsonify({
            "code": "Payroll_Not_Found", 
            "error": "Required fields for data update not provided"
        }), 404

    try:
        updated_payroll = update_payroll_crud(
            id=data.id,
            employee_contract_hours=data.employee_contract_hours,
            employee_rota_hours=data.employee_rota_hours,
            employee_worked_hours=data.employee_worked_hours,
            employee_lates=data.employee_lates,
            employee_early=data.employee_early,
            employee_leaves=data.employee_leaves
        )

        return jsonify({
            "code": "Payroll_Updated",
            "data": PayrollResponse(updated_payroll).to_dict()
        }), 403
           
    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for {data.id} updation, please try again {error}"
        })
        
    except Exception:
        current_app.logger.error(f"Exception Error Occured")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for {data.id} updation, please try again"
        })
    
    


