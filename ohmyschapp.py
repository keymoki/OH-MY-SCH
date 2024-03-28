import flask
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('homepage.html', name=__name__)

if __name__ == '__main__':
    app.run(debug=True)