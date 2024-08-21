from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/Posts/", response_model=schemas.Post)
def create_Post(Post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_Post(db=db, Post=Post)

@app.get("/Posts/{Post_id}", response_model=schemas.Post)
def read_Post(Post_id: int, db: Session = Depends(get_db)):
    db_Post = crud.get_Post(db, Post_id=Post_id)
    if db_Post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_Post

@app.get("/Posts/", response_model=list[schemas.Post])
def read_Posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    Posts = crud.get_Posts(db, skip=skip, limit=limit)
    return Posts

