# importing libraries
from flask_sqlalchemy import SQLAlchemy
from src import app

import sqlalchemy
from sqlalchemy import create_engine
#from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
#from sqlalchemy import inspect


# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/flaskmvc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
engine=create_engine('mysql+mysqlconnector://root:@localhost:3306/flaskmvc')
conn=engine.connect()
conn.execute("commit")