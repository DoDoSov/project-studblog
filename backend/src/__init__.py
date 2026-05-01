from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from .database import db
import os

# Initialize extensions outside the function so routes.py can import them
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'cockroachdb://root@localhost:26257/studblog'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = '123' # Required for JWT!
    
    # Bind extensions to the app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from .routes import api
    app.register_blueprint(api, url_prefix='/api') # Changed url_rule to url_prefix
    
    return app