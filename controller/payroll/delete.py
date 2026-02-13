from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll.delete import delete_payroll_crud
from utils.utils import get_payroll_by_id
from sqlalchemy.exc import IntegrityError
from schemas.payroll import DeletePayrollRequest
from auth import require_auth

payroll_delete_bp = Blueprint("payroll_delete_bp", __name__, url_prefix="/payroll")

@payroll_delete_bp.route("/delete", methods=["POST"])
@require_auth
def delete_payroll():

    data = DeletePayrollRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400
    
    payroll_delete = get_payroll_by_id(data.id)

    if not payroll_delete:
        current_app.logger.error(f"Payroll Error. {payroll_delete}")
        return jsonify({
            "code": "Payroll_Desnt_Exist", 
            "message": f"Payroll Doesn't Exist. Please Enter Your Valid ID {data.id}"
        }), 404

    
    try:
        delete_query = delete_payroll_crud(id=data.id)

        if delete_query:
            return jsonify({
                "CODE": "Payroll_DELETED",
                "message": f"Payroll {data.id} Is Deleted"
            }), 200
        
    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for {data.id} updation, please try again {error}"
        })
        
    except Exception:
        current_app.logger.error("Exception Error Occured")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for {data.id} updation, please try again"
        })
    