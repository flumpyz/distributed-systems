from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def root():
#     return {"message": "Hello World!!!!!!!!!!"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


@app.post("/links/", response_model=schemas.LinkInDB)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = crud.create_link(db, link)
    return db_link


@app.post("/links/{link_id}", response_model=schemas.LinkInDB)
def get_link(link_id: int, db: Session = Depends(get_db)):
    db_link = crud.get_link(db, link_id=link_id)
    if link_id is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link
