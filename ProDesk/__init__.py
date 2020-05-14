from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = "c96418b075871ec41adaea54fee6f4ac"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eyjbdhslylxxcw:2537e4a98d96a2fb95dd659505126f8a23b469000a1b130d68a8ea5493e3ae93@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d3s5ievnk6355i'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # function name of our route like url_for
login_manager.login_message_category = 'info'  # bootstrap class

from ProDesk import routes
