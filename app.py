from flask import Flask
from database import init_db
from flask_cors import CORS
from config import Config

# Company Blueprints
from controller.company.create import create_bp
from controller.company.update import update_bp
from controller.company.get import get_bp

# Company Blueprints
from controller.employee.create import employee_create_bp

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # CORS
    CORS(app)

    # Logging
    app.logger.setLevel(app.config["LOG_LEVEL"])

    # Initialize DB
    init_db(app)

    # Register Company Blueprints
    app.register_blueprint(create_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(get_bp)


    # Register Employee Blueprints
    app.register_blueprint(employee_create_bp)
    

    @app.route("/")
    def index():
        return "Wellcome To Flask"
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)