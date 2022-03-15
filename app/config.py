
import os

class Config:
    SECRET_KEY = 'mike254'
    
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:musili@localhost/musili'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:access@localhost/pitchapp'
    DEBUG = True


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}






