from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import SessionLocal

app = FastAPI()

class Book(BaseModel):
    title : str = Field(min_length = 2)
    author : str = Field(min_length = 2)
    price : int = Field(gt=0)

# Create get_db()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test database connection
@app.get("/test-db")
def test_database(connection:Session = Depends(get_db)):
    return{
        "message": "Database session created successfully"
    }
