from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel): 
    username: str
    correo: str
    password: str

database_users = Dict[str,UserInDB]

database_users = {
   "Mabel123": UserInDB(**{ "username": "Mabel123",
                            "correo" : "mabel.olaya.perez@gmail.com",
                            "password" : "clave123"}),


"Johana456": UserInDB(**{ "username" : "Johana456",
                            "correo" : "johana.mintic@gmail.com",
                            "password" : "clave456"}),

"Santiago789": UserInDB(**{ "username" : "Santiago789",
                            "correo" : "santiagoprogramador@gmail.com",
                            "password" : "clave789"}),

"Alexis123": UserInDB(**{ "username" : "Alexis123",
                            "correo" : "alexis-tic@gmail.com",
                            "password" : "clave111"}),

"MiguelA12": UserInDB(**{ "username" : "MiguelA12",
                            "correo" : "miguelangel@gmail.com",
                            "password" : "clave0000"}),

}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
