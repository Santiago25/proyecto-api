from pydantic import BaseModel

class UsuarioIn(BaseModel):
    username: str
    correo:str
    password: str
    
class UsuarioOut(BaseModel):
    username: str
    
