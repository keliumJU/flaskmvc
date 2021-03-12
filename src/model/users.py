from src.config.settings import * 
from flask_sqlalchemy import SQLAlchemy
from src import app
import json
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# Initializing our database
db = SQLAlchemy(app)
#Aqui deberia importar el dto

# the class User will inherit the db.Model of SQLAlchemy
class User(db.Model):
    __tablename__ = 'Users'  # creating a table name
    id=db.Column(db.Integer, primary_key=True)  # this is the primary key
    nombre=db.Column(db.String(255), nullable=False)
    apellido=db.Column(db.String(255), nullable=False)
    celular=db.Column(db.String(10), nullable=True) 
    correo=db.Column(db.String(255), nullable=False)
    contrasenia=db.Column(db.String(255), nullable=False)

    def json(self):
        return {'id': self.id, 'nombre': self.nombre,
                'apellido': self.apellido, 'celular': self.celular,
                'correo': self.correo, 'contrasenia': self.contrasenia}
        # this method we are defining will convert our output to json
    def add_user(self, _nombre, _apellido, _correo, _contrasenia, _celular="None"):
        '''function to add User to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our User constructor
        new_user = User(nombre=_nombre, apellido=_apellido, celular=_celular, correo=_correo, contrasenia=_contrasenia)
        db.session.add(new_user)  # add new user to database session
        db.session.commit()  # commit changes to session

    def get_all_users(self):
        '''function to get all users in our database'''
        return [User.json(user) for user in User.query.all()]

    def get_user(self, _id):
        '''function to get user using the id of the User as parameter'''
        return [User.json(User.query.filter_by(id=_id).first())]
        # User.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_user(self, _id, _nombre, _apellido,_correo, _contrasenia, _celular="None"):
        '''function to update the details of a user using the id, title,
        year and genre as parameters'''
        user_to_update = User.query.filter_by(id=_id).first()
        user_to_update.nombre= _nombre
        user_to_update.apellido= _apellido
        user_to_update.celular= _celular
        user_to_update.correo= _correo
        user_to_update.contrasenia= _contrasenia
        db.session.commit()

    def delete_user(self, _id):
        '''function to delete a user from our database using
           the id of the user as a parameter'''
        User.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database

db.create_all()
db.session.commit()