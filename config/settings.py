
from config import variabbles


class DevelopmentConfig:
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 1 dia    

    # Configurar JWT
    JWT_SECRET_KEY = variabbles.JWT_SECRET_KEY  

class ProductionConfig:
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hora
    
    # Configurar JWT
    JWT_SECRET_KEY = variabbles.JWT_SECRET_KEY
    
