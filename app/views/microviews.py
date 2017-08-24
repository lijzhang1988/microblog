from flask import render_template
from app import app
from app.views.forms import LoginForm



@app.route('/')
@app.route('/login')
def login():
    form = LoginForm()
    template_neame = 'login.html'
    return render_template(template_neame,title='Sign In',form=form)