from pydantic import BaseModel

class AsignacionIn(BaseModel):
    nombre: str
    nombreP:str
    
    
class AsignacionOut(BaseModel):
    idAsignacion: int
    nombre: str
    nombreP: str