from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this-is-very-secret-key'
env = 'prod'
if env == 'dev':
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/blogster'
 app.debug = True
else:
 app.debug = False
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bxvekjlojagsuc:000b96f0d93b4757f252946e13be05a5bc33f1834d7a1424cdcc44630ffaa294@ec2-52-86-115-245.compute-1.amazonaws.com:5432/d4kv5jhtnd6orl'

db = SQLAlchemy(app)
bc = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from blog import views