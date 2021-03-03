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
        {{link}}
    </body>
    </html>
    ''')


@app.route('/')
def home():
    content = 'Home'
    title = 'HOME'
    link = '''
    <a href='/'>Home</a>
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''

    return html_temp.render(title=title, content=content, link=link)


@app.route('/aboutme')
def aboutme():
    content = 'Aboutme'
    title = 'ABOUTME'
    link = '''
    <a href='/'>Home</a>
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    return html_temp.render(title=title, content=content, link=link)


@app.route('/portfolio')
def portfolio():
    content = 'Portfolio'
    title = 'PORTFOLIO'
    link = '''
    <a href='/'>Home</a>
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    return html_temp.render(title=title, content=content, link=link)


@app.route('/contact')
def contact():
    content = 'Contact'
    title = 'CONTACT'
    link = '''
    <a href='/'>Home</a>
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    return html_temp.render(title=title, content=content, link=link)


@app.route('/help')
def help():
    content = 'Help'
    title = 'HELP'
    link = '''
    <a href='/'>Home</a>
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    return html_temp.render(title=title, content=content, link=link)


app.run(debug=True)
