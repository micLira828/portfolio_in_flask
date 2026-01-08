from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    # IMPORTANT: allow Flask to access /instance folder
    app = Flask(__name__, 
                static_folder="static",
                instance_relative_config=True)

    # Load database settings
    app.config.from_object(Config)

    # Initialize extensions
   
    CORS(
            app, 
            resources={r"/api/*":{"origins": ["https://micLira828.github.io"]}},
            supports_credentials=False
        )
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    
    from routes.projects_routes import projects_routes
    from routes.nutshell_routes import nutshell_routes
    from routes.messages_routes import messages_routes
    
    app.register_blueprint(projects_routes)
    app.register_blueprint(nutshell_routes)
    app.register_blueprint(messages_routes)

    # Test route
    @app.route("/")
    def index():
        return "Portfolio backend is running!"

    return app
