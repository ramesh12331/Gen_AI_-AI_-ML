# 📚 FastAPI + PostgreSQL + SQLAlchemy CRUD — Beginner Summary

You built a simple **Book Management API** using:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
books table
```

The main goal is to understand how a FastAPI application communicates with a PostgreSQL database.

---

## 1. 🏗️ Project Structure

```text
fastapi_project/
│
├── main.py
│
└── database.py
```

### `database.py`

Responsible for creating the database connection:

```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
```

### Remember:

```text
create_engine()
      ↓
Creates database connection setup
```

---

# 2. 🚀 FastAPI Application

In `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()` creates your API application.

---

# 3. 🔌 Database Connection

You used:

```python
with engine.connect() as connection:
```

This means:

> Connect to PostgreSQL.

For example:

```python
with engine.connect() as connection:
    pass
```

You don't need `SELECT 1` just to understand basic connection testing.

### Remember:

```text
engine.connect()
       ↓
Connect to database
```

---

# 4. 📖 READ — Get All Books

Endpoint:

```text
GET /get_books
```

SQL:

```sql
SELECT * FROM books;
```

Meaning:

> Get all records from the `books` table.

Python:

```python
result = connection.execute(
    text("SELECT * FROM books")
)

books = result.mappings().all()
```

### Important:

```python
.all()
```

means:

> Give me all matching rows.

---

# 5. 📕 READ — Get One Book

Endpoint:

```text
GET /books/{id}
```

Example:

```text
/books/2
```

FastAPI gets:

```python
id = 2
```

SQL:

```sql
SELECT *
FROM books
WHERE book_id = :id
```

Then:

```python
{"id": id}
```

connects the Python value to the SQL placeholder.

---

# 6. 🧠 Understanding `{"id": id}`

This is one of the most important concepts you learned.

```python
{
    "id": id
}
```

There are two sides:

```text
"id"        → SQL placeholder name
 id         → Python variable
```

For example:

```text
/books/5
   ↓
id = 5
   ↓
{"id": 5}
   ↓
:id gets the value 5
```

So:

```sql
WHERE book_id = :id
```

means:

> Find the book using the value provided for `id`.

---

# 7. ➕ CREATE — POST

Endpoint:

```text
POST /books
```

Purpose:

> Add a new book.

SQL:

```sql
INSERT INTO books
(title, author, price)
VALUES
(:title, :author, :price);
```

Python values:

```python
{
    "title": title,
    "author": author,
    "price": price
}
```

### Understand the names

```text
title       → Python variable
"title"     → dictionary key
title       → database column
:title       → SQL placeholder
```

For example:

```text
Swagger
   ↓
title = Python Basics
author = John
price = 500
   ↓
Python variables
   ↓
SQLAlchemy
   ↓
INSERT
   ↓
PostgreSQL
```

---

# 8. ✏️ UPDATE — PUT

Endpoint:

```text
PUT /books/{id}
```

Example:

```text
PUT /books/2
```

Purpose:

> Change an existing book.

SQL:

```sql
UPDATE books
SET
    title = :title,
    author = :author,
    price = :price
WHERE book_id = :id;
```

Flow:

```text
/books/2
   ↓
id = 2
   ↓
Find book 2
   ↓
UPDATE
   ↓
Save changes
```

---

# 9. 🗑️ DELETE

Endpoint:

```text
DELETE /books/{id}
```

Example:

```text
DELETE /books/2
```

SQL:

```sql
DELETE FROM books
WHERE book_id = :id;
```

Flow:

```text
/books/2
   ↓
id = 2
   ↓
Find book 2
   ↓
DELETE
   ↓
Book removed
```

---

# 10. 🔄 `connect()` vs `begin()`

This is important.

### For reading:

```python
with engine.connect() as connection:
```

Usually used for:

```text
GET
 ↓
SELECT
```

### For changing data:

```python
with engine.begin() as connection:
```

Used for:

```text
POST
 ↓
INSERT

PUT
 ↓
UPDATE

