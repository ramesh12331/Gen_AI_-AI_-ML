from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import SessionLocal, Base, engine
from sqlalchemy.orm import Session 
from sqlalchemy import text
from models import Book

app = FastAPI()

Base.metadata.create_all(bind = engine)

class BookCreate(BaseModel):
    title : str = Field(min_length=2)
    author : str = Field(min_length=2)
    price : int = Field(gt=0)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message" : "FastAPI Working"}
    

@app.get("/books")
def get_books(connection:Session = Depends(get_db)):
        books = connection.query(Book).all()
        return books

    # result = connection.execute(
    #     text("""
    #         SELECT * FROM books
    #     """)
    # )
    # books = result.mappings().all()
    # return books