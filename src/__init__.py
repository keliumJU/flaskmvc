# importing libraries
from flask import Flask

app = Flask(__name__)

from src.controller import *
from src.routes import *
from src.config import *

def create_app():
    app.run(debug=True, port=1234)