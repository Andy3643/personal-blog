from flask import Flask
from flask_bootstrap import Bootstrap



app = Flask(__name__)
bootstrap = Bootstrap()

def create_app(configname):
    """"
    method to initialize app
    """
    
    
    
    
    
    #initialize imports
    bootstrap.init_app(app)
    
    
    
    
    
    
    
    return app





