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


@main.route('/articlediscussion/<int:article_id>/comment',methods=['POST','GET'])
@login_required
def comment(article_id):
    current_article = Article.query.filter_by(id = article_id).first()
    if request.method == "POST":
        comment = request.form.get("comment")
        new_comment = Comment(comment = comment,user = current_user,article = current_article)
        db.session.add(new_comment)
        db.session.commit()
    article = Article.query.get_or_404(article_id)
    comments = Comment.get_comments(article_id)

    title = 'Article Discussion'
    return render_template('blogdiscussion.html',title = title,article = article,comments=comments)
