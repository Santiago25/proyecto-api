from db.proyecto_db import get_proyecto
from db.usuario_db import get_user 
from db.asignacion_db import AsignacionProyecto
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

@api.post("/proyect/addUser/")
async def add_uder(user: str, proyecto: str):

    user_in_db = get_user(user)
    proyecto_in_db = get_proyecto(proyecto)

    if user_in_db = None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if proyecto_in_db = None:
        raise HTTPException(status_code=404, detail="El proyecto no existe")
    asignacion_in_db = AsignacionProyecto(nombre: user, nombreP: proyecto)
    asignacion_in_db = save_asignacion(asignacion_in_db)

    return asignacion_out #Pendiente
