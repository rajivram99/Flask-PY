from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html",title = 'Title of the page-home')

@app.route("/us/<username>/")
def hello(username):
    return render_template("index.html",title = 'Title of the page-username',user=username)

@app.route("/us/allusers/") 
def allusers():
    users=["aa","bb","cc","dd"]
    return render_template("users.html",title = 'Title of the page-allusers',user=users)   


if __name__=="__main__":
    app.run()