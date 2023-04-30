from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Job(Base):
  __tablename__="jobs"
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, unique=True, index=True)
  company = Column(String, index=True)
  location = Column(String, index=True)
  posted_date = Column(String, index=True)
  description = Column(String, index=True)
  skills = Column(String, index=True)