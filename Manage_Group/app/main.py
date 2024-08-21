from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, group, react
from . import models
from .database import engine

#sqlalchemy check if table has already exist, if not exist then create a new table
#alembic check if table, column has already exist, if not exist then create a new table, new column

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/Welcome")
async def root():
    return {"message": "Welcome to the FastAPI blog !"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(react.router)
app.include_router(group.router)
