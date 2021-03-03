from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    content = 'Home'
    title = 'HOME'
    link = '''
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    html_temp = f'''
    <html>
    <head>
        <title> {title} </title>
    </head>
    <body>
        <h1>{content}</h1>
        {link}
    </body>
    </html>
    '''
    return html_temp


@app.route('/aboutme')
def aboutme():
    content = 'Aboutme'
    title = 'ABOUTME'
    link = '''
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    html_temp = f'''
    <html>
    <head>
        <title> {title} </title>
    </head>
    <body>
        <h1>{content}</h1>
        {link}
    </body>
    </html>
    '''
    return html_temp


@app.route('/portfolio')
def portfolio():
    content = 'Portfolio'
    title = 'PORTFOLIO'
    link = '''
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    html_temp = f'''
    <html>
    <head>
        <title> {title} </title>
    </head>
    <body>
        <h1>{content}</h1>
        {link}
    </body>
    </html>
    '''
    return html_temp


@app.route('/contact')
def contact():
    content = 'Contact'
    title = 'CONTACT'
    link = '''
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    html_temp = f'''
    <html>
    <head>
        <title> {title} </title>
    </head>
    <body>
        <h1>{content}</h1>
        {link}
    </body>
    </html>
    '''
    return html_temp


@app.route('/help')
def help():
    content = 'Help'
    title = 'HELP'
    link = '''
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    html_temp = f'''
    <html>
    <head>
        <title> {title} </title>
    </head>
    <body>
        <h1>{content}</h1>
        {link}
    </body>
    </html>
    '''
    return html_temp


app.run(debug=True)
