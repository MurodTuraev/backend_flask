from flask import Flask, render_template
from jinja2 import Template
app = Flask(__name__)


@app.route('/')
def home():
    content = 'Home'
    title = 'HOME'
    img = 'uz.png'
    return render_template('home.html', title=title, content=content, img=img)


@app.route('/aboutme')
def aboutme():
    content = 'Aboutme'
    title = 'ABOUTME'
    img = 'uz.png'
    return render_template('home.html', title=title, content=content, img=img)


@app.route('/portfolio')
def portfolio():
    content = 'Portfolio'
    title = 'PORTFOLIO'
    img = 'ru.png'
    return render_template('home.html', title=title, content=content, img=img)


@app.route('/contact')
def contact():
    content = 'Contact'
    title = 'CONTACT'
    img = 'kz.png'
    return render_template('home.html', title=title, content=content, img=img)


@app.route('/help')
def help():
    content = 'Help'
    title = 'HELP'
    img = 'us.png'
    return render_template('home.html', title=title, content=content, img=img)


app.run(debug=True)
