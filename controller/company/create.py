from flask import Flask, Blueprint, request, jsonify, current_app
from crud.company.create import create_company_crud
from utils.utils import get_company
from sqlalchemy.exc import IntegrityError
from schemas.company import CreateCompanyRequest, CompanyResponse
from auth import require_auth

create_bp = Blueprint("create_bp", __name__, url_prefix="/company")

@create_bp.route("/create", methods=["POST"])
@require_auth
def create_company():
    current_app.logger.info(request.json)

    data = CreateCompanyRequest(request.json)
    current_app.logger.info(data)
    valid, message = data.is_valid()


    current_app.logger.info(f"Checking Data By Company Name And Email {data.company_name, data.company_email}")


    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400

    
    company = get_company(data.company_name, data.company_email)


    current_app.logger.info(f"Found Company By Name And Email: {company}")


    if company:
        current_app.logger.error("Company Already Exists")
        return jsonify({
                "code": "COMPANY_ALREADY_EXISTS",
                "message": f"This Company Name {data.company_name} And Email {data.company_email} Is Already Exists, Please Try a New One"
        }), 403
    
    current_app.logger.info(f"calling create_company_crud from controller")

    try:
        new_company = create_company_crud(
            company_name = data.company_name,
            company_email = data.company_email,
            company_address = data.company_address,
            company_joined = data.company_joined
        )

        return jsonify({
            "code": "COMPANY_CREATED",
            "data": CompanyResponse(new_company).to_dict()
        }), 201

    except IntegrityError as e:
        current_app.logger.error(f"Integrity Error {e}")
        return jsonify({"code": "INTEGRITY_ERROR", "message": str(e)}), 409

    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return jsonify({"code": "ERROR"}), 500