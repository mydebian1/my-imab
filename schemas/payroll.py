class CreatePayrollRequest:
    def __init__(self, data):
        self.employee_id = data.get("employee_id")
        self.company_id = data.get("company_id")
        self.batch_name = data.get("batch_name")
        self.batch_status = data.get("batch_status", "open")
        self.employee_contract_hours = data.get("employee_contract_hours")
        self.employee_rota_hours = data.get("employee_rota_hours")
        self.employee_worked_hours = data.get("employee_worked_hours")
        self.employee_lates = data.get("employee_lates")
        self.employee_early = data.get("employee_early")
        self.employee_leaves = data.get("employee_leaves")

    def is_valid(self):
        if not all([
            self.employee_id,
            self.company_id,
            self.batch_name,
            self.batch_status,
            self.employee_contract_hours,
            self.employee_rota_hours,
            self.employee_worked_hours,
            self.employee_lates,
            self.employee_early,
            self.employee_leaves
        ]):
            return False, "Missing Required Fields"
        

        if self.employee_lates < 0:
            return False, f"{self.employee_lates} Cannot Be Negative"

        if self.employee_early < 0:
            return False, f"{self.employee_early} Cannot Be Negative"
        
        if self.employee_leaves < 0:
            return False, f"{self.employee_leaves} Cannot Be Negative"

        return True, None
        
class UpdatePayrollRequest:
    def __init__(self, data):
        self.id = data.get("id")
        self.employee_contract_hours = data.get("employee_contract_hours")
        self.employee_rota_hours = data.get("employee_rota_hours")
        self.employee_worked_hours = data.get("employee_worked_hours")
        self.employee_lates = data.get("employee_lates")
        self.employee_early = data.get("employee_early")
        self.employee_leaves = data.get("employee_leaves")
        
    def is_valid(self):
        if self.employee_lates < 0:
            return False, f"{self.employee_lates} Cannot Be Negative"

        if self.employee_early < 0:
            return False, f"{self.employee_early} Cannot Be Negative"
        
        if self.employee_leaves < 0:
            return False, f"{self.employee_leaves} Cannot Be Negative"
        
        return True, None
        
    
    def has_any_updates(self):
        return any([
            self.id,
            self.employee_contract_hours,
            self.employee_rota_hours,
            self.employee_worked_hours,
            self.employee_lates,
            self.employee_early,
            self.employee_leaves
        ])
    
class DeletePayrollRequest:
    def __init__(self, data):
        self.id = data.get("id")
        
    def is_valid(self):
        if not all([self.id]):
            return False, "Payroll ID Is Required"
        
        return True, None


class PayrollResponse:
    def __init__(self, payroll):
        self.employee_id = payroll.employee_id
        self.company_id = payroll.company_id
        self.batch_name = payroll.batch_name
        self.batch_status = payroll.batch_status
        self.employee_contract_hours = payroll.employee_contract_hours
        self.employee_rota_hours = payroll.employee_rota_hours
        self.employee_worked_hours = payroll.employee_worked_hours
        self.employee_lates = payroll.employee_lates
        self.employee_early = payroll.employee_early
        self.employee_leaves = payroll.employee_leaves

        #Check if employee relationship is loaded
        if getattr(payroll, 'employee') and payroll.employee_id:
            self.employee_name = payroll.employee.employee_name
            self.employee_status = payroll.employee.employee_status if payroll.employee.employee_status else None
            self.employee_department = payroll.employee.employee_department if payroll.employee.employee_department else None
        else:
            self.employee_name = None
            self.employee_status = None
            self.employee_department = None
        
        #Check if company relationship is loaded
        if getattr(payroll, 'company') and payroll.company_id:
            self.company_name = payroll.company.company_name
        else:
            self.company_name = None

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "company_id": self.company_id,
            "batch_name": self.batch_name,
            "batch_status": self.batch_status,
            "employee_contract_hours": self.employee_contract_hours,
            "employee_rota_hours": self.employee_rota_hours,
            "employee_worked_hours": self.employee_worked_hours,
            "employee_lates": self.employee_lates,
            "employee_early": self.employee_early,
            "employee_leaves": self.employee_leaves,
            "employee_name": self.employee_name,
            "employee_status": self.employee_status.value,
            "employee_department": self.employee_department.value,
            "company_name": self.company_name
        }
    
class PayrollShortResponse:
    def __init__(self, payroll):
        self.id = payroll.id
        self.employee_name = payroll.employee_name
        self.company_name = payroll.company_name
        self.batch_name = payroll.batch_name

    def to_dict(self):
        return {
            "id": self.id,
            "employee_name": self.employee_name,
            "company_name": self.company_name,
            "batch_name": self.batch_name
        }
    
    @staticmethod
    def from_list(payrolls):
        return [PayrollShortResponse(emp).to_dict() for emp in payrolls]

class PayrollListResponse:
    @staticmethod
    def build(payrolls):
        return [PayrollResponse(emp).to_dict() for emp in payrolls]
    


        