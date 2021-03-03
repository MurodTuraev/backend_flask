from flask import Flask
from jinja2 import Template
app = Flask(__name__)

html_temp = Template('''
    <html>
    <head>
        <title> {{title}} </title>
    </head>
    <body>
        <h1>{{content}}</h1>
        <a href='/'>Home</a>
        <a href='/aboutme'>About ME</a>
        <a href='/portfolio'>Portfolio</a>
        <a href='/contact'>Contact</a>
        <a href='/help'>Help</a>
    </body>
    </html>
    ''')


@app.route('/')
def home():
    content = 'Home'
    title = 'HOME'
    return html_temp.render(title=title, content=content)


@app.route('/aboutme')
def aboutme():
    content = 'Aboutme'
    title = 'ABOUTME'
    return html_temp.render(title=title, content=content)


@app.route('/portfolio')
def portfolio():
    content = 'Portfolio'
    title = 'PORTFOLIO'
    return html_temp.render(title=title, content=content)


@app.route('/contact')
def contact():
    content = 'Contact'
    title = 'CONTACT'
    return html_temp.render(title=title, content=content)


@app.route('/help')
def help():
    content = 'Help'
    title = 'HELP'
    return html_temp.render(title=title, content=content)


app.run(debug=True)
