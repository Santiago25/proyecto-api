from pydantic import BaseModel

class UsuarioIn(BaseModel):
    nombre: str
    correo:str
    password: str
    
class UsuarioOut(BaseModel):
    nombre: str
    