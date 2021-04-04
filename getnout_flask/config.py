import os
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
SECRET_KEY = 'my precious'

# Connect to the database
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'DemoData',
    'host': 'localhost',
    'port': 27017
}
