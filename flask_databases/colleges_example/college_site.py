import os
from forms import AddForm, DelForm, AddStudentForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "pass_123"

# sql database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

# models
class Colleges(db.Model):

    __tablename__ = 'colleges'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    student = db.relationship('Students',backref='colleges',uselist=False)

    def __init__(self, name):
        # Note how a college only needs to be initalized with a name!
        self.name = name

    def __repr__(self):
        if self.student:
            return f"Student {self.student.name} is from College {self.name}"
        else:
            return f"College {self.name}."

class Students(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    clg_id = db.Column(db.Integer,db.ForeignKey('colleges.id'))

    def __init__(self,name,clg_id):
        self.name = name
        self.clg_id = clg_id

    def __repr__(self):
        return f"Student Name: {self.name}"

# view functions with forms

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
def add_clg():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_clg = Colleges(name)
        db.session.add(new_clg)
        db.session.commit()
        return redirect(url_for("list_clg"))
    return render_template("add.html", form=form)

@app.route("/delete", methods=["GET", "POST"])
def del_clg():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        clg = Colleges.query.get(id)
        db.session.delete(clg)
        db.session.commit()
        return redirect(url_for("list_clg"))
    return render_template("delete.html", form=form)

@app.route('/add_stu', methods=['GET', 'POST'])
def add_stu():
    form = AddStudentForm()
    if form.validate_on_submit():
        name = form.name.data
        clg_id = form.clg_id.data
        # Add new student to database
        new_stu = Students(name,clg_id)
        db.session.add(new_stu)
        db.session.commit()
        return redirect(url_for('list_clg'))
    return render_template('add_stu.html',form=form)

@app.route("/list")
def list_clg():
    colleges = Colleges.query.all()
    return render_template("list.html", colleges=colleges)

if __name__ == "__main__":
    app.run(debug=True)