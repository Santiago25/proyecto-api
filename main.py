from db.proyecto__db import get_proyecto
from db.usuario_db import get_user 
from db.asignacion_db import AsignacionProyecto
from db.asignacion_db import save_asignacion
from models.asignacion_modelo import AsignacionIn
from models.asignacion_modelo import AsignacionOut
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

@api.post("/proyect/addUser/")
async def add_user(asign_user: AsignacionIn):

    user_in_db = get_user(asign_user.nombre)
    proyecto_in_db = get_proyecto(asign_user.nombreP)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if proyecto_in_db == None:
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    asignacion_in_db = AsignacionProyecto(**asign_user.dict())
    asignacion_in_db = save_asignacion(asignacion_in_db)

    asignacion_out = AsignacionOut(**asignacion_in_db.dict())
    
    return asignacion_out
