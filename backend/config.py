import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
DB_URL = os.getenv('DATABASE_URL')

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'DB_URL'
SQLALCHEMY_TRACK_MODIFICATIONS = False
