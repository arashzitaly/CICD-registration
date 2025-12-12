# app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


def _get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        # Default for local Docker Postgres
        url = "postgresql://postgres:postgres@localhost:5432/registration_db"

    # If you're using Neon and the URL doesn't already specify sslmode,
    # enforce SSL (Neon typically requires it).
    if "neon.tech" in url and "sslmode=" not in url:
        sep = "&" if "?" in url else "?"
        url = f"{url}{sep}sslmode=require"

    return url


DATABASE_URL = _get_database_url()

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # avoids broken/stale connections
    future=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
