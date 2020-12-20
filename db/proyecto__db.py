from pydantic import BaseModel
from typing import Dict 

class ProyectoInDB(BaseModel):
    nombreP: str
    actividadP: str
    lider:str
    

database_proyecto = Dict[str, ProyectoInDB]

database_proyecto = {
    "Actualización sistema contable": ProyectoInDB(**{"nombreP":"Actualización sistema contable",
                                                      "actividadP":"Actualizar software con nuevos requerimientos",
                                                      "lider":"Andrés Perez"}),
    "Mercadotecnia": ProyectoInDB(**{"nombreP":"Mercadotecnia",
                                     "actividadP":"Estudiar el mercado textil",
                                     "lider":"Juan Lopez"}),
    "Marketing Digital": ProyectoInDB(**{"nombreP":"Marketing Digital",
                                         "actividadP":"Reforzar publicidad en Facebook e Instagram",
                                         "lider":"Ana Fernandez"}),                       
}

def get_proyecto(nombreP: str):
    if nombreP in database_proyecto.keys():
        return database_proyecto[nombreP]
    else:
        return None

def get_proyectos():
    return database_proyecto.values()

def update_proyecto(proyecto_in_db: ProyectoInDB):
    database_proyecto[proyecto_in_db.nombreP] = proyecto_in_db
    return proyecto_in_db

   
database_proyectos = []
generator = {"id":0}

""" def save_proyecto(proyecto_in_db: ProyectoInDB):
    generator["id"] = generator["id"] + 1
    proyecto_in_db.id_Proyecto = generator["id"]
    database_proyectos.append(proyecto_in_db)
    return proyecto_in_db """

def new_proyect(n_proyect: ProyectoInDB):
    database_proyecto[n_proyect.nombreP]=n_proyect
    return n_proyect