from database import db
from utils.utils import get_payroll_by_id
from sqlalchemy.exc import IntegrityError

def update_payroll_crud(id, employee_contract_hours, employee_rota_hours, employee_worked_hours, employee_lates, employee_early, employee_leaves):
    payroll = get_payroll_by_id(id)

    if not payroll:
        return payroll == False
    
    try:
        if id:
            payroll.id = id

        if employee_contract_hours:
            payroll.employee_contract_hours = employee_contract_hours

        if employee_rota_hours:
            payroll.employee_rota_hours = employee_rota_hours

        if employee_worked_hours:
            payroll.employee_worked_hours = employee_worked_hours

        if employee_lates: 
            payroll.employee_lates = employee_lates

        if employee_early:
            payroll.employee_early = employee_early

        if employee_leaves:
            payroll.employee_leaves = employee_leaves

        db.session.commit()

        return payroll
    
    except IntegrityError:
        raise
    
    except Exception:
        raise




