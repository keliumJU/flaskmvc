# importing libraries
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

from src.controller import *

def create_app():
    app.run(debug=True, port=1234)