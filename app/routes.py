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
