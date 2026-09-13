Yes 👍. You want to take **your exact current code** and separate the **Pydantic validation into a separate `schemas.py` file**.

There is also **one important issue** in your code: your ORM model uses `__tablename__ = "book"` while your routes are working with `Book`. That's okay as a Python class name, but make sure the actual PostgreSQL table you want is `book`. `create_all()` will create `book` if it doesn't already exist.

## 📁 Final project structure

```text
book_api/
│
├── main.py
├── database.py
├── models.py
└── schemas.py
```

---

# 1️⃣ `database.py`

This file is responsible for **database connection + session**.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()
```

### Simple responsibility

```text
database.py
     ↓
PostgreSQL connection
     ↓
Engine
     ↓
Session
     ↓
Base
```

---

# 2️⃣ `models.py`

This file contains the **SQLAlchemy ORM model**.

```python
from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Integer)
```

### What this does

```text
Python Class
    ↓
Book
    ↓
Database Table
    ↓
book
```

So:

```python
Book
```

represents:

```text
book table
```

And:

```python
Book.book_id
Book.title
Book.author
Book.price
```

represent the database columns.

---

# 3️⃣ `schemas.py` ⭐ NEW FILE

Now we move your Pydantic validation here.

```python
from pydantic import BaseModel, Field


class Novel(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    price: int = Field(gt=0)
```

This file is responsible only for **API data validation**.

For example:

```json
{
    "title": "Python Basics",
    "author": "John Smith",
    "price": 500
}
```

Pydantic checks:

```text
title  → string → minimum 2 characters
author → string → minimum 2 characters
price  → integer → greater than 0
```

---

# 4️⃣ `main.py`

Now your `main.py` becomes cleaner.

```python
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
```

---

# ⭐ What changed from your code?

Only one major change:

### Before

You had Pydantic inside `main.py`:

```python
from pydantic import BaseModel, Field

class Novel(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    price: int = Field(gt=0)
```

### Now

Move it to:

```text
schemas.py
```

and import it into `main.py`:

```python
from schemas import Novel
```

So `main.py` no longer needs:

```python
from pydantic import BaseModel, Field
```

---

# 🧠 Now understand the 4 files

This is the important part for you as a beginner:

```text
                 FASTAPI PROJECT
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
     schemas.py    models.py    database.py
          │            │            │
          ↓            ↓            ↓
      Pydantic       ORM        Connection
          │            │            │
       Validate      Table       Session
       API data      mapping         │
          │            │            │
          └────────────┼────────────┘
                       ↓
                    main.py
                       ↓
                    Routes
                       ↓
                  PostgreSQL
```

### Remember this:

| File          | What it does                   | Technology     |
| ------------- | ------------------------------ | -------------- |
| `database.py` | Connect to DB / create session | SQLAlchemy     |
| `models.py`   | Represent database table       | SQLAlchemy ORM |
| `schemas.py`  | Validate incoming API data     | Pydantic       |
| `main.py`     | API endpoints                  | FastAPI        |

### Most important distinction

```text
schemas.py
     ↓
"What data is allowed to enter my API?"
     ↓
Pydantic


models.py
     ↓
"How is my database table represented in Python?"
     ↓
SQLAlchemy ORM
```

So your overall flow is now:

```text
POST /novels
      ↓
JSON data
      ↓
schemas.py
      ↓
Novel (Pydantic)
      ↓
Validation
      ↓
main.py
      ↓
Book (ORM)
      ↓
Session
      ↓
PostgreSQL
```

**This is the clean structure you should learn going forward.**
