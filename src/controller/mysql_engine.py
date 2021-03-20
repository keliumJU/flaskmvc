from src.model.mysql_engine import MysqlEngine
from src.dto.table import TableDTO
class MysqlEngineController():
    def create(self,name):
        modelmysql=MysqlEngine()
        modelmysql.create_database(name)
    def list(self):
        modelmysql=MysqlEngine()
        return modelmysql.all_databases()
    def list_tables_columns(self):
        modelMysql=MysqlEngine()
        return modelMysql.all_tables_columns()
    def create_table(self,table:TableDTO):
        modelMysql=MysqlEngine()     
        modelMysql.create_table(table)

