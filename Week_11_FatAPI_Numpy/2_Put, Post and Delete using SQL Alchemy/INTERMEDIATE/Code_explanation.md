# 📚 FastAPI + PostgreSQL + SQLAlchemy CRUD

> **Beginner Level README — Telugu Explanation**

ఈ project లో మనం **FastAPI ద్వారా PostgreSQL database లో Books data ని CRUD operations** చేయడం నేర్చుకుంటాం.

```text
FastAPI
   ↓
Pydantic Validation
   ↓
Depends(get_db)
   ↓
SQLAlchemy Session
   ↓
SQL Query
   ↓
PostgreSQL
```

---

# 1. 🎯 Project Goal

మన database లో `books` అనే table ఉందని అనుకుందాం.

```text
books
--------------------------------
book_id
title
author
price
```

మన API ద్వారా:

* 📖 Books చూడాలి
* 🔍 ఒక Book చూడాలి
* ➕ కొత్త Book add చేయాలి
* ✏️ Book update చేయాలి
* 🗑️ Book delete చేయాలి

అంటే:

```text
CRUD

C → Create → POST
R → Read   → GET
U → Update → PUT
D → Delete → DELETE
```

---

# 2. 📦 Required Imports

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
```

## Definition

### `FastAPI`

API application create చేయడానికి ఉపయోగిస్తాం.

```python
app = FastAPI()
```

### `Depends`

FastAPI కి dependency provide చేయడానికి ఉపయోగిస్తాం.

```python
Depends(get_db)
```

### `BaseModel`

Pydantic model create చేయడానికి.

```python
class Books(BaseModel):
```

### `Field`

Input validation చేయడానికి.

```python
Field(min_length=2)
Field(gt=0)
```

### `SessionLocal`

SQLAlchemy database session create చేయడానికి.

```python
db = SessionLocal()
```

### `Session`

Database session type.

```python
connection: Session
```

### `text`

Raw SQL query execute చేయడానికి.

```python
text("SELECT * FROM books")
```

---

# 3. 🚀 FastAPI Application

## Syntax

```python
app = FastAPI()
```

## Example

```python
from fastapi import FastAPI

app = FastAPI()
```

ఇది FastAPI application create చేస్తుంది.

---

# 4. 🛡️ Pydantic Model

```python
class Books(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    price: int = Field(gt=0)
```

ఇది API కి వచ్చే input data ని validate చేస్తుంది.

## Fields

### `title`

```python
title: str
```

`title` string అయి ఉండాలి.

```python
Field(min_length=2)
```

కనీసం 2 characters ఉండాలి.

---

### `author`

```python
author: str = Field(min_length=2)
```

Author కూడా string అయి ఉండాలి మరియు minimum 2 characters ఉండాలి.

---

### `price`

```python
price: int = Field(gt=0)
```

`gt` అంటే:

> **greater than**

అంటే:

```text
price > 0
```

ఉండాలి.

## Valid data

```json
{
    "title": "Python Basics",
    "author": "Ramesh",
    "price": 500
}
```

## Invalid data

```json
{
    "title": "A",
    "author": "B",
    "price": 0
}
```

ఇది validation error ఇస్తుంది.

---

# 5. 🔌 Database Session — `get_db()`

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

ఇది project లో చాలా important function.

## Step-by-step

### Step 1

```python
db = SessionLocal()
```

కొత్త SQLAlchemy Session create అవుతుంది.

```text
SessionLocal()
     ↓
Session
     ↓
db
```

### Step 2

```python
yield db
```

Database session ని FastAPI endpoint కి ఇస్తుంది.

### Step 3

API database operation చేస్తుంది.

### Step 4

```python
db.close()
```

Session close అవుతుంది.

---

# 6. 🤔 `yield` ఎందుకు ఉపయోగిస్తాం?

```python
yield db
```

`yield` అంటే:

> "ఈ database session ని ఇప్పుడే API కి ఇవ్వు. API పని పూర్తయిన తర్వాత మిగిలిన cleanup code run చేయి."

Flow:

```text
SessionLocal()
      ↓
Session create
      ↓
yield db
      ↓
API uses db
      ↓
API complete
      ↓
finally
      ↓
db.close()
```

### `return` vs `yield`

```text
return
↓
value ఇవ్వు
↓
function complete
```

```text
yield
↓
value ఇవ్వు
↓
function pause
↓
API పని complete
↓
function continue
↓
cleanup
```

---

# 7. 🧩 `Depends(get_db)`

Example:

```python
def test_database(
    connection: Session = Depends(get_db)
):
```

ఇక్కడ:

```text
connection
↓
Variable name
```

```text
Session
↓
SQLAlchemy Session type
```

```text
Depends(get_db)
↓
get_db() ద్వారా session తీసుకో
```

## Important

`connection` పేరు compulsory కాదు.

ఇలా కూడా రాయవచ్చు:

```python
db: Session = Depends(get_db)
```

లేదా:

```python
database: Session = Depends(get_db)
```

లేదా:

```python
connection: Session = Depends(get_db)
```

అన్నీ valid.

---

# 8. 🔗 `/test-db`

```python
@app.get("/test-db")
def test_database(connection: Session = Depends(get_db)):
    return {
        "message": "Database Session Created Successfully"
    }
```

## Flow

```text
GET /test-db
      ↓
Depends(get_db)
      ↓
get_db()
      ↓
SessionLocal()
      ↓
Session
      ↓
connection
      ↓
Response
```

Response:

```json
{
    "message": "Database Session Created Successfully"
}
```

> Note: ఈ endpoint session create అవుతుందో test చేస్తుంది. Actual SQL connection test చేయాలంటే `SELECT 1` execute చేయడం మంచిది.

---

# 9. 📖 GET All Books

```python
@app.get("/books")
def get_books(connection: Session = Depends(get_db)):
    try:
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
```

## SQL

```sql
SELECT * FROM books;
```

అన్ని books తీసుకువస్తుంది.

---

# 10. 🔍 `connection.execute()`

```python
result = connection.execute(
    text("SELECT * FROM books")
)
```

Meaning:

> SQLAlchemy Session ద్వారా SQL query execute చేయి.

Flow:

```text
connection
    ↓
execute()
    ↓
text()
    ↓
SQL Query
    ↓
PostgreSQL
```

---

# 11. 📦 `result.mappings().all()`

```python
books = result.mappings().all()
```

Database result ని dictionary-like format లో తీసుకోవడానికి ఉపయోగిస్తాం.

Database:

```text
book_id | title  | author | price
----------------------------------
1       | Python | Ramesh | 500
```

API:

```json
[
    {
        "book_id": 1,
        "title": "Python",
        "author": "Ramesh",
        "price": 500
    }
]
```

---

# 12. 🔎 GET One Book

```python
@app.get("/books/{id}")
def get_book(
    id: int,
    connection: Session = Depends(get_db)
):
```

ఇక్కడ:

```text
id
↓
Path Parameter
```

Example:

```text
GET /books/5
```

అప్పుడు:

```python
id = 5
```

---

# 13. 🔐 SQL Parameters

```python
text("""
    SELECT * FROM books
    WHERE book_id = :id
"""),
{"id": id}
```

ఇక్కడ:

```text
:id
↓
SQL placeholder
```

Python:

```python
{"id": id}
```

`id` value ని SQL query కి provide చేస్తుంది.

Example:

```text
URL:
GET /books/5

id = 5

:id → 5
```

---

# 14. `first()`

```python
book = result.mappings().first()
```

మొదటి matching record తీసుకుంటుంది.

Book లేకపోతే:

```python
book is None
```

అప్పుడు:

```python
if book is None:
    return {
        "message": "Book not found"
    }
```

---

# 15. ➕ POST — Add Book

```python
@app.post("/books")
def add_books(
    books: Books,
    connection: Session = Depends(get_db)
):
```

ఇక్కడ రెండు important inputs ఉన్నాయి.

```text
books
↓
Request Body

connection
↓
Database Session
```

Swagger లో:

```json
{
    "title": "FastAPI",
    "author": "Ramesh",
    "price": 600
}
```

---

# 16. 📥 INSERT Query

```python
connection.execute(
    text("""
        INSERT INTO books (title, author, price)
        VALUES (:title, :author, :price)
    """),
    {
        "title": books.title,
        "author": books.author,
        "price": books.price
    }
)
```

Mapping:

```text
:title
  ↓
books.title

:author
  ↓
books.author

:price
  ↓
books.price
```

---

# 17. 💾 `commit()`

```python
connection.commit()
```

Database change ని permanently save చేయడానికి `commit()` ఉపయోగిస్తాం.

```text
INSERT
  ↓
Transaction
  ↓
commit()
  ↓
Saved in PostgreSQL
```

---

# 18. ✏️ PUT — Update Book

```python
@app.put("/books/{id}")
def update_book(
    id: int,
    book: Books,
    connection: Session = Depends(get_db)
):
```

ఇక్కడ 3 values ఉన్నాయి:

```text
id
↓
URL

book
↓
Request Body

connection
↓
Database Session
```

Example:

```text
PUT /books/5
```

Body:

```json
{
    "title": "Advanced Python",
    "author": "Ramesh",
    "price": 800
}
```

---

# 19. UPDATE SQL

```sql
UPDATE books
SET
    title = :title,
    author = :author,
    price = :price
WHERE book_id = :id
```

Values:

```python
{
    "id": id,
    "title": book.title,
    "author": book.author,
    "price": book.price
}
```

Meaning:

```text
URL id
  ↓
WHERE book_id

Body title
  ↓
title

Body author
  ↓
author

Body price
  ↓
price
```

---

# 20. 📊 `rowcount`

```python
if result.rowcount == 0:
```

`rowcount` అంటే:

> ఎన్ని rows ప్రభావితం అయ్యాయో.

### Book exists

```text
rowcount = 1
```

అంటే ఒక book update అయింది.

### Book doesn't exist

```text
rowcount = 0
```

అప్పుడు:

```python
return {
    "message": "Book not found"
}
```

### Important

```python
result.rowcount
```

✅ Correct

```python
result.rowcount()
```

❌ Wrong

`rowcount` attribute, function కాదు.

---

# 21. 🗑️ DELETE — Delete Book

```python
@app.delete("/books/{id}")
def delete_book(
    id: int,
    connection: Session = Depends(get_db)
):
```

Example:

```text
DELETE /books/5
```

SQL:

```sql
DELETE FROM books
WHERE book_id = :id
```

Values:

```python
{"id": id}
```

---

# 22. DELETE `rowcount`

```python
if result.rowcount == 0:
    return {
        "message": "Book not found"
    }
```

Book ఉంటే:

```text
rowcount = 1
```

Book లేకపోతే:

```text
rowcount = 0
```

---

# 23. ⚠️ DELETE లో `commit()`

Successful DELETE తర్వాత:

```python
connection.commit()
```

అవసరం.

ఎందుకంటే delete change ని database లో save చేయాలి.

Better:

```python
connection.commit()

return {
    "message": "Book deleted successfully"
}
```

---

# 24. ❌ `rollback()`

Error వస్తే:

```python
connection.rollback()
```

ఉపయోగిస్తాం.

Meaning:

> Current transaction లో చేసిన changes ని cancel చేయి.

Flow:

```text
SQL Operation
      ↓
Error ❌
      ↓
rollback()
      ↓
Transaction cancel
```

---

# 25. `try` and `except`

Example:

```python
try:
    connection.execute(...)
    connection.commit()

except Exception as e:
    connection.rollback()

    return {
        "message": "Something went wrong",
        "error": str(e)
    }
```

## `try`

Database operation చేయడానికి.

## `except`

Error వచ్చినప్పుడు handle చేయడానికి.

## `e`

Error information.

```python
str(e)
```

Error ని string గా return చేస్తుంది.

---

# 26. 🧠 Complete CRUD Flow

## CREATE

```text
POST /books
     ↓
JSON Body
     ↓
Pydantic
     ↓
Depends(get_db)
     ↓
Session
     ↓
INSERT
     ↓
commit()
     ↓
PostgreSQL
```

---

## READ All

```text
GET /books
     ↓
Depends(get_db)
     ↓
Session
     ↓
SELECT *
     ↓
PostgreSQL
     ↓
mappings().all()
     ↓
Response
```

---

## READ One

```text
GET /books/5
     ↓
id = 5
     ↓
Session
     ↓
SELECT ... WHERE book_id = :id
     ↓
PostgreSQL
     ↓
first()
     ↓
Response
```

---

## UPDATE

```text
PUT /books/5
     ↓
id = 5
     ↓
Pydantic Body
     ↓
Session
     ↓
UPDATE
     ↓
rowcount
     ↓
commit()
     ↓
Response
```

---

## DELETE

```text
DELETE /books/5
     ↓
id = 5
     ↓
Session
     ↓
DELETE
     ↓
rowcount
     ↓
commit()
     ↓
Response
```

---

# 27. 📌 Where Does Each Value Come From?

ఇది చాలా important concept.

## GET All

```python
def get_books(
    connection: Session = Depends(get_db)
):
```

```text
connection
↓
get_db()
```

---

## GET One

```python
def get_book(
    id: int,
    connection: Session = Depends(get_db)
):
```

```text
id
↓
URL

connection
↓
get_db()
```

---

## POST

```python
def add_books(
    books: Books,
    connection: Session = Depends(get_db)
):
```

```text
books
↓
JSON Request Body

connection
↓
get_db()
```

---

## PUT

```python
def update_book(
    id: int,
    book: Books,
    connection: Session = Depends(get_db)
):
```

```text
id
↓
URL

book
↓
JSON Request Body

connection
↓
get_db()
```

---

## DELETE

```python
def delete_book(
    id: int,
    connection: Session = Depends(get_db)
):
```

```text
id
↓
URL

connection
↓
get_db()
```

---

# 28. 🔑 Important Keywords

| Keyword          | Meaning                                       |
| ---------------- | --------------------------------------------- |
| `FastAPI()`      | FastAPI application create                    |
| `BaseModel`      | Pydantic model                                |
| `Field()`        | Validation                                    |
| `Depends()`      | Dependency injection                          |
| `SessionLocal()` | Database session create                       |
| `Session`        | SQLAlchemy session type                       |
| `yield`          | Session provide చేసి cleanup allow చేస్తుంది  |
| `execute()`      | SQL execute                                   |
| `text()`         | Raw SQL query                                 |
| `mappings()`     | Result ని mapping/dictionary-like format లోకి |
| `all()`          | అన్ని rows                                    |
| `first()`        | మొదటి row                                     |
| `rowcount`       | Affected rows count                           |
| `commit()`       | Changes save                                  |
| `rollback()`     | Failed transaction cancel                     |
| `close()`        | Session close                                 |

---

# 29. 🗺️ CRUD Endpoint Table

| Method | URL           | Purpose     | SQL            |
| ------ | ------------- | ----------- | -------------- |
| GET    | `/books`      | అన్ని books | `SELECT`       |
| GET    | `/books/{id}` | ఒక book     | `SELECT WHERE` |
| POST   | `/books`      | Book add    | `INSERT`       |
| PUT    | `/books/{id}` | Book update | `UPDATE`       |
| DELETE | `/books/{id}` | Book delete | `DELETE`       |

---

# 30. 📄 Complete Code

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()


# -------------------------
# Pydantic Model
# -------------------------

class Books(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    price: int = Field(gt=0)


# -------------------------
# Database Dependency
# -------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# -------------------------
# Test Database Session
# -------------------------

@app.get("/test-db")
def test_database(
    connection: Session = Depends(get_db)
):
    return {
        "message": "Database Session Created Successfully"
    }


# -------------------------
# GET All Books
# -------------------------

@app.get("/books")
def get_books(
    connection: Session = Depends(get_db)
):
    try:
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


# -------------------------
# GET One Book
# -------------------------

@app.get("/books/{id}")
def get_book(
    id: int,
    connection: Session = Depends(get_db)
):
    try:
        result = connection.execute(
            text("""
                SELECT * FROM books
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


# -------------------------
# POST - Add Book
# -------------------------

@app.post("/books")
def add_books(
    books: Books,
    connection: Session = Depends(get_db)
):
    try:
        connection.execute(
            text("""
                INSERT INTO books (title, author, price)
                VALUES (:title, :author, :price)
            """),
            {
                "title": books.title,
                "author": books.author,
                "price": books.price
            }
        )

        connection.commit()

        return {
            "message": "Book added successfully"
        }

    except Exception as e:
        connection.rollback()

        return {
            "message": "Something went wrong",
            "error": str(e)
        }


# -------------------------
# PUT - Update Book
# -------------------------

@app.put("/books/{id}")
def update_book(
    id: int,
    book: Books,
    connection: Session = Depends(get_db)
):
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

        connection.commit()

        return {
            "message": "Book updated successfully"
        }

    except Exception as e:
        connection.rollback()

        return {
            "message": "Something went wrong",
            "error": str(e)
        }


# -------------------------
# DELETE - Delete Book
# -------------------------

@app.delete("/books/{id}")
def delete_book(
    id: int,
    connection: Session = Depends(get_db)
):
    try:
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

        connection.commit()

        return {
            "message": "Book deleted successfully"
        }

    except Exception as e:
        connection.rollback()

        return {
            "message": "Something went wrong",
            "error": str(e)
        }
```

---

# 31. 🧠 Final Beginner Summary

ఈ project లో main concept:

```text
FastAPI
   ↓
API Endpoint
   ↓
Pydantic
   ↓
Validate Request Data
   ↓
Depends(get_db)
   ↓
get_db()
   ↓
SessionLocal()
   ↓
SQLAlchemy Session
   ↓
connection.execute()
   ↓
SQL Query
   ↓
PostgreSQL
```

### Pydantic

```text
User పంపిన data correct గా ఉందా?
        ↓
Pydantic checks
```

### Session

```text
Python code database తో ఎలా మాట్లాడాలి?
        ↓
SQLAlchemy Session
```

### Depends

```text
Endpoint కి database session ఎవరు ఇస్తారు?
        ↓
Depends(get_db)
```

### `yield`

```text
Session API కి ఇవ్వు
        ↓
API పని complete
        ↓
Session close చేయి
```

### `execute()`

```text
SQL query run చేయి
```

### `commit()`

```text
INSERT / UPDATE / DELETE changes save చేయి
```

### `rollback()`

```text
Error అయితే transaction cancel చేయి
```

### `close()`

```text
Database session close చేయి
```

---

# ⭐ One-Minute Revision

```text
POST
↓
Pydantic validates
↓
Session gets created
↓
INSERT
↓
commit()
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
URL id + Pydantic body
↓
UPDATE
↓
rowcount
↓
commit()
```

```text
DELETE
↓
URL id
↓
DELETE
↓
rowcount
↓
commit()
```

### 🔥 Remember This

> **Pydantic = Data Validation**

> **Depends = Dependency Injection**

> **SessionLocal = Session Creation**

> **Session = Database Work Interface**

> **execute() = SQL Run**

> **commit() = Save**

> **rollback() = Undo Failed Transaction**

> **yield = Give Session + Later Cleanup**

> **close() = Close Session**

> **CRUD = Create, Read, Update, Delete**
