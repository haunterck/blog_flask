from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# Imports our configuration data
from config import Configuration

app = Flask(__name__)
# Use values from Configuration class
app.config.from_object(Configuration)
db = SQLAlchemy(app)
