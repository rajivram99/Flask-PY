from flask import render_template
import random
from .models import Quotes
from .forms import QuoteForm
from helloapp import app, db
from flask import request


#only core logic present here

@app.route('/')
def hello():
    return render_template('index.html')
…  if request.method == 'POST':
    user = Quotes(quoteauthor=form.qauthor.data, quotestring=form.qstring.data)
    try:
      db.session.add(user)
      db.session.commit()
    except Exception:
      db.session.rollback()
    return render_template('addquote_confirmation.html',title = 'Add User Confirmation', authorname=form.qauthor.data)
  return render_template('addquote.html', title = 'User Input Form', form = form)
