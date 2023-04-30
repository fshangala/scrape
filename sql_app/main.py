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
  db_job=crud.get_job_by_title(db, title=job.title)
  if db_job:
    raise HTTPException(400,detail="Job with that title already exists.")
  return crud.create_job(db, job)

@app.get("/jobs/", response_model=list[schemas.Job])
def get_jobs(db:Session = Depends(get_db)):
  return crud.get_jobs(db)