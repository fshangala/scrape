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
def get_jobs(page:int=1, per_page:int=10, db:Session = Depends(get_db)):
  offset=(page-1)*per_page
  limit=per_page
  return crud.get_jobs(db, offset=offset, limit=limit)

@app.get("/jobs/search-skill/", response_model=list[schemas.Job])
def get_jobs_by_skill(skill:str="", page:int=1, per_page:int=10, db:Session = Depends(get_db)):
  offset=(page-1)*per_page
  limit=per_page
  return crud.get_job_by_technology(db, skill, offset=offset, limit=limit)

@app.get("/jobs/search-location/", response_model=list[schemas.Job])
def get_jobs_by_location(location:str="", page:int=1, per_page:int=10, db:Session = Depends(get_db)):
  offset=(page-1)*per_page
  limit=per_page
  return crud.get_job_by_location(db, location, offset=offset, limit=limit)
