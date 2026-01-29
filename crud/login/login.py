from flask import current_app
from models import Login

def verify_login(username, password):
    login = Login.query.filter_by(username=username).first()
    
    if not login:
        current_app.logger.info(f"No Employee {login}.")
        return None
    
    if login.password == password:
        current_app.logger.info(f"Employee {login} returned.")
        return login
    
    return None