from src import app
from src.controller.user import UserController
from flask import make_response, jsonify, request, Response
from src.dto.users import UsersDTO

userController=UserController()

@app.route('/users',methods=['GET'])
def get_all_users():
    users=userController.list()
    return make_response(jsonify(users),200)

@app.route('/users',methods=['POST'])
def add_user():
    '''Function to add new user to our database'''
    request_data = request.get_json()  # getting data from client

    userDTO=UsersDTO(
        request_data["nombre"],
        request_data["apellido"],
        request_data["correo"],
        request_data["celular"],
        request_data["contrasenia"]
    )
    adduser=userController.create(userDTO)

    response = Response("Usuario Agregado", 201, mimetype='application/json')
    return response

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return_value = userController.get(id)
    return jsonify(return_value)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    '''Function to edit user in our database using movie id'''
    request_data = request.get_json()
    userUpdate=UsersDTO( request_data['nombre'], request_data['apellido'], request_data['correo'], request_data['celular'], request_data['contrasenia'])
    userController.put(id, userUpdate)
    response = Response("Usuario Actulizado correctamente", status=200, mimetype='application/json')
    return response

@app.route('/users/<int:id>', methods=['DELETE'])
def remove_user(id):
    '''Function to delete user from our database'''
    userController.delete(id)
    response = Response("Usuario borrado correctamente", status=200, mimetype='application/json')
    return response

