import os
from flask import Flask
from flask_jwt_extended import JWTManager

from config import variabbles, settings

def create_app():
    app = Flask(__name__)    
    
    # Carregar configurações com base no ambiente
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(settings.ProductionConfig)
    else:
        app.config.from_object(settings.DevelopmentConfig)
    
    jwt = JWTManager(app)

    # Registrar blueprints
    from app.controllers.health_controller import health_bp # type: ignore
    from app.controllers.webhook_controller import webhook_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.example_controller import example_bp
    from app.controllers.license_plate_controller import license_plate_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(example_bp)
    app.register_blueprint(license_plate_bp)

    return app