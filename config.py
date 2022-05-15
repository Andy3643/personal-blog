import os
class Config:
    '''
    General configuration settings
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SECRET_KEY="secret123"
    #SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:paswaad@localhost/blogsite"
    DEBUG = True
class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY ="secret123"
    #SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:paswaad@localhost/blogsite"



class TestConfig(Config):
    SECRET_KEY="testkeyintestconfig"
    #SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:paswaad@localhost/blogsite"

configurations = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
}