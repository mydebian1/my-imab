from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll.create import create_payroll_crud
from utils.utils import get_payroll, get_employee_by_id, get_hourly_rate, get_over_below, get_score, get_addition, get_deduction, get_gross, get_tax, get_total_net, get_net_orion
from sqlalchemy.exc import IntegrityError
from schemas.payroll import CreatePayrollRequest, PayrollResponse
from auth import require_auth

payroll_create_bp = Blueprint("payroll_create_bp", __name__, url_prefix="/payroll")

@payroll_create_bp.route('/create', methods = ["POST"])
@require_auth
def create_payroll():

    data = CreatePayrollRequest(request.json)
    current_app.logger.info(f"Data: {data}")

    if not data.is_valid():
        return jsonify({"error": "Missing Fields"}), 400
        
    payroll = get_payroll(data.employee_id, data.batch_name)
    
    if payroll:
        current_app.logger.error("Payroll Already Exists")
        return jsonify({
                "code": "PAYROLL_ALREADY_EXISTS",
                "message": f"This Employee ID {data.employee_id} and Batch Name {data.batch_name} is already exists, Please try another one"
        }), 403
    
    employee = get_employee_by_id(data.employee_id)
    if not employee:
        current_app.logger.error("Employee Not Exists")
        return jsonify({
                "code": "EMPLOYEE_NOT_EXIST",
                "message": f"This Employee ID {data.employee_id} does not exist."
        }), 403
    
    current_app.logger.info(f"employee.employee_basic_salary: {employee.employee_basic_salary}")

    #Calculations
    employee_hourly_rate = get_hourly_rate(employee.employee_basic_salary, data.employee_contract_hours)
    employee_over_below = get_over_below(data.employee_worked_hours, data.employee_contract_hours)
    employee_score = get_score(data.employee_lates, data.employee_early, data.employee_leaves)
    total_addition = get_addition(employee_over_below, employee_hourly_rate)
    total_deduction = get_deduction(employee_over_below, employee_hourly_rate)
    total_gross = get_gross(employee.employee_basic_salary, total_addition, total_deduction)
    total_tax = get_tax(total_gross)
    total_net_employee = get_total_net(total_gross, total_tax)
    total_net_orion = get_net_orion(total_gross)

    if employee_hourly_rate and employee_over_below and employee_score and total_addition and total_deduction and total_gross and total_tax and total_net_employee and total_net_orion:
        current_app.logger.info(f"Payroll calculations performed.")
    
    try:
        new_payroll = create_payroll_crud(
            employee_id = data.employee_id,
            company_id = data.company_id,
            batch_name = data.batch_name,
            batch_status = data.batch_status,
            employee_contract_hours = data.employee_contract_hours,
            employee_rota_hours = data.employee_rota_hours,
            employee_worked_hours = data.employee_worked_hours,
            employee_net_hours = 0,
            employee_lates = data.employee_lates,
            employee_early = data.employee_early,
            employee_leaves = data.employee_leaves,
            employee_basic_salary = employee.employee_basic_salary,
            employee_hourly_rate = employee_hourly_rate,
            employee_over_below = employee_over_below,
            employee_score = employee_score,
            total_addition = total_addition,
            total_deduction = total_deduction,
            total_gross = total_gross,
            total_tax = total_tax,
            total_net_employee = total_net_employee,
            total_net_orion = total_net_orion
        )
    
        return jsonify({
            "code": "Payroll_CREATED",
            "data": PayrollResponse(new_payroll).to_dict()
        }), 200
    
    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error {error}")
        return jsonify({"code": "INTEGRITY_ERROR", "message": str(error)}), 409

    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return jsonify({"code": "ERROR"}), 500





    





