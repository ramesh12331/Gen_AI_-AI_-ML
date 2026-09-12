from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()

class Books(BaseModel):
    title : str = Field(min_length=2)
    author : str = Field(min_length=2)
    price : int = Field(gt=0)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test-db")
def test_database(connection:Session = Depends(get_db)):
    return{"message" : "Database Session Created Successfully"}

@app.get("/books")
def get_books(connection:Session = Depends(get_db)):
    try:
        result = connection.execute(
            text("SELECT * FROM books")
        )
        books = result.mappings().all()
        return books
    except Exception as e:
        return{
            "message" :"Somthing went wrong",
            "error" : str(e) 
            }

@app.get("/books/{id}")
def get_book(id:int, connection:Session = Depends(get_db)):
    try:
        result = connection.execute(
            text("""
                SELECT * FROM books
                WHERE book_id = :id
                """),
                {"id":id}
        )
        book = result.mappings().first()

        if book is None:
            return{
                "message" : "Book not found"
            }
        return book
    except Exception as e:
        return{
            "message" : "Something went wrong",
            "error" : str(e)
        }

@app.post("/books")
def add_books(books:Books, connection:Session = Depends(get_db)):
    try:
        connection.execute(
            text("""
                INSERT INTO books (title, author, price)
                VALUES
                (:title, :author, :price)
                """),
                {
                    "title" : books.title,
                    "author" : books.author,
                    "price" : books.price
                 }
        )
        connection.commit()
        return{"message" : "Books added successfully"}
    except Exception as e:
        connection.rollback()
        return{
            "message" : "Something went wrong",
            "error" : str(e)
        }

@app.put("/books/{id}")
def update_book(id:int, book:Books, connection:Session = Depends(get_db)):
    try:
        result = connection.execute(
            text("""
                UPDATE books
                SET
                    title = :title,
                    author = :author,
                    price = :price
                WHERE book_id = :id
            """),
            {
                "id" : id,
               "title" : book.title,
               "author" : book.author,
               "price"  : book.price
            }
        )
        
        if result.rowcount == 0:
            return{
                "message" : "Book not found"
            }
        connection.commit()
        return{
            "message" : "Book updated successfully"
        }
    except Exception as e:
        connection.rollback()
        return{
            "message" : "Something went wrong",
            "error" : str(e)
        }

@app.delete("/books/{id}")
def delete_book(id:int, connection:Session = Depends(get_db)):
    try:
        result = connection.execute(
                text("""
                    DELETE FROM books
                    WHERE 
                    book_id = :id
                    """),
                    {"id" : id}
            )
        
        if result.rowcount == 0:
            return{
                    "message" : "Book not found"
                }
        connection.commit()
    except Exception as e:
        connection.rollback()
        return{
            "message" : "Something Went Wrong",
            "error" : str(e)
        }
        
            