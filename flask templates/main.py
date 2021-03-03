from flask import Flask, render_template
from jinja2 import Template
app = Flask(__name__)


@app.route('/')
def home():
    content = 'Home'
    title = 'HOME'
    return render_template('home.html', title=title, content=content)


@app.route('/aboutme')
def aboutme():
    content = 'Aboutme'
    title = 'ABOUTME'
    return render_template('home.html', title=title, content=content)


@app.route('/portfolio')
def portfolio():
    content = 'Portfolio'
    title = 'PORTFOLIO'
    return render_template('home.html', title=title, content=content)


@app.route('/contact')
def contact():
    content = 'Contact'
    title = 'CONTACT'
    return render_template('home.html', title=title, content=content)


@app.route('/help')
def help():
    content = 'Help'
    title = 'HELP'
    return render_template('home.html', title=title, content=content)


app.run(debug=True)
