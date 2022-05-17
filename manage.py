from flask_script import Manager,Server
from app import create_app,db
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Article


app = create_app("development")

#db = SQLAlchemy()
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server(use_debugger=True))




@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=5).run(tests)
# @manager.shell
# def make_shell_context():
#     return {'db' : db,'User':User , 'Article':Article}


@manager.shell
def  add_shell_context():
    return dict(db=db,app=app,User=User,Article=Article)





if __name__ == "__main__":
    manager.run()