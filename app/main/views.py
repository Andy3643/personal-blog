from flask_login import login_required
from . import main
from flask import redirect,render_template,url_for
from .forms import UploadBlogForm,CommentsForm,UpdateProfile



@main.route('/')
def index():
    return render_template('index.html')


@main.route('/addblog',methods = ['GET','POST'])
@login_required
def add_article():
    form = UploadBlogForm()
    if form.validate_on_submit():
        article = form.article.data
        category = form.category.data
        new_article = Article(article = article,category = category,user = current_user)
        new_article.save_article()
        return redirect(url_for('.index'))
    title = 'Add a article'
    return render_template('newblog.html',title = title,articleform = form)
