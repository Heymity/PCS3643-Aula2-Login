import psycopg2
from psycopg2 import sql

# Configurações do banco de dados
DATABASE_URL = "postgresql://postgres:1234@localhost/postgres"
TARGET_DATABASE = "api_db"
SCHEMA_NAME = "api"

# Função para criar o banco de dados se não existir
def create_database_if_not_exists():
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [TARGET_DATABASE])
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(TARGET_DATABASE)))
        conn.commit()
    cursor.close()
    conn.close()

# Função para criar o schema se não existir
def create_schema_if_not_exists():
    conn = psycopg2.connect(f"postgresql://postgres:1234@localhost/{TARGET_DATABASE}")
    cursor = conn.cursor()
    cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(SCHEMA_NAME)))
    conn.commit()
    cursor.close()
    conn.close()

# Criar banco de dados e schema
create_database_if_not_exists()
create_schema_if_not_exists()