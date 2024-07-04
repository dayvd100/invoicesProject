from fastapi import FastAPI
from .users.routes.users import router_users
from .database.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}


app.include_router(router_users)
