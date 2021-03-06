from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import configure_uploads,IMAGES,UploadSet

app = Flask(__name__)
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    '''
    Method for creating the app to enable for easier configurations
    '''
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    #Importing BluePrints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    #Initialising the Importations
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # configure UploadSet
    configure_uploads(app,photos)

    return app
