from src import app
from src.controller.mysql_engine import MysqlEngineController
from flask import make_response, jsonify, request, Response
from src.dto.table import CamposDTO, TableDTO

mysqlEngineController=MysqlEngineController()

@app.route('/mysql_engine',methods=['POST'])
def create_db_route(name):
    mysqlEngineController.create(name)
    return Response("Base de datos creada",status=201,mimetype='application/json')

@app.route('/mysql_engine',methods=['GET'])
def all_databases_route():
    databases=mysqlEngineController.list()
    return make_response(jsonify(databases),200)

@app.route('/mysql_engine/all',methods=['GET']) 
def all():
    all_db=mysqlEngineController.list_tables_columns()
    return make_response(jsonify(all_db),201)

@app.route('/mysql_engine/table',methods=['POST'])
def create_table_route():
    request_data = request.get_json()  # getting data from client

    allCampos=[]
    for campos in request_data["campos"]:
        camposDTO=CamposDTO(
                campos["field"],
                campos["type_column"],
                campos["null_column"],
                campos["key"],
                campos["default"],
                campos["extra"]
        )
        allCampos.append(camposDTO)
    tableDTO=TableDTO(
        request_data["name"],
        allCampos 
    )
    mysqlEngineController.create_table(tableDTO)
    return make_response('tabla creada satisfactoriamente',201)
