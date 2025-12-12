from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from . import models, schemas
from .database import engine, Base, get_db

app = FastAPI(title="Registration Service")


@app.on_event("startup")
def on_startup():
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError:
        print("WARNING: Database not reachable on startup")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(
        models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password="hashed_" + user_in.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
