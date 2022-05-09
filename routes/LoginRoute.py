from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/login")

# Class model for users
class User(BaseModel):
    usuario: str
    password: str

# Hard code for login validation test
db = {
        "Users":[
            User(usuario="admin", password="admin"), 
            User(usuario="user", password="user"),
            User(usuario="maori", password="12345"),
            User(usuario="pixeon", password="pixeon")
            ],

        "LoggedUser": {} 
    }

# Login endpoint
@router.post("/", tags=["login"])
async def login(user: User):
    if(user in db["Users"]):
        db["LoggedUser"] = user
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Login failed")