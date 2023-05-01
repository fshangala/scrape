from sqlalchemy.orm import Session
from . import models, schemas

def create_job(db:Session, job:schemas.JobCreate):
  db_job=models.Job(
    title=job.title,
    company=job.company,
    location=job.location,
    posted_date=job.posted_date,
    description=job.description,
    skills=job.skills
  )
  db.add(db_job)
  db.commit()
  db.refresh(db_job)
  return db_job

def get_jobs(db:Session, offset:int=0, limit:int=10):
  return db.query(models.Job).offset(offset).limit(limit).all()

def get_job_by_title(db:Session, title:str):
  return db.query(models.Job).filter(models.Job.title==title).first()

def get_job_by_technology(db:Session, skills:str, offset:int=0, limit:int=10):
  return db.query(models.Job).filter(models.Job.skills.like(f"%{skills}%")).offset(offset).limit(limit).all()

def get_job_by_location(db:Session, location:str, offset:int=0, limit:int=10):
  return db.query(models.Job).filter(models.Job.location.like(f"%{location}%")).offset(offset).limit(limit).all()