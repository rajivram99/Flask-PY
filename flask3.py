#dynamic URL 

from flask import Flask
from flask import redirect
from flask import url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/user/<username>")
def hello_user(username):
    return "redirected..<br>Welcome "+username



@app.route("/greet/user/<uname>/")
def redirect_urlfor(uname):
    return redirect(url_for('hello_user',username=uname))

if __name__ =="__main__":
    app.run()

#greet_user func redirects URL /greet/user/xxx to /user/xx