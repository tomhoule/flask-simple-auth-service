from flask import Flask, g
import sqlalchemy
import os
from dotenv import load_dotenv
from auth_service.routes import auth
from logging import StreamHandler
import sys

# Load environment variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Configuration
DB_URL = os.environ["DB_URL"]
DEBUG = os.environ.get("DEBUG", default=None) == "1"
SECRET_KEY = os.environ["SECRET_KEY"]

# Populate the app object
app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(auth, url_prefix='/api/v1/')

# Configure the app logger
app.logger.addHandler(StreamHandler(stream=sys.stdout))

engine = sqlalchemy.create_engine(DB_URL)


@app.before_request
def before_request():
    g.db = engine.connect()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
