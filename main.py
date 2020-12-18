from db.proyecto__db import get_proyecto, get_proyectos
from db.usuario_db import get_user 
from db.asignacion_db import AsignacionProyecto
from db.asignacion_db import save_asignacion
from models.asignacion_modelo import AsignacionIn
from models.asignacion_modelo import AsignacionOut
from models.proyecto_modelo import ProyectoOut, ProyectoIn

import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://epyme-app.herokuapp.com/",
    "https://epyme-app.herokuapp.com/proyectos"
]

api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

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

@api.get("/proyect/list")
async def proyects_list():
    proyects_in_db= get_proyectos()
    proyects_out= []
    for proyect in proyects_in_db:
        proyect_out= ProyectoOut(**proyect.dict())
        proyects_out.append(proyect_out)
    return proyects_out
