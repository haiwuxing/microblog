from app import app
from flask import render_template
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm();
    if form.validate_on_submit():
        flash('LOgin requested for OpenID="%s", remember_me=%s' % 
              (form.openid.data, str(form.remember_me.data)));
        return redirect('/index');
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS']);