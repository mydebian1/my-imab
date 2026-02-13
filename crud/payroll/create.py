from database import db
from models import Payroll
from sqlalchemy.exc import IntegrityError


def create_payroll_crud(employee_id, company_id, batch_name, batch_status, employee_contract_hours, employee_rota_hours, employee_worked_hours, employee_net_hours, employee_lates, employee_early, employee_leaves, employee_basic_salary, employee_hourly_rate, employee_over_below, employee_score, total_addition, total_deduction, total_gross, total_tax, total_net_employee, total_net_orion):
    try:
        create_payroll = Payroll(
            employee_id = employee_id,
            company_id = company_id,
            batch_name = batch_name,
            batch_status = batch_status,
            employee_contract_hours = employee_contract_hours,
            employee_rota_hours = employee_rota_hours,
            employee_worked_hours = employee_worked_hours,
            employee_net_hours = 0,
            employee_lates = employee_lates,
            employee_early = employee_early,
            employee_leaves = employee_leaves,
            employee_basic_salary = employee_basic_salary,
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

        db.session.add(create_payroll)
        db.session.commit()

        return create_payroll
    
    except IntegrityError:
        raise
        
    except Exception:
        raise
