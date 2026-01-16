from flask import Blueprint, Flask, request, jsonify, current_app
from crud.employee.get import get_employee_id_crud, get_all_employee_crud, get_short_employee_crud
from schemas.employee import EmployeeResponse, EmployeeListResponse, EmployeeShortResponse

employee_get_bp = Blueprint("employee_get_bp", __name__, url_prefix="/employee")


@employee_get_bp.route("/get", methods = ["GET"])
def get_employees():

    data = request.json
    current_app.logger.info(f"Data: {data}")

    id = data.get("id")

    if not id:
        current_app.logger.error(f"Error {id}")

        return jsonify({
            "Code": "Invalid_Employee_ID",
            "message": "Please enter a valid employee ID."
        }), 403
        

    employee = get_employee_id_crud(id=id)

    try:
        if employee:
            return EmployeeResponse(employee).to_dict()
        
        else:
            return jsonify({
                "code": "ID_Not_Found",
                "message": "The provided ID is not registered. Please try another ID."
            }), 403
            
    except Exception as error:
        current_app.logger.error(f"Error {error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Employee '{id}', Please Try Again"
        })
    

@employee_get_bp.route("/all", methods = ["GET"])
def get_all_employees():

    print('Get All Employee Request Issue')

    try:
        get_employees =  get_all_employee_crud()

        if get_employees:
            return EmployeeListResponse.build(get_employees)
        
        else:
            return {
                "code": "No_Employees_Found",
                "message": "No employees found. Please add an employee before searching."
            }, 403
            
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For All Employees, Please Try Again"
        }
    
@employee_get_bp.route("/short", methods = ["GET"])
def get_short_employee():

    try:
        employees = get_short_employee_crud()

        if employees:
            return EmployeeShortResponse.from_list(employees)
        
        else:
            return {
                "code": "No_Short_Employees_Found",
                "message": "No employees found. Please add an employee name before searching."
            }, 403
        
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For Short Employees, Please Try Again"
        }



