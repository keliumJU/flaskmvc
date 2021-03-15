# importing libraries
from flask_sqlalchemy import SQLAlchemy
from src import app

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/flaskmvc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)