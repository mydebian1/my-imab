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
        