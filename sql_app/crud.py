from sqlalchemy.orm import Session
from . import models, schemas

def create_job(db:Session, job:schemas.JobCreate):
  db_job=models.Job(
    title=job.title,
  )
  db.add(db_job)
  db.commit()
  db.refresh(db_job)
  return db_job

def get_jobs(db:Session):
  return db.query(models.Job).all()