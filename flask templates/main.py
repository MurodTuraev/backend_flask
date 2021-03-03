from flask import Flask
app = Flask(__name__)

html = "<h1>HTML</h1>"


@app.route('/')
def home():
    link = '''
    <a href='/aboutme'>About ME</a>
    <a href='/portfolio'>Portfolio</a>
    <a href='/contact'>Contact</a>
    <a href='/help'>Help</a>
    '''
    return link


@app.route('/aboutme')
def aboutme():
    return 'About ME'


@app.route('/portfolio')
def portfolio():
    return 'portfolio'


@app.route('/contact')
def contact():
    return 'Contact'


@app.route('/help')
def help():
    return html


app.run(debug=True)
