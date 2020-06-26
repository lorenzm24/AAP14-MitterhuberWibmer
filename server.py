from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/eller')
def eller():
    return render_template('eller.html', title='Eller')

