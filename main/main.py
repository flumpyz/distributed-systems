from os import environ

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

import crud
import models
import schemas
from custom_queue import send_message_to_queue
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

SERVER_NAME = environ.get('NAME')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/links/", response_model=schemas.LinkInDB)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = crud.create_link(db, link)
    send_message_to_queue(db_link)
    return db_link


@app.get("/links/{link_id}", response_model=schemas.LinkInDB)
def get_link(link_id: int, db: Session = Depends(get_db)):
    db_link = crud.get_link(db, link_id=link_id)
    if link_id is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link


@app.put("/links/{link_id}", response_model=schemas.LinkInDB)
def update_link(link_id: int, link: schemas.LinkUpdate, db: Session = Depends(get_db)):
    db_link = crud.update_link(db, link_id=link_id, link_update=link)
    if link_id is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-State-Name"] = SERVER_NAME
    return response
