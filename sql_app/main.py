from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependancy
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/jobs/", response_model=schemas.Job)
def create_job(job:schemas.JobCreate, db:Session = Depends(get_db)):
  return crud.create_job(db, job)

@app.get("/jobs/", response_model=list[schemas.Job])
def get_jobs(db:Session = Depends(get_db)):
  return crud.get_jobs(db)