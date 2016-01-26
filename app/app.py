from flask import Flask
# Imports our configuration data
from config import Configuration

app = Flask(__name__)
# Use values from Configuration class
app.config.from_object(Configuration)
