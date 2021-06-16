from flask import Flask
from flask import redirect
app = Flask(__name__)

#redirect to home function using redirects lib
@app.route("/home/")
def redirect_home():
    return redirect("http://localhost:5000/")

#simple execution
@app.route("/")
def hello():
    return "hello world from flask"

#parameterized function calls
@app.route("/user/<username>/")   
def helloUser(username):
    return "hello "+username+" Welcome to the website"

#double parameters
@app.route("/user/<username>/<int:age>/")
def UserAge(username,age):
    return "hello "+username+"!! <br>Your age is "+str(age)

#main
if __name__ =="__main__":
    app.run()

