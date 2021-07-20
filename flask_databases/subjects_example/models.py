import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Students(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # This is a one-to-many relationship
    # A student can have many subjects
    subjects = db.relationship('Subjects',backref='students',lazy='dynamic')
    # This is a one-to-one relationship
    # A student only has one college, thus uselist is False.
    # Strong assumption of 1 college per 1 student and vice versa.
    colleges = db.relationship('Colleges',backref='students',uselist=False)

    def __init__(self, name):
        # Note how a student only needs to be initalized with a name!
        self.name = name


    def __repr__(self):
        if self.colleges:
            return f"Student name is {self.name} and college is {self.colleges.name}"
        else:
            return f"Student name is {self.name} and has no college assigned yet."

    def report_subjects(self):
        print("Here are the students subjects!")
        for subj in self.subjects:
            print(subj.name)

class Subjects(db.Model):

    __tablename__ = 'subjects'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # Connect the subject to the student that has it.
    # We use students.id because __tablename__='students'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class Colleges(db.Model):

    __tablename__ = 'colleges'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use students.id because __tablename__='students'
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id