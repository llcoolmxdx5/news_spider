import os
from flask import Flask
from news.settings import FLASK_HOST, FLASK_PORT

__all__ = ['app']

app = Flask(__name__)
@app.route('/')
def index():
    return '<h2>Welcome to News Spider System</h2>'

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT)
