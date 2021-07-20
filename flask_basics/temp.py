from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    var = "yeshw" # for jinja template
    l = list(var)
    d = {"yeshw": "best", "rest": "everyone else..."}
    return render_template("temp.html", my_variable = var, l=l, d=d)

if __name__ == "__main__":
    app.run()