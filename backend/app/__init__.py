"""Flask application initialization."""

from flask import Flask
from flask_cors import CORS

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints here when ready
    # from .routes import api_bp
    # app.register_blueprint(api_bp)
    
    return app
