from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)
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
@app.route('/mystuff')
def account():
    my_songs =[
        {
            'title': 'Mr. Cadillac', 'artist': 'Mac Saturn'
        }
        ]
    my_notes =[
        {
            'notes amount': '10'
        }
        ]
    return render_template('account.html', title='Account Page', account=account, my_songs=my_songs, my_notes=my_notes)
