from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL= os.getenv('DATABASE_URL')

engine= create_engine(DATABASE_URL)

SessionLocal= sessionmaker(bind=engine, autoflush=False, autocommit=False)
metadata= MetaData()

Base= declarative_base()

def get_db():
  db= SessionLocal()
  try:
    yield db
  finally:
    db.close()

Base.metadata.create_all(bind=engine)