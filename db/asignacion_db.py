from typing import  Dict
from pydantic import BaseModel

class AsignacionProyecto(BaseModel):
    idAsignacion: int
    nombre: str
    nombreP: str

asignaciones_db = []
generator = {"id": 0}

def save_asignacion(asignacion: AsignacionProyecto):
    generator["id"] = generator["id"] + 1
    AsignacionProyecto.idAsignacion = generator["id"]
    asignaciones_db.append(asignacion)
    return asignacion
