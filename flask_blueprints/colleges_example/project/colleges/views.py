from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Colleges
from project.colleges.forms import AddForm, DelForm

colleges_blueprint = Blueprint("colleges", __name__, template_folder="templates/colleges")

@colleges_blueprint.route("/add", methods=["GET", "POST"])
def add_clg():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_clg = Colleges(name)
        db.session.add(new_clg)
        db.session.commit()
        return redirect(url_for("colleges.list_clg"))
    return render_template("add.html", form=form)

@colleges_blueprint.route("/delete", methods=["GET", "POST"])
def del_clg():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        clg = Colleges.query.get(id)
        db.session.delete(clg)
        db.session.commit()
        return redirect(url_for("colleges.list_clg"))
    return render_template("delete.html", form=form)

@colleges_blueprint.route("/list")
def list_clg():
    colleges = Colleges.query.all()
    return render_template("list.html", colleges=colleges)