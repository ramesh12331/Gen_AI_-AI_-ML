from fastapi import FastAPI
from pydantic import BaseModel, Field
from database import engine
from sqlalchemy import text

app = FastAPI()


# =========================
# PYDANTIC MODEL
# =========================

class Book(BaseModel):

    title: str = Field(
        min_length=2,
        max_length=100
    )

    author: str = Field(
        min_length=2,
        max_length=100
    )

    price: int = Field(
        gt=0
    )


# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "message": "FastAPI is Working"
    }


# =========================
# TEST DATABASE
# =========================

@app.get("/test-db")
def test_database():

    try:

        with engine.connect() as connection:
            pass

        return {
            "message": "Database connected successfully"
        }

    except Exception as e:

        return {
            "message": "Database connection failed",
            "error": str(e)
        }


# =========================
# GET ALL BOOKS
# =========================

@app.get("/get_books")
def get_books():

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT * FROM books")
            )

            books = result.mappings().all()

        return books

    except Exception as e:

        return {
            "message": "Something went wrong",
            "error": str(e)
        }


# =========================
# GET ONE BOOK
# =========================

@app.get("/books/{id}")
def get_book(id: int):

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("""
                    SELECT *
                    FROM books
                    WHERE book_id = :id
                """),
                {
                    "id": id
                }
            )

            book = result.mappings().first()

        if book is None:

            return {
                "message": "Book not found"
            }

        return book

    except Exception as e:

        return {
            "message": "Something went wrong",
            "error": str(e)
        }


# =========================
# CREATE BOOK
# =========================

@app.post("/books")
def add_book(book: Book):

    try:

        with engine.begin() as connection:

            connection.execute(
                text("""
                    INSERT INTO books
                    (title, author, price)
                    VALUES
                    (:title, :author, :price)
                """),
                {
                    "title": book.title,
                    "author": book.author,
                    "price": book.price
                }
            )

        return {
            "message": "Book added successfully"
        }

    except Exception as e:

        return {
            "message": "Something went wrong",
            "error": str(e)
        }


# =========================
# UPDATE BOOK
# =========================

@app.put("/books/{id}")
def update_book(id: int, book: Book):

    try:

        with engine.begin() as connection:

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
                    "id": id,
                    "title": book.title,
                    "author": book.author,
                    "price": book.price
                }
            )

        if result.rowcount == 0:

            return {
                "message": "Book not found"
            }

        return {
            "message": "Book updated successfully"
        }

    except Exception as e:

        return {
            "message": "Something went wrong",
            "error": str(e)
        }


# =========================
# DELETE BOOK
# =========================

@app.delete("/books/{id}")
def delete_book(id: int):

    try:

        with engine.begin() as connection:

            result = connection.execute(
                text("""
                    DELETE FROM books
                    WHERE book_id = :id
                """),
                {
                    "id": id
                }
            )

        if result.rowcount == 0:

            return {
                "message": "Book not found"
            }

        return {
            "message": "Book deleted successfully"
        }

    except Exception as e:

        return {
            "message": "Something went wrong",
            "error": str(e)
        }