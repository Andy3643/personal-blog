from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads,IMAGES,UploadSet


app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos',IMAGES)

def create_app(configname):
    """"
    method to initialize app
    """
    app.config.from_object(config_options[configname])
    
    
    
    
    #initialize imports
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    
    
    #registering blueprints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    return app





