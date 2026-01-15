import enum

class DepartmentEnum(enum.Enum):
    HR = "hr"
    ACCOUNTS = "accounts"
    TECH = "tech"
    GUEST = "guest"

class StatusEnum(enum.Enum):
    PERMANENT = "permanent"
    PROBATION = "probation"
    TRAINEE = "trainee"

class GenderEnum(enum.Enum):
    MALE = "male"
    FEMALE = "female"

class CreateEmployeeRequest:
    def __init__(self, data):
        self.employee_id = data.get("employee_id")
        self.employee_department = data.get("hr", "accounts", "tech", "guest")
        self.employee_name = data.get("employee_name")
        self.employee_status = data.get("permanent", "probation", "trainee")
        self.employee_email = data.get("employee_email")
        self.employee_phone_number_main = data.get("employee_phone_number_main")
        self.employee_phone_number_secondary = data.get("employee_phone_number_secondary")
        self.employee_dob = data.get("employee_dob")
        self.employee_cnic = data.get("employee_cnic")
        self.employee_gender = data.get("male", "female")
        self.employee_address_permanent = data.get("employee_address_permanent")
        self.employee_address_current = data.get("employee_address_current")

    def is_valid(self):
        # Required fields
        if not all([
            self.employee_id,
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
        ]):
            
            return False, "Missing required fields"
        

        # Validate Department Role Against Enum
        if self.employee_department not in [role.value for role in DepartmentEnum]:
            return False, "Invalid role provided."
        
        
        # Validate Status Role Against Enum
        if self.employee_status not in [role.value for role in StatusEnum]:
            return False, "Invalid role provided."
        

        # Validate Gender Role Against Enum
        if self.employee_gender not in [role.value for role in GenderEnum]:
            return False, "Invalid role provided."
        

        return True, None


class UpdateEmployeeRequest:
    def __init__(self, data):
        self.employee_id = data.get("employee_id")
        self.employee_department = data.get("hr", "accounts", "tech", "guest")
        self.employee_name = data.get("employee_name")
        self.employee_status = data.get("permanent", "probation", "trainee")
        self.employee_email = data.get("employee_email")
        self.employee_phone_number_main = data.get("employee_phone_number_main")
        self.employee_phone_number_secondary = data.get("employee_phone_number_secondary")
        self.employee_dob = data.get("employee_dob")
        self.employee_cnic = data.get("employee_cnic")
        self.employee_gender = data.get("male", "female")
        self.employee_address_permanent = data.get("employee_address_permanent")
        self.employee_address_current = data.get("employee_address_current")
    
    def is_valid(self):

        # Validate Department Role Against Enum
        if self.employee_department not in [role.value for role in DepartmentEnum]:
            return False, "Invalid role provided."
        
        
        # Validate Status Role Against Enum
        if self.employee_status not in [role.value for role in StatusEnum]:
            return False, "Invalid role provided."
        

        # Validate Gender Role Against Enum
        if self.employee_gender not in [role.value for role in GenderEnum]:
            return False, "Invalid role provided."
        
        return True, None


    def has_any_updates(self):
        return any([
            self.employee_id,
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
        self.employee_id = data.get("employee_id")

    def is_valid(self):
        if not any(self.employee_id):
            return False, "Employee ID Is Required"
        
        return True, None

class EmployeeResponse:
    def __init__(self, employee):
        self.employee_id = employee.employee_id
        self.employee_department = employee.employee_department.value
        self.employee_name = employee.employee_name
        self.employee_status = employee.employee_status.value
        self.employee_email = employee.employee_email
        self.employee_phone_number_main = employee.employee_phone_number_main
        self.employee_phone_number_secondary = employee.employee_phone_number_secondary
        self.employee_dob = employee.employee_dob
        self.employee_cnic = employee.employee_cnicb
        self.employee_gender = employee.employee_gender.value
        self.employee_address_permanent = employee.employee_address_permanent
        self.employee_address_current = employee.employee_address_current

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
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
            "employee_address_current": self.employee_address_current
        }
    
class EmployeeShortResponse:
    def __init__(self, employee):
        self.employee_id = employee.employee_id
        self.employee_name = employee.employee_name

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "employee_name": self.employee_name
        }
    
    @staticmethod
    def from_list(employees):
        return [EmployeeShortResponse(emp).to_dict() for emp in employees]

class EmployeeListResponse:
    @staticmethod
    def build(employees):
        return [EmployeeResponse(emp).to_dict() for emp in employees]