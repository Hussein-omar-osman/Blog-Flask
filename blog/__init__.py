from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this-is-very-secret-key'
env = 'dev'
if env == 'dev':
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/blogster'
 app.debug = True
else:
 app.debug = False
 app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)
bc = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from blog import views