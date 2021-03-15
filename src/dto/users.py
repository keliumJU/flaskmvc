class UsersDTO():
    nombre: str
    apellido: str
    correo: str
    celular: str
    contrasenia: str

    def __init__(self,nombre,apellido,correo,celular,contrasenia):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.celular=celular
        self.contrasenia=contrasenia