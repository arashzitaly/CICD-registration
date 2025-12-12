# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, Base, get_db

# Create tables (for demo; in real life use Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Registration Service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    existing = db.query(models.User).filter(
        models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Very naive hashing (you'll improve it later)
    fake_hashed_password = "hashed_" + user_in.password

    user = models.User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=fake_hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
