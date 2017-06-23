import os

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from webapp.database import init_db

from webapp.user import user
from webapp.article import article

app = Flask(__name__)
import webapp.views

app.register_blueprint(user)
app.register_blueprint(article)

init_db()

