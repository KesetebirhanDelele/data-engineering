from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID #, uuid4
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()
# db defines database which currently is a list
db: List[User] = [ 
    User(
        id=UUID("3fcdabf8-0e37-4b87-85ce-1517d17e9962"), 
        first_name="Jamila", 
        last_name="Ahmed",
        middle_name="Kemal",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("028bbb03-3dbc-4cd6-b807-9271f7ed05be"), 
        first_name="Alex", 
        last_name="Jones",
        middle_name="John",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():   # async method is used to allow pause to request data from a site # await foo() in aynchronus fashion. 
    # await foo() is used to specifiy what to get. 
    return {"message": "Hello Kc. Well done Boy"}

@app.get("/api/v1/users") # Use http://127.0.0.1:8000/api/v1/users to see in browser. Add json viewer extension to see json format.
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User): # a function that takes User which is an entity that we recieved from the request body
    db.append(user) # register a new client to the database. Note this can not be done using Web browser 
                    # and hence use Thunder Client Rest API
    return {"id": user.id} # send to the client a new id

@app.delete("/api/v1/users/{user_id}") # Deleting a user
async def delete_user(user_id: UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}") # user_id is a path variable
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )