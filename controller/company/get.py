from flask import Blueprint, request, jsonify, current_app
from crud.company.get import get_company_id_crud, get_all_company_crud, get_short_company_crud
from schemas.company import CompanyResponse, CompanyListResponse, CompanyShortResponse
from auth import require_auth

get_bp = Blueprint("get_bp", __name__, url_prefix="/company")


@get_bp.route("/get", methods = ["GET"])
@require_auth
def get_company_id():

    data = request.json
    current_app.logger.info(f"Data: {data}")

    id = data.get("id")

    if not id:
        current_app.logger.error(f"Error {id}")

        return jsonify({
            "Code":"ID_Data",
            "message":"Please Enter Your With Another ID"
        }), 403
        

    company = get_company_id_crud(id=id)

    try:
        if company:
            return CompanyResponse(company).to_dict()
        
        else:
            return jsonify({
                "code":"Company_Name_Doesn't_Exist",
                "message": f"Please Try another With Another ID, {company} Is Not Registered"
            }), 403
            
    except Exception as error:
        current_app.logger.error(f"Error {error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Company '{company}', Please Try Again"
        })
    

@get_bp.route("/all", methods = ["GET"])
@require_auth
def get_all_companies():

    print('Get All Company Request Issue')

    try:
        get_companies =  get_all_company_crud()

        if get_companies:
            return CompanyListResponse.build(get_companies)
        
        else:
            return {
                "code": "No_Companies_Found",
                "message": "Please Add The Company First Then Search Here"
            }, 403
            
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For All Companies, Please Try Again"
        }
    

@get_bp.route("/short", methods = ["GET"])
@require_auth
def get_short_company():

    try:
        companies = get_short_company_crud()

        if companies:
            return CompanyShortResponse.from_list(companies)
        
        else:
            return {
                "code": "No_Short_Companies_Found",
                "message": "No companies found. Please add an employee name before searching."
            }, 403
        
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For Short Companies, Please Try Again"
        }