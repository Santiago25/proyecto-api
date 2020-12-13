from pydantic import BaseModel
from datetime import datetime

class ProyectoIn(BaseModel):
    nombreP: str
    actividadP: str
    lider:str

class ProyectoOut(BaseModel):
    nombreP: str
    actividadP: str
    lider: str
    