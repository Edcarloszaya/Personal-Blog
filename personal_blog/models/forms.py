from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired

class EditPost(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    published_date = StringField('published_date', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Update')

class NewPost(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    published_date = StringField('published_date', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Publish')

class User(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

