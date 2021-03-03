from flask import Flask
app = Flask(__name__)

html = "<h1>HTML</h1>"


@app.route('/')
def home():
    return html


@app.route('/aboutme')
def aboutme():
    return 'About ME'


@app.route('/portfolio')
def portfolio():
    return 'portfolio'


@app.route('/help')
def help():
    return html


app.run(debug=True)
