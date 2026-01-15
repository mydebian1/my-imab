class CreatePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.batch_status = data.get("batch_status")
        self.employee_basic_salary = data.get("employee_basic_salary")
        self.employee_hourly_rate = data.get("employee_hourly_rate")
        self.employee_contract_hours = data.get("employee_contract_hours")
        self.employee_rota_hours = data.get("employee_rota_hours")
        self.employee_worked_hours = data.get("employee_worked_hours")
        self.employee_net_hours = data.get("employee_net_hours")
        self.employee_over_below = data.get("employee_over_below")
        self.employee_lates = data.get("employee_lates")
        self.employee_early = data.get("employee_early")
        self.employee_leaves = data.get("employee_leaves")
        self.employee_score = data.get("employee_score")
        self.total_addition = data.get("total_addition")
        self.total_deduction = data.get("total_deduction")
        self.total_gross = data.get("total_gross")
        self.total_tax = data.get("total_tax")
        self.total_net_employee = data.get("total_net_employee")
        self.total_net_orion = data.get("total_net_orion")


    def is_valid(self):
        # Required fields
        if not all([
            self.batch_name,
            self.batch_status,
            self.employee_basic_salary,
            self.employee_hourly_rate,
            self.employee_contract_hours,
            self.employee_rota_hours,
            self.employee_worked_hours,
            self.employee_net_hours,
            self.employee_over_below,
            self.employee_lates,
            self.employee_early,
            self.employee_leaves,
            self.employee_score,
            self.total_addition,
            self.total_deduction,
            self.total_gross,
            self.total_tax,
            self.total_net_employee,
            self.total_net_orion
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
        self.batch_name = data.get("batch_name")
        self.batch_status = data.get("batch_status")
        self.employee_basic_salary = data.get("employee_basic_salary")
        self.employee_hourly_rate = data.get("employee_hourly_rate")
        self.employee_contract_hours = data.get("employee_contract_hours")
        self.employee_rota_hours = data.get("employee_rota_hours")
        self.employee_worked_hours = data.get("employee_worked_hours")
        self.employee_net_hours = data.get("employee_net_hours")
        self.employee_over_below = data.get("employee_over_below")
        self.employee_lates = data.get("employee_lates")
        self.employee_early = data.get("employee_early")
        self.employee_leaves = data.get("employee_leaves")
        self.employee_score = data.get("employee_score")
        self.total_addition = data.get("total_addition")
        self.total_deduction = data.get("total_deduction")
        self.total_gross = data.get("total_gross")
        self.total_tax = data.get("total_tax")
        self.total_net_employee = data.get("total_net_employee")
        self.total_net_orion = data.get("total_net_orion")
        
    def is_valid(self):
        # Required fields
        if not self.batch_name:
            return False, "Batch name is not provided"
        
        if not self.staff_id:
            return False, "Staff id is not provided"
        
        
        if self.employee_lates < 0:
            return False, f"{self.employee_lates} Cannot Be Negative"

        if self.employee_early < 0:
            return False, f"{self.employee_early} Cannot Be Negative"
        
        if self.employee_leaves < 0:
            return False, f"{self.employee_leaves} Cannot Be Negative"
        
        return True, None
        
    
    def has_any_updates(self):
        return any([
            self.batch_name,
            self.batch_status,
            self.employee_basic_salary,
            self.employee_hourly_rate,
            self.employee_contract_hours,
            self.employee_rota_hours,
            self.employee_worked_hours,
            self.employee_net_hours,
            self.employee_over_below,
            self.employee_lates,
            self.employee_early,
            self.employee_leaves,
            self.employee_score,
            self.total_addition,
            self.total_deduction,
            self.total_gross,
            self.total_tax,
            self.total_net_employee,
            self.total_net_orion
        ])
    
class DeletePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.employee_id = data.get("employee_id")
        
    def is_valid(self):
        if not all([self.batch_name, self.employee_id]):
            return False, "Username Is Required"
        
        return True, None


class PayrollResponse:
    def __init__(self, payroll):
        self.batch_name = payroll.batch_name
        self.batch_status = payroll.batch_status
        self.employee_basic_salary = payroll.employee_basic_salary
        self.employee_hourly_rate = payroll.employee_hourly_rate
        self.employee_contract_hours = payroll.employee_contract_hours
        self.employee_rota_hours = payroll.employee_rota_hours
        self.employee_worked_hours = payroll.employee_worked_hours
        self.employee_net_hours = payroll.employee_net_hours
        self.employee_over_below = payroll.employee_over_below
        self.employee_lates = payroll.employee_lates
        self.employee_early = payroll.employee_early
        self.employee_leaves = payroll.employee_leaves
        self.employee_score = payroll.employee_score
        self.total_addition = payroll.total_addition
        self.total_deduction = payroll.total_deduction
        self.total_gross = payroll.total_gross
        self.total_tax = payroll.total_tax
        self.total_net_employee = payroll.total_net_employee
        self.total_net_orion = payroll.total_net_orion

    def to_dict(self):
        return {
            "batch_name": self.batch_name,
            "batch_status": self.batch_status,
            "employee_basic_salary": self.employee_basic_salary,
            "employee_hourly_rate": self.employee_hourly_rate,
            "employee_contract_hours": self.employee_contract_hours,
            "employee_rota_hours": self.employee_rota_hours,
            "employee_worked_hours": self.employee_worked_hours,
            "employee_net_hours": self.employee_net_hours,
            "employee_over_below": self.employee_over_below,
            "employee_lates": self.employee_lates,
            "employee_early": self.employee_early,
            "employee_leaves": self.employee_leaves,
            "employee_score": self.employee_score,
            "total_addition": self.total_addition,
            "total_deduction": self.total_deduction,
            "total_gross": self.total_gross,
            "total_tax": self.total_tax,
            "total_net_employee": self.total_net_employee,
            "total_net_orion": self.total_net_orion
        }


class PayrollListResponse:
    @staticmethod
    def build(payrolls):
        return [PayrollResponse(emp).to_dict() for emp in payrolls]

        