from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.sql_app import crud, models, schemas
from app.sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()