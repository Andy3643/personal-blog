from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options



app = Flask(__name__)
bootstrap = Bootstrap()

def create_app(configname):
    """"
    method to initialize app
    """
    app.config.from_object(config_options[configname])
    
    
    
    
    #initialize imports
    bootstrap.init_app(app)
    
    
    
    
    
    
    
    return app





