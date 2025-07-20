from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    #== Fake posts in view function ==
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
            'age': 25
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!',
            'age': 30
        }
        
    ]
    return render_template('index.html', title='Home Page', user=user, posts = posts)