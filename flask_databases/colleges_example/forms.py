from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of the College: ")
    submit = SubmitField("Add College")

class AddStudentForm(FlaskForm):

    name = StringField('Name of Student:')
    clg_id = IntegerField("Id of College: ")
    submit = SubmitField('Add Student')

class DelForm(FlaskForm):
    id = IntegerField("Id of the College to remove: ")
    submit = SubmitField("Delete College")