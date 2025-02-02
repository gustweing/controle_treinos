from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

POSTGRESS_DATABASE_URL = "postgresql://user:password@postgres/database_treino"

engine = create_engine(POSTGRESS_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False, 
    autoflush = False, 
    bind = engine 
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
