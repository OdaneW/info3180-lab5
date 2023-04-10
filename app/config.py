import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    SECRET_KEY = os.environ.get('SECRET_KEY', '616a1b5b4a5952ca6678d59346afff630668f169fad4f598ca7be9b2111331d3')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:tanneik123@localhost/lab5')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed