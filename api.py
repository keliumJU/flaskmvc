from users import * 

# route to get all movies
@app.route('/users', methods=['GET'])
def get_users():
    '''Function to get all the movies in the database'''
    return jsonify({'Users': User().get_all_users()})


# route to get movie by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return_value = User().get_user(id)
    return jsonify(return_value)


# route to add new movie
@app.route('/users', methods=['POST'])
def add_user():
    '''Function to add new user to our database'''
    request_data = request.get_json()  # getting data from client
    User().add_user(request_data["nombre"], request_data["apellido"],
                    request_data["correo"], request_data["contrasenia"],request_data["celular"])
    response = Response("Usuario Agregado", 201, mimetype='application/json')
    return response


# route to update movie with PUT method
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    '''Function to edit user in our database using movie id'''
    request_data = request.get_json()
    User().update_user(id, request_data['nombre'], request_data['apellido'], request_data['correo'], request_data['contrasenia'], request_data['celular'])
    response = Response("Usuario Actulizado correctamente", status=200, mimetype='application/json')
    return response


# route to delete movie using the DELETE method
@app.route('/users/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete user from our database'''
    User().delete_user(id)
    response = Response("Usuario borrado correctamente", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)
