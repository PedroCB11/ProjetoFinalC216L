import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import StaticPool

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://estudos_user:estudos_password@localhost:5432/estudos_db",
)

engine_config = {}

if DATABASE_URL.startswith("sqlite"):
    engine_config = {
        "connect_args": {"check_same_thread": False},
        "poolclass": StaticPool,
    }

engine = create_engine(DATABASE_URL, **engine_config)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
