from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, Base, engine
from models import Book
from schemas import Novel


app = FastAPI()


# Create database table
Base.metadata.create_all(bind=engine)


# Database session
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# --------------------------------
# HOME
# --------------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI Working"
    }


# --------------------------------
# GET ALL NOVELS
# --------------------------------

@app.get("/novel")
def get_novels(
    connection: Session = Depends(get_db)
):
    novels = connection.query(Book).all()

    return novels


# --------------------------------
# GET ONE NOVEL
# --------------------------------

@app.get("/novel/{id}")
def get_novel(
    id: int,
    connection: Session = Depends(get_db)
):

    novel = connection.query(Book).filter(
        Book.book_id == id
    ).first()

    if novel is None:
        return {
            "message": "Novel not found"
        }

    return novel


# --------------------------------
# ADD NOVEL
# --------------------------------

@app.post("/novels")
def add_novels(
    novels: Novel,
    connection: Session = Depends(get_db)
):

    new_novel = Book(
        title=novels.title,
        author=novels.author,
        price=novels.price
    )

    connection.add(new_novel)

    connection.commit()

    connection.refresh(new_novel)

    return new_novel


# --------------------------------
# UPDATE NOVEL
# --------------------------------

@app.put("/novel/{id}")
def update_novel(
    id: int,
    novels: Novel,
    connection: Session = Depends(get_db)
):

    existing_book = connection.query(Book).filter(
        Book.book_id == id
    ).first()

    if existing_book is None:
        return {
            "message": "Book not found"
        }

    existing_book.title = novels.title
    existing_book.author = novels.author
    existing_book.price = novels.price

    connection.commit()

    connection.refresh(existing_book)

    return existing_book


# --------------------------------
# DELETE NOVEL
# --------------------------------

@app.delete("/novel/{id}")
def delete_novel(
    id: int,
    connection: Session = Depends(get_db)
):

    novel = connection.query(Book).filter(
        Book.book_id == id
    ).first()

    if novel is None:
        return {
            "message": "Novel not found"
        }

    connection.delete(novel)

    connection.commit()

    return {
        "message": "Book deleted successfully"
    }