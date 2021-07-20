from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# secret key for security
app.config["SECRET_KEY"] = "pass_1234"

# create a class of wtform
class InfoForm(FlaskForm):
    name = StringField("What should we call you as?")
    submit = SubmitField("Proceed")

@app.route('/', methods=["GET", "POST"])
def index():
    name = False
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("sampleform.html", form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True)