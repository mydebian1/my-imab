from models import DepartmentEnum, StatusEnum, GenderEnum

class CreateEmployeeRequest:
    def __init__(self, data):
        self.employee_company_id = data.get("employee_company_id")
        self.employee_department = data.get("employee_department")
        self.employee_name = data.get("employee_name")
        self.employee_status = data.get("employee_status")
        self.employee_email = data.get("employee_email")
        self.employee_phone_number_main = data.get("employee_phone_number_main")
        self.employee_phone_number_secondary = data.get("employee_phone_number_secondary")
        self.employee_dob = data.get("employee_dob")
        self.employee_cnic = data.get("employee_cnic")
        self.employee_gender = data.get("employee_gender")
        self.employee_address_permanent = data.get("employee_address_permanent")
        self.employee_address_current = data.get("employee_address_current")
        self.employee_basic_salary = data.get("employee_basic_salary")

    def is_valid(self):
        # Required fields
        if not all([
            self.employee_company_id,
            self.employee_department,
            self.employee_name,
            self.employee_status,
            self.employee_email,
            self.employee_phone_number_main,
            self.employee_phone_number_secondary,
            self.employee_dob,
            self.employee_cnic,
            self.employee_gender,
            self.employee_address_permanent,
            self.employee_address_current,
            self.employee_basic_salary
        ]):
            
            return False, "Missing required fields"
        

        # Validate Department Role Against Enum
        if self.employee_department and self.employee_department not in [role.value for role in DepartmentEnum]:
            return False, "Invalid role provided."
        
        
        # Validate Status Role Against Enum
        if self.employee_status and self.employee_status not in [role.value for role in StatusEnum]:
            return False, "Invalid role provided."
        

        # Validate Gender Role Against Enum
        if self.employee_gender and self.employee_gender not in [role.value for role in GenderEnum]:
            return False, "Invalid role provided."
        

        return True, None


class UpdateEmployeeRequest:
    def __init__(self, data):
        self.id = data.get("id")
        self.employee_department = data.get("employee_department")
        self.employee_name = data.get("employee_name")
        self.employee_status = data.get("employee_status")
        self.employee_email = data.get("employee_email")
        self.employee_phone_number_main = data.get("employee_phone_number_main")
        self.employee_phone_number_secondary = data.get("employee_phone_number_secondary")
        self.employee_dob = data.get("employee_dob")
        self.employee_cnic = data.get("employee_cnic")
        self.employee_gender = data.get("employee_gender")
        self.employee_address_permanent = data.get("employee_address_permanent")
        self.employee_address_current = data.get("employee_address_current")
    
    def is_valid(self):

        # Validate Department Role Against Enum
        if self.employee_department and self.employee_department not in [role.value for role in DepartmentEnum]:
            return False, "Invalid role provided."
        
        
        # Validate Status Role Against Enum
        if self.employee_status and self.employee_status not in [role.value for role in StatusEnum]:
            return False, "Invalid role provided."
        

        # Validate Gender Role Against Enum
        if self.employee_gender and self.employee_gender not in [role.value for role in GenderEnum]:
            return False, "Invalid role provided."
        
        return True, None


    def has_any_updates(self):
        return any([
            self.id,
            self.employee_department,
            self.employee_name,
            self.employee_status,
            self.employee_email,
            self.employee_phone_number_main,
            self.employee_phone_number_secondary,
            self.employee_dob,
            self.employee_cnic,
            self.employee_gender,
            self.employee_address_permanent,
            self.employee_address_current
        ])

class DeleteEmployeeRequest:
    def __init__(self, data):
        self.id = data.get("id")

    def is_valid(self):
        if not (self.id):
            return False, "Employee ID Is Required"
        
        return True, None

class EmployeeResponse:
    def __init__(self, employee):
        self.id = employee.id
        self.employee_company_id = employee.employee_company_id
        self.employee_department = employee.employee_department.value
        self.employee_name = employee.employee_name
        self.employee_status = employee.employee_status.value
        self.employee_email = employee.employee_email
        self.employee_phone_number_main = employee.employee_phone_number_main
        self.employee_phone_number_secondary = employee.employee_phone_number_secondary
        self.employee_dob = employee.employee_dob
        self.employee_cnic = employee.employee_cnic
        self.employee_gender = employee.employee_gender.value
        self.employee_address_permanent = employee.employee_address_permanent
        self.employee_address_current = employee.employee_address_current
        self.employee_basic_salary = employee.employee_basic_salary

    def to_dict(self):
        return {
            "id": self.id,
            "employee_company_id": self.employee_company_id,
            "employee_department": self.employee_department,
            "employee_name": self.employee_name,
            "employee_status": self.employee_status,
            "employee_email": self.employee_email,
            "employee_phone_number_main": self.employee_phone_number_main,
            "employee_phone_number_secondary": self.employee_phone_number_secondary,
            "employee_dob": self.employee_dob.isoformat(),
            "employee_cnic": self.employee_cnic,
            "employee_gender": self.employee_gender,
            "employee_address_permanent": self.employee_address_permanent,
            "employee_address_current": self.employee_address_current,
            "employee_basic_salary": self.employee_basic_salary 
        }
    
class EmployeeShortResponse:
    def __init__(self, employee):
        self.id = employee.id
        self.employee_name = employee.employee_name
        self.employee_email = employee.employee_email
        self.employee_status = employee.employee_status

    def to_dict(self):
        return {
            "id": self.id,
            "employee_name": self.employee_name,
            "employee_email": self.employee_email,
            "employee_status": self.employee_status.value
        }
    
    @staticmethod
    def from_list(employees):
        return [EmployeeShortResponse(emp).to_dict() for emp in employees]

class EmployeeListResponse:
    @staticmethod
    def build(employees):
        return [EmployeeResponse(emp).to_dict() for emp in employees]