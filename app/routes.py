from flask import render_template
from app import app

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
            'title': 'Mr. Cadillac', 'artist': 'Mac Saturn'
        },
        {
            'title': 'Light My Love', 'artist':'Greta Van Fleet'
        }
        ]
    return render_template('songs.html', title='Song Page', songs=songs)
