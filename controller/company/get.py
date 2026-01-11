from flask import Blueprint, Flask, request, jsonify, current_app
from crud.company.get import get_company_by_id, get_all_company_crud
from schemas.company import CompanyResponse, CompanyListResponse

get_bp = Blueprint("get_bp", __name__, url_prefix="/company")


@get_bp.route("/by_company_name", methods = ["GET"])
def get_company_id():

    data = request.json
    current_app.logger.info(f"Data: {data}")

    company_id = data.get("company_id")

    if not company_id:
        current_app.logger.error(f"Error {company_id}")

        return jsonify({
            "Code":"No_Company_ID_Data",
            "message":"Please Enter Your With Another ID"
        }), 403
        

    company = get_company_by_id(company_id=company_id)

    try:
        if company:
            return CompanyResponse(company_id).to_dict()
        
        else:
            return jsonify({
                "code":"Company_Name_Doesn't_Exist",
                "message": f"Please Try another With Another ID, {company_id} Is Not Registered"
            }), 403
            
    except Exception as error:
        current_app.logger.error(f"Error {error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Company '{company_id}', Please Try Again"
        })
    

@get_bp.route("/all", methods = ["GET"])
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