class CamposDTO():
    field:str
    type_column:str
    null_column:str
    key:str
    default:str
    extra:str
    def __init__(self,field,type_column,null_column,key,default,extra):
        self.field=field
        self.type_column=type_column
        self.null_column=null_column
        self.key=key
        self.default=default
        self.extra=extra

    def __str__(self):
        return ("{} {} {} {} {} {}".format(self.field, self.type_column, self.extra, self.null_column, self.key, self.default))

class TableDTO():
    name:str
    campos:[{CamposDTO}]
    def __init__(self,name,campos):
        self.name=name,
        self.campos=campos
    def __str__(self):
        return "{}".format(self.name)