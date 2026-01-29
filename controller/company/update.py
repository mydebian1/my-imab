from flask import Blueprint, Flask, request, jsonify, current_app
from crud.company.update import update_company_crud
from utils.utils import get_company_by_id
from sqlalchemy.exc import IntegrityError
from schemas.company import UpdateCompanyRequest, CompanyResponse
from auth import require_auth

update_bp = Blueprint("update_bp", __name__, url_prefix="/company")


@update_bp.route("/update", methods=["PUT"])
@require_auth
def update_require_company():

    data = UpdateCompanyRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400

    if not data.has_any_updates():
        return jsonify({
            "code": "DATA_MISSING", 
            "error": "Required fields for data update not provided"
            }), 400
    
    company = get_company_by_id(data.id)

    if not company:
        current_app.logger.error(f"Error. {company}")
        return jsonify({
            "code": "COMPANY_NOT_FOUND", 
            "error": "Required fields for data update not provided"
        }), 404

    try:
        company = update_company_crud(id=data.id, company_name=data.company_name, company_email=data.company_email, company_address=data.company_address, company_joined=data.company_joined)

        return jsonify({
            "code": "Company_Updated",
            "data": CompanyResponse(company).to_dict()
        }), 403
    

    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for '{data.id}' creation, please try again {error}"
        })
    
        
    except Exception as e:
        current_app.logger.error(f"Integrity Error Occured: {e}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{data.id}' creation, please try again"
        })
    

