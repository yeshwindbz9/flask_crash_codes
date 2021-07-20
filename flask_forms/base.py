from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                        RadioField, SelectField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "pass_123"

class InfoForm(FlaskForm):

    name = StringField("What should we call you?", validators=[DataRequired()])
    student = BooleanField("Are you a student?")
    mood = RadioField("Select your mood: ", choices=[
        ("mood_one", "Happy"), ("mood_two", "Exicted")])
    food_choice = SelectField("Select your favourite food:", choices=[
        ("veg", "VEG"), ("non_veg", "Non-Veg")])
    feedback = TextAreaField()
    submit = SubmitField("Submit")

@app.route('/', methods=["GET", "POST"])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        session["student"] = form.student.data
        session["mood"] = form.mood.data
        session["food_choice"] = form.food_choice.data
        session["feedback"] = form.feedback.data
        flash(f"Hi, {form.name.data} Thanks for filling out the survey!")
        if form.feedback.data:
            flash("Feedback recieved!")

        return redirect(url_for("success"))
    return render_template("index.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)