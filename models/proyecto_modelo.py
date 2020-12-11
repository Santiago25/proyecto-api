from pydantic import BaseModel
from datetime import datetime

class ProyectoIn(BaseModel):
    nombreP: str
    actividadP: str
    lider:str

class ProyectoOut(BaseModel):
    id_Proyecto: int
    usuarios: []
    date: datetime
    actividad: str
    