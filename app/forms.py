from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    description = TextAreaField('description', validators=[InputRequired()])
    poster = FileField('poster', validators=[InputRequired()])