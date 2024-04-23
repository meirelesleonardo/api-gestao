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
        
    # Configurar o caminho para os templates
    app.template_folder = app.config['TEMPLATE_FOLDER']
            
    jwt = JWTManager(app)    

    
    # Registrar blueprints Frontend Gestão
    from apps.gestao.controllers.auth_frontend import auth_frontend_bp

    app.register_blueprint(auth_frontend_bp)

    return app