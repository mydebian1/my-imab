class LoginRequest:
    def __init__(self, data):
        self.username = data.get("username")
        self.password = data.get("password")
    
    def is_valid(self):
        if not self.username:
            return False, "Username is required."
        
        if not self.password:
            return False, "Password is required."
        
        if len(self.username) < 6:
            return False, "The username must be a minimum of six characters in length."
        
        if len(self.password) < 6:
            return False, "The Password must be a minimum of six characters in length."
        
        return True, None

class LoginResponse:
    def __init__(self, token, employee_id, username):
        self.token = token
        self.employee_id = employee_id
        self.username = username
    
    def to_dict(self):
        return {
            "token": self.token,
            "employee_id": self.employee_id,
            "username": self.username
        }