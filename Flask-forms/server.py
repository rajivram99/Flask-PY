from flask import Flask,render_template
app=Flask(__name__)
app.config['SECRET_KEY'] = 'rage'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class SignUpForm(FlaskForm):
   fname = StringField("First Name",  [validators.DataRequired(), validators.Length(min=3, max=100)])
   lname = StringField("Last Name", [validators.DataRequired(), validators.Length(min=3, max=100)])
   email = StringField("Email", [validators.DataRequired(), validators.Email("Please provide a valid email address.")])
   submit = SubmitField("Submit")    
    
@app.route("/")
def home():
    return "hello world"

@app.route("/about/")
def about():
    return "about page"

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/blog/<int:blog_id>/")
def blogpost(blog_id):
    return "the blog id is"

@app.route("/signup")
def signup():
    form = SignUpForm()
    return render_template("signup.html",form =form)

if __name__ == "__main__":
    app.run()