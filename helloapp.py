from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>homepage<h1>"

@app.route("/us/<username>/")
def hello(username):
    users = ["ral","sam","arm","rajiv"]
    return render_template("index.html",title = 'Title of the page',users=users,username=username)


if __name__=="__main__":
    app.run()