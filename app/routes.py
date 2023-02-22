from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Valentina'}
    posts = [
        {
            'author': {'username': 'Chris'},
            'body': 'Computer science is fun!'
        },
        {
            'author': {'username': 'Judy'},
            'body': 'I am feeling tired right now.'
        }
    ]
 return render_template("index.html", title='Home Page', posts=posts)
@app.route('/songs')
def songs():
    songs =[
        {
            'title': 'Mr. Cadillac', 'artist': 'Mac Saturn','price': '5 notes'
        },
        {
            'title': 'Light My Love', 'artist':'Greta Van Fleet','price': '5 notes'
        }
        ]
    return render_template('songs.html', title='Song Page', songs=songs)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
@app.route('/account')
def account():
    account=[
        {
            'title': 'Mr. Cadillac', 'artist': 'Mac Saturn'
        },
        {
            'my notes amount': '10'
        }
        ]

    return render_template('account.html', title='Account Page', account=account)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
