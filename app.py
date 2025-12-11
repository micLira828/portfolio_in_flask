from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # IMPORTANT: allow Flask to access /instance folder
    app = Flask(__name__, 
                static_folder="static",
                instance_relative_config=True)

    # Load database settings
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Test route
    @app.route("/")
    def index():
        return "Portfolio backend is running!"

    return app
