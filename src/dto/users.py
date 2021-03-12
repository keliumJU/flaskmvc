from pydantic import BaseModel

class UsersDTO(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str
    celular: str
    contrasenia: str

    class Config:
        orm_mode = True