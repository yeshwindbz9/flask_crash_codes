from flask import Flask
app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
    return "<h1>HelloWorld!</h1>"

@app.route("/info") # 127.0.0.1:5000/info
def info():
    return "<h3>This is a webpage created using Flask!</h3>"

@app.route("/dynamic/<user>")
def dynamic(user):
    return f"<h3>Demonstrating a dynamic route for {user.upper()}</h3>"

if __name__ == "__main__":
    app.run()