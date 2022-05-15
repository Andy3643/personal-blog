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
    
    
    #registering blueprints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    
    
    
    
    return app





