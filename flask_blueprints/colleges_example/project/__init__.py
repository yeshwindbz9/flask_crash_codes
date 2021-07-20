import os
from flask import Flask
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

from project.colleges.views import colleges_blueprint
from project.students.views import students_blueprint
app.register_blueprint(colleges_blueprint, url_prefix="/colleges")
app.register_blueprint(students_blueprint, url_prefix="/students")
