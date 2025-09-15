import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

# URL de conexão ao banco de dados padrão
TARGET_DATABASE = "api_db"
SCHEMA_NAME = "api"
DATABASE_URL = f"postgresql://postgres:1234@localhost/{TARGET_DATABASE}"


# Crie o engine com o schema padrão 'api'
engine = create_engine(DATABASE_URL, connect_args={"options": f"-csearch_path={SCHEMA_NAME}"})


SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()