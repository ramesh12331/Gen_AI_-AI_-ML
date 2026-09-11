from fastapi import FastAPI
from database import engine
from sqlalchemy import text

app = FastAPI()

@app.get("/")
def home():
    return{"message" : "FastAPI is Working"}

# @app.get("/test_db")
# def test_database():
#     with engine.connect() as connection_db:
#         result = connection_db.execute(
#             text("SELECT * from books")
#         )
#     return{"message" : "Database connect successfully"}

@app.get("/test-db")
def test_database():
    try:
        connection = engine.connect()
        connection.close()
        return{"message" : "Datbase connected successfullyyyy"}
    except Exception:
        return{"message" : "Database connection failed"}

@app.get("/books")
def get_books():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * from books")
            )
            books = result.mappings().all()
        return books
    except Exception as e:
        return{
            "meaasge" : "Something went wrong",
            "error" : str(e)
        }

@app.get("/book/{id}")
def get_book(id : int):
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * from books where book_id = :id"),
                {"id" : id}
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