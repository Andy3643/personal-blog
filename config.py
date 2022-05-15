import os
class Config:
    '''
    General  app configuration settings
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SECRET_KEY="secret123"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:pass123@localhost/blogsite"
    DEBUG = True
class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY ="secret123"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:pass123@localhost/blogsite"
    DEBUG = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:pass123@localhost/blogsite"


config_options = {
'test':TestConfig,
'development':DevConfig,
'production':ProdConfig
}