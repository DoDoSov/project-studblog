from flask import Flask
from flask_jwt_extended import JWTManager
from .database import db
import os

# 1. REMOVED Bcrypt import and initialization. 
# We are now using werkzeug.security inside routes.py 
# because it's compatible with your 'pbkdf2:sha256' database hashes.

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'cockroachdb://root@localhost:26257/studblog'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key-that-is-at-least-32-characters-long') 
    
    # Bind extensions to the app
    db.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from .routes import api
    
    # 2. IMPORTANT: If your routes.py decorators already say @api.route('/api/login'),
    # then url_prefix should be '/' or empty to avoid double prefixing (/api/api/login).
    # If your decorators say @api.route('/login'), then use url_prefix='/api'.
    app.register_blueprint(api, url_prefix='/api') 
    
    return app