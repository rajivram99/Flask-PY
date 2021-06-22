from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from flask import request
# Define QuoteForm below
class QuoteForm(FlaskForm):
  qauthor = StringField("Quote Author",  [validators.DataRequired(), validators.Length(min=3, max=100)])
  qstring = StringField("Quote", [validators.DataRequired(), validators.Length(min=3, max=200)])
  submit = SubmitField("Add Quote")
