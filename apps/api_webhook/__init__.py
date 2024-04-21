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
    from apps.api_webhook.controllers.webhook_controller import webhook_bp
    app.register_blueprint(webhook_bp)    

    return app