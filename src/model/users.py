from src.dto.users import UsersDTO
from src.config.settings import db
# Initializing our database
#Aqui deberia importar el dto

# the class User will inherit the db.Model of SQLAlchemy
class UserModel(db.Model):
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

        #Debe recibir un dto como parametro? un dto con typado statico 
    def add_user(self, user: UsersDTO):
        '''function to add User to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our User constructor
        new_user = UserModel(nombre=user.nombre, apellido=user.apellido, celular=user.celular, correo=user.correo, contrasenia=user.contrasenia)
        db.session.add(new_user)  # add new user to database session
        db.session.commit()  # commit changes to session

    def get_all_users(self):
        '''function to get all users in our database'''
        #Debo retornar una lista de UsersDTO?
        return [UserModel.json(user) for user in UserModel.query.all()]

    def get_user(self, _id):
        '''function to get user using the id of the User as parameter'''
        #Deberia retornar un UsersDTO?
        return [UserModel.json(UserModel.query.filter_by(id=_id).first())]
        # User.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_user(self, _id, user:UsersDTO):
        '''function to update the details of a user using the id, title,
        year and genre as parameters'''
        user_to_update = UserModel.query.filter_by(id=_id).first()
        user_to_update.nombre= user.nombre 
        user_to_update.apellido=user.apellido 
        user_to_update.celular=user.celular 
        user_to_update.correo=user.correo 
        user_to_update.contrasenia=user.contrasenia 
        db.session.commit()

    def delete_user(self, _id):
        '''function to delete a user from our database using
           the id of the user as a parameter'''
        UserModel.query.filter_by(id=_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database

db.create_all()
db.session.commit()