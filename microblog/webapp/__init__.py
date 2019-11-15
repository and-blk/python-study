from flask import Flask
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from webapp.dataprocessing import DataProcessing


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
login = LoginManager(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from webapp import routes, models

