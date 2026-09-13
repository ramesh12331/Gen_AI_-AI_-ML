from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)