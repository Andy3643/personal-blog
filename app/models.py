from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    data base for users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique = True,nullable = False)
    email = db.Column(db.String,unique = True,nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    article = db.relationship('Article',backref='user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    password_hash = db.Column(db.String,nullable=False)
    
    
    @property
    def password(self):
        '''
        prevent user from viewing password
        '''
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self,password):
        '''
        Generates password hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        '''
        confirms password equal to the password hash during login
        '''
        check_password_hash(self.password_hash,password)
