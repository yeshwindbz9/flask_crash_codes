from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Student:')
    clg_id = IntegerField("Id of College: ")
    submit = SubmitField('Add Student')