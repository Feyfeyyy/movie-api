from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = environ.get("DATABASE_URI")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> SessionLocal:
    """
    Get a database session

    :return: database session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