DELETE
 ↓
DELETE
```

Why?

Because POST, PUT and DELETE change the database and need a transaction that can be committed.

---

# 11. 🛡️ `try-except`

You also learned database error handling.

Basic pattern:

```python
try:

    # database code

except Exception as e:

    return {
        "message": "Something went wrong",
        "error": str(e)
    }
```

### Meaning:

```text
try
 ↓
Try database operation
 ↓
Successful?
 ↓ YES
Return result

 ↓ NO

except
 ↓
Handle error
```

---

# 12. 🧩 CRUD — The Most Important Part

This is what you should memorize:

```text
C → CREATE → POST   → INSERT
R → READ   → GET    → SELECT
U → UPDATE → PUT    → UPDATE
D → DELETE → DELETE → DELETE
```

### Easy memory trick:

```text
POST   = ADD ➕
GET    = SEE 👀
PUT    = CHANGE ✏️
DELETE = REMOVE 🗑️
```

---

# 13. 🌐 Your API Endpoints

Your project looks like:

```text
                BOOK API
                   │
       ┌───────────┼───────────┐
       │           │           │
      POST         GET         PUT
       │           │           │
     CREATE       READ       UPDATE
       │           │           │
       └───────────┼───────────┘
                   │
                 DELETE
                   │
                 DELETE
```

Endpoints:

```text
GET     /get_books
GET     /books/{id}

POST    /books

PUT     /books/{id}

DELETE  /books/{id}
```

---

# 14. 🗄️ Database Flow

The complete project works like this:

```text
                 Swagger UI
                     │
                     ▼
                  FastAPI
                     │
                     ▼
                 SQLAlchemy
                     │
                     ▼
                PostgreSQL
                     │
                     ▼
                 books table
                     │
                     ▼
                  DBeaver
```

### Important clarification

**DBeaver does not receive data from Swagger.**

DBeaver is simply a database tool that lets you view your PostgreSQL data.

```text
Swagger
   ↓
FastAPI
   ↓
PostgreSQL
   ↑
DBeaver views PostgreSQL
```

---

# ⭐ 15. What You Should Remember as a Beginner

Don't try to memorize every line.

First memorize these **7 concepts**:

### ① FastAPI

```python
app = FastAPI()
```

Creates your API.

### ② Database engine

```python
engine = create_engine(DATABASE_URL)
```

Connects your application to PostgreSQL.

### ③ Connection

```python
with engine.connect() as connection:
```

Connects to the database for operations such as reading.

### ④ SQL

```python
text("SELECT * FROM books")
```

Allows you to send SQL to PostgreSQL.

### ⑤ Parameters

```python
WHERE book_id = :id
```

and:

```python
{"id": id}
```

connect the SQL placeholder with the Python value.

### ⑥ CRUD

```text
POST    → INSERT
GET     → SELECT
PUT     → UPDATE
DELETE  → DELETE
```

### ⑦ Error handling

```python
try:
    ...
except Exception as e:
    ...
```

Handles database errors.

---

# 🎯 Final Beginner Cheat Sheet

```text
┌─────────────────────────────────────┐
│           FASTAPI CRUD              │
├─────────────────────────────────────┤
│                                     │
│ POST   → INSERT → Add               │
│ GET    → SELECT → Read              │
│ PUT    → UPDATE → Change            │
│ DELETE → DELETE → Remove            │
│                                     │
├─────────────────────────────────────┤
│                                     │
│ engine.connect()                    │
│      ↓                              │
│ Database connection                 │
│                                     │
│ engine.begin()                      │
│      ↓                              │
│ Change database data                │
│                                     │
├─────────────────────────────────────┤
│                                     │
│ :id          → SQL placeholder      │
│ {"id": id}   → gives its value      │
│                                     │
└─────────────────────────────────────┘
```

**Your next learning step:** after becoming comfortable with this raw-SQL version, learn **Pydantic `BaseModel` for POST/PUT request bodies**. That will make your FastAPI CRUD API much closer to how real FastAPI projects are normally written.
