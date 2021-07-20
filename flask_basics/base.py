from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route("/content")
def content():
    first = request.args.get('first')
    last = request.args.get('last')
    username = request.args.get('username')
    flagU, flagL, flagN = 0, 0, 0
    errors = []
    for char in username:
        if char.isupper():
            flagU = 1
        elif char.islower():
            flagL = 1
    if username[-1].isnumeric():
        flagN = 1
    if flagU == flagL == flagN == 1:
        return render_template("content.html", first=first, last=last)
    if flagU == 0:
        errors.append("You did not use an uppercase character.")
    if flagL == 0:
        errors.append("You did not use an lowercase character.")
    if flagN == 0:
        errors.append("You did not use a number at the end.")
    return render_template("error.html", errors=errors)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()