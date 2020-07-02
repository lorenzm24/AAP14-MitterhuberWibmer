from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config ['SECRET_KEY'] = '70605307ef30f5c02ea41a995c7538dc'

news = [
    {
        'author': 'Alfred Stumfpel',
        'title': 'Schlagezeile 1',
        'content': 'DIC',
        'date_posted': '1. Juni 2020'
    },
    {
        'author': 'Eller Johannes',
        'title': 'Schlagezeile 2',
        'content': 'Schmutzzulage',
        'date_posted': '10. Juni 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', news=news)

@app.route('/about')
def eller():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')