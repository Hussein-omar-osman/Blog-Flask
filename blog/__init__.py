from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this-is-very-secret-key'

from blog import views