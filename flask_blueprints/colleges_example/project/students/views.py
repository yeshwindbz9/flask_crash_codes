from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Students
from project.students.forms import AddForm

students_blueprint = Blueprint("students", __name__, template_folder="templates/students")

@students_blueprint.route("/add", methods=['GET', 'POST'])
def add_stu():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        clg_id = form.clg_id.data
        # Add new student to database
        new_stu = Students(name,clg_id)
        db.session.add(new_stu)
        db.session.commit()
        return redirect(url_for('colleges.list_clg'))
    return render_template('add_stu.html',form=form)