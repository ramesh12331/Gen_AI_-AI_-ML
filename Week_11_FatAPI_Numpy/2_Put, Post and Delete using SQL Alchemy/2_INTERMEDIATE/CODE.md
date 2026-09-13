Yes 👍 Let's build the **Book CRUD API using Pydantic + SQLAlchemy Session**, **step by step**, at beginner level.

We'll keep **raw SQL** for now. We won't introduce SQLAlchemy ORM yet.

---

# Step 1 — Project structure

```text
book_api/
│
├── main.py
└── database.py
```

We already have a `books` table in PostgreSQL:

```text
books
├── book_id
├── title
├── author
└── price
```

---

# Step 2 — `database.py`

First, create the database engine and session.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

### 🧠 Understand

```text
DATABASE_URL
      ↓
    engine
      ↓
 SessionLocal
      ↓
   creates
   Session
```

`SessionLocal` is used to create a database session.

---

# Step 3 — Import everything in `main.py`

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import SessionLocal
```

Then:

```python
app = FastAPI()
```

---

# Step 4 — Create Pydantic model

```python
class Book(BaseModel):

    title: str = Field(min_length=2)

    author: str = Field(min_length=2)

    price: int = Field(gt=0)
```

This validates incoming data.

For example:

```json
{
    "title": "Python Basics",
    "author": "John",
    "price": 500
}
```

---

# Step 5 — Create `get_db()`

This is the most important new part when learning Session.

```python
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
```

### 🧠 What happens?

```text
Request
   ↓
get_db()
   ↓
SessionLocal()
   ↓
Create session
   ↓
Give session to endpoint
   ↓
Finish request
   ↓
db.close()
```

---

# Step 6 — Test database connection

Now let's make a simple test endpoint.

```python
@app.get("/test-db")
def test_database(db: Session = Depends(get_db)):

    return {
        "message": "Database session created successfully"
    }
```

### What is this?

```python
db: Session = Depends(get_db)
```

Means:

> FastAPI, call `get_db()` and give me the database session.

So:

```text
Depends(get_db)
       ↓
get_db()
       ↓
SessionLocal()
       ↓
db
```

---

# Step 7 — GET all books

Now let's use our session.

```python
@app.get("/get_books")
def get_books(db: Session = Depends(get_db)):

    try:

        result = db.execute(
            text("SELECT * FROM books")
        )

        books = result.mappings().all()

        return books

    except Exception as e:

        return {
            "message": "Something went wrong",
            "error": str(e)
        }
```

### Notice the difference

Before Session:

```python
with engine.connect() as connection:
```

Now:

```python
db: Session = Depends(get_db)
```

And:

```python
db.execute(...)
```

instead of:

```python
connection.execute(...)
```

---

# Step 8 — GET one book

```python
@app.get("/books/{id}")
def get_book(id: int, db: Session = Depends(get_db)):

    try:

        result = db.execute(
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
```

If you call:

```text
GET /books/2
```

then:

```python
id = 2
```

and:

```python
{"id": id}
```

becomes:

```python
{"id": 2}
```

---

# Step 9 — POST a book

Now we use **Pydantic + Session together**.

```python
@app.post("/books")
def add_book(
    book: Book,
    db: Session = Depends(get_db)
):

    try:

        db.execute(
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

        db.commit()

        return {
            "message": "Book added successfully"
        }

    except Exception as e:

        db.rollback()

        return {
            "message": "Something went wrong",
            "error": str(e)
        }
```

### 🧠 Flow

```text
Swagger
   ↓
JSON
   ↓
Pydantic
   ↓
Validation
   ↓
Book object
   ↓
db.execute()
   ↓
INSERT
   ↓
db.commit()
   ↓
PostgreSQL
```

---

# Step 10 — PUT a book

```python
@app.put("/books/{id}")
def update_book(
    id: int,
    book: Book,
    db: Session = Depends(get_db)
):

    try:

        result = db.execute(
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

        db.commit()

        return {
            "message": "Book updated successfully"
        }

    except Exception as e:

        db.rollback()

        return {
            "message": "Something went wrong",
            "error": str(e)
        }
```

Example:

```text
PUT /books/2
```

Body:

```json
{
    "title": "Advanced Python",
    "author": "John",
    "price": 800
}
```

Flow:

```text
/books/2
   ↓
id = 2
   ↓
Pydantic validates body
   ↓
UPDATE books
   ↓
db.commit()
   ↓
Saved ✅
```

---

# Step 11 — DELETE a book

```python
@app.delete("/books/{id}")
def delete_book(
    id: int,
    db: Session = Depends(get_db)
):

    try:

        result = db.execute(
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

        db.commit()

        return {
            "message": "Book deleted successfully"
        }

    except Exception as e:

        db.rollback()

        return {
            "message": "Something went wrong",
            "error": str(e)
        }
```

---

# 🎯 Final Architecture

Now your project has three important layers:

```text
                 Swagger UI
                     ↓
                  FastAPI
                     ↓
                Pydantic
                     ↓
                 Validation
                     ↓
                 Session
                     ↓
                SQLAlchemy
                     ↓
                PostgreSQL
```

### CRUD

```text
POST
 ↓
Pydantic
 ↓
Session
 ↓
INSERT
 ↓
COMMIT
```

```text
GET
 ↓
Session
 ↓
SELECT
 ↓
Return data
```

```text
PUT
 ↓
Pydantic
 ↓
Session
 ↓
UPDATE
 ↓
COMMIT
```

```text
DELETE
 ↓
Session
 ↓
DELETE
 ↓
COMMIT
```

---

# ⭐ Session Cheat Sheet

These are the main things to remember:

```python
SessionLocal()
```

➡️ Creates a session.

```python
Depends(get_db)
```

➡️ Gives the session to your API function.

```python
db.execute()
```

➡️ Executes SQL.

```python
db.commit()
```

➡️ Saves INSERT/UPDATE/DELETE.

```python
db.rollback()
```

➡️ Cancels the transaction if there is an error.

```python
db.close()
```

➡️ Closes the session.

---

## 🧠 The beginner version to memorize

```text
SessionLocal()
     ↓
   Session
     ↓
 db.execute()
     ↓
SQL Query
     ↓
db.commit()       ← POST / PUT / DELETE
```

And:

```text
get_db()
   ↓
yield db
   ↓
API uses db
   ↓
db.close()
```

**Don't learn ORM yet.** First become comfortable with this exact flow: **Pydantic → Session → raw SQL → commit/rollback**. Then SQLAlchemy ORM will make much more sense.
