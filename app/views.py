from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}; # fake user
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beutiful day in Porland!'
            },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avergers movie was so cool!'
            }
        ]
    return render_template('index.html',
                        title='Home',
                        user=user,
                        posts=posts);