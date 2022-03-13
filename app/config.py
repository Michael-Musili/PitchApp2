
import os

class Config:
    SECRET_KEY = 'mike254'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:musili@localhost/musili'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:mapesa@localhost/mapesa'
    DEBUG = True


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}






