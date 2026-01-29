from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll.get import get_payroll_id_crud, get_all_payroll_crud, get_short_payroll_crud
from schemas.payroll import PayrollResponse, PayrollListResponse, PayrollShortResponse
from auth import require_auth

payroll_get_bp = Blueprint("payroll_get_bp", __name__, url_prefix="/payroll")


@payroll_get_bp.route("/get", methods = ["GET"])
@require_auth
def get_payroll_id():

    data = request.json
    current_app.logger.info(f"Data: {data}")

    id = data.get("id")

    if not id:
        current_app.logger.error(f"Error {id}")
        return jsonify({
            "code": "Invalid_Payroll_ID",
            "Message": f"Please Enter a Valid Payroll ID"
        }), 403
    
    payroll = get_payroll_id_crud(id=id)
    print(f"Payroll:{payroll}")

    try:
        if payroll:
            return PayrollResponse(payroll).to_dict()
        
        else: 
            return {
                "code": "Payroll_ID_Dosent_Exists",
                "message": f"Please Try Another Payroll ID But This Payroll {id} Is Not Found!"
            }, 403
        
    except Exception as error:
        current_app.logger.error(f"Exception Error {error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Payroll {id}, Please Try Again"
        })
    

@payroll_get_bp.route("/all", methods = ["GET"])
@require_auth
def get_all_payrolls():

    current_app.logger.error('Get All Payroll Request Issue')

    try:
        get_all_payroll =  get_all_payroll_crud()

        if get_all_payroll:
            return PayrollListResponse.build(get_all_payroll)
        
        else:
            return {
                "code": "NO_PAYROLL_FOUND",
                "message": "No Payroll Exist. Please Add Payroll Earlier"
            }, 403
            
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "EXCEPTION",
            "message": f"Exception Error Occured For Payroll Deletion!"
        }
    
@payroll_get_bp.route("/short", methods = ["GET"])
@require_auth
def get_short_payroll():

    try:
        payrolls = get_short_payroll_crud()

        if payrolls:
            return PayrollShortResponse.from_list(payrolls)
        
        else:
            return {
                "code": "No_Short_Payroll_Found",
                "message": "No Payroll Found. Please Add Payroll Before Searching."
            }, 403
        
    except Exception as error:
        current_app.logger.error(f"Exception Error {error}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For Short Payroll, Please Try Again"
        }

