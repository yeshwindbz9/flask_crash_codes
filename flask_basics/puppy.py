from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h3>go to /puppy_latin/enter_pups_name here to see the pups name in ppuppy latin!</h3>"

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y' or name[-1] == 'Y':
        latin = name[:-1] + "iful"
    else:
        latin = name + 'y'
    return f"<h3>Hi {name}, your puppy_latin name is {latin}!</h3>"

if __name__ == "__main__":
    app.run()
