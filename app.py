from flask import Flask
from database import init_db
from flask_cors import CORS
from config import Config

from controller.company.create import create_bp

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

    # Register EmplFLASK_ENVoyee blueprints
    app.register_blueprint(create_bp)

    @app.route("/")
    def index():
        return "Wellcome To Flask"
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)