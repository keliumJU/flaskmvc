from src.config.settings import db, conn
from sqlalchemy.sql import text
from src.dto.table import CamposDTO, TableDTO

class MysqlEngine():
    def create_database(self, name:str):
        conn.execute('create database {}'.format(name))
        conn.execute('commit')

    def all_databases(self):
        dbs=conn.execute('show databases')
        available_databases= dbs.fetchall()

        field=["name"]        
        response=[]
        for index, d in enumerate(available_databases):
            response.append({})
            for index_field, f in enumerate(field):
                response[index][field[index_field]]=d[index_field]
        
        return response
    
    def all_tables_columns(self):            
        dbs=conn.execute('show tables')
        available_tables=dbs.fetchall()

        names_tables=[name[0] for name in available_tables]
        field=["name_column"]        
        response=[]
        fields_columns=["Field","Type","Null","Key","Default","Extra"]            
        col_tmp=[]
        for index, tb in enumerate(names_tables):
            columns=conn.execute('describe '+tb).fetchall()                
            columnsJson=[col[0] for col in columns]
            response_columns=[]
            for col in columns:
                for campo in col:
                        col_tmp.append(campo)
                obj={} 
                for index, tmp in enumerate(col_tmp):                        
                    obj[fields_columns[index]]=tmp

                response_columns.append(obj)
                col_tmp=[]

            field=["name_column"]        
            response.append({"table_name":tb,"columns":response_columns})
        
        return response
            
    def create_table(self,table:TableDTO):
        nombre = str(table.name[0])
        query="CREATE TABLE {} (".format(nombre)

        for col in table.campos:
            query+=("{},".format(col))

        #eliminamos la coma sobrante
        query = query[:-1]
        query+=");"
        conn.execute(query)
        conn.execute('commit')

    def update_table(self, table:TableDTO):
        #Actualizando base de datos de la forma menos modesta posible(campiranamente)
        nombre = str(table.name[0])
        query="DROP TABLE IF EXISTS {}".format(nombre)
        conn.execute(query)
        conn.execute('commit')
        self.create_table(table)
    
    def select_database(self,name:str):
        query="use {}".format(name)
        conn.execute(query)
        conn.execute('commit')