from wtforms import TextAreaField,StringField,SubmitField
from . import main
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from ..models import Comment,Article

class UploadBlogForm(FlaskForm):
    article = TextAreaField('Article',validators=[DataRequired()])
    category = StringField('Title',validators=[DataRequired()])
    submit = SubmitField('Add Article')

class CommentsForm(FlaskForm):
    comment = TextAreaField('comment on the article',validators=[DataRequired()])
    submit = SubmitField('Add Comment')

class UpdateProfile(FlaskForm):
    bio = StringField('About You',validators=[DataRequired()])
    submit = SubmitField('Add Bio')
