from flask_login import login_required
from . import main
from flask import redirect,render_template




@main.route('/')
def index():
    return render_template('index.html')


@main.route('/addblog',methods = ['GET','POST'])
@login_required