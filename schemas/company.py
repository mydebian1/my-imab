from datetime import date

class CreateCompanyRequest:
    def __init__(self, data):
        self.company_id = data.get("id")
        self.company_name = data.get("name")
        self.company_email = data.get("email")
        self.company_address = data.get("address")
        self.company_joined = data.get("date")

        try:
            self.company_joined = date.fromisoformat(data.get("date")) if data.get("date") else None
        except ValueError:
            self.company_joined = None  # Handle invalid formats

    def is_valid(self):
        # Required fields
        if not all([self.company_id, self.company_name, self.company_email, self.company_address, self.company_joined]):
            return False, "Missing required fields"

        return True, None


class UpdateCompanyRequest:
    def __init__(self, data):
        self.company_id = data.get("id")
        self.company_name = data.get("name")
        self.company_email = data.get("email")
        self.company_address = data.get("address")
        self.company_joined = data.get("date")

        try:
            self.company_joined = date.fromisoformat(data.get("date")) if data.get("date") else None
        except ValueError:
            self.company_joined = None  # Handle invalid formats
    
    def is_valid(self):

        if not self.company_id:
            return False, "Company ID Not Provided"
        
        return True, None


    def has_any_updates(self):
        return any([self.company_id, self.company_name, self.company_email, self.company_address, self.company_joined])
    

class CompanyResponse:
    def __init__(self, company):
        self.id = company.company_id
        self.name = company.company_name
        self.email = company.company_email
        self.address = company.company_address
        self.date = company.company_joined

    def to_dict(self):
        return {
            "company_id": self.id,
            "company_name": self.name,
            "company_email": self.email,
            "company_address": self.address,
            "company_joined": self.date
        }

class CompanyListResponse:
    @staticmethod
    def build(companies):
        return [CompanyResponse(emp).to_dict() for emp in companies]