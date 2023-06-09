from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import settings

if settings.DEBUG:
  engine = create_engine(
      "sqlite:///./sql_app.db", connect_args={"check_same_thread": False}
  )
else:
  engine = create_engine(
      settings.SQLALCHEMY_DATABASE_URL
  )


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()