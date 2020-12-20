from db.proyecto__db import get_proyecto, get_proyectos,ProyectoInDB, new_proyect
from db.usuario_db import get_user , UserInDB, new_user
from db.asignacion_db import AsignacionProyecto, save_asignacion
from models.asignacion_modelo import AsignacionIn, AsignacionOut
from models.proyecto_modelo import ProyectoOut, ProyectoIn
from models.usuario_modelo import UsuarioIn, UsuarioOut

import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://epyme-app.herokuapp.com"
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

""" @api.post (/usuario) """
@api.post("/usuario")
async def new_proyect_in(n_usuario: UsuarioIn):

    usuario_in_db = UserInDB(**n_usuario.dict())
    usuario_in_db = new_user(usuario_in_db)

    usuario_out = UsuarioOut(**usuario_in_db.dict())
    
    return usuario_out

""" @api.post (/proyecto) """
@api.post("/proyecto")
async def new_proyect_in(n_proyecto: ProyectoIn):

    proyecto_in_db = ProyectoInDB(**n_proyecto.dict())
    proyecto_in_db = new_proyect(proyecto_in_db)

    proyecto_out = ProyectoOut(**proyecto_in_db.dict())
    
    return proyecto_out
    
