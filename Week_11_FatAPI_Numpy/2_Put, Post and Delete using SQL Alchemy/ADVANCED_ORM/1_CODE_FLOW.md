Absolutely 👍 You are at the **right point to learn SQLAlchemy ORM**.

You already learned:

```text
FastAPI
   ↓
Pydantic
   ↓
Session
   ↓
Raw SQL
   ↓
PostgreSQL
```

Now ORM changes the way you write database queries.

# 🧠 1. What is ORM?

**ORM = Object Relational Mapping**

Simple meaning:

> ORM lets you work with database tables using **Python classes and objects instead of writing SQL manually**.

### Before — Raw SQL

You wrote:

```python
db.execute(
    text("SELECT * FROM books")
)
```

With ORM, you can write:

```python
db.query(Book).all()
```

Much more Python-like.

---

# 🔄 2. Raw SQL vs ORM

Suppose your PostgreSQL table is:

```text
books
-------------------
book_id
title
author
price
```

### Raw SQL

```sql
SELECT * FROM books;
```

### ORM

```python
db.query(Book).all()
```

The ORM understands that:

```text
Python Book class
       ↕
books table
```

---

# 🧩 3. First create an ORM Model

This is different from your **Pydantic model**.

You will have **two models**:

```text
Pydantic Model
     ↓
API validation

ORM Model
     ↓
Database table
```

---

# Step 1 — Create `models.py`

Create a new file:

```text
book_api/
│
├── main.py
├── database.py
└── models.py
```

In `models.py`:

```python
from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):

    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Integer)
```

---

# 🧠 4. Understand `class Book`

```python
class Book(Base):
```

This is your **ORM model**.

It represents:

```text
Python class
     ↓
Database table
```

---

# Step 2 — Understand `__tablename__`

```python
__tablename__ = "books"
```

This tells SQLAlchemy:

> This Python class represents the `books` table.

So:

```text
Book class
    ↓
books table
```

---

# Step 3 — Understand columns

```python
book_id = Column(Integer, primary_key=True)
```

means:

```text
book_id
   ↓
Integer
   ↓
Primary Key
```

And:

```python
title = Column(String)
```

means:

```text
title
   ↓
String
```

So your model represents:

```text
Book
│
├── book_id → Integer
├── title   → String
├── author  → String
└── price   → Integer
```

---

# ⚠️ 5. Add `Base` to `database.py`

Your current `database.py` needs one additional thing.

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

### What is `Base`?

Think:

```text
Base
 ↓
Parent for ORM models
 ↓
Book
 ↓
books table
```

---

# 🧠 6. Pydantic vs ORM

This is **very important**.

You might have:

### Pydantic

```python
class BookCreate(BaseModel):

    title: str
    author: str
    price: int
```

Used for:

```text
Client
  ↓
API
  ↓
Validation
```

### ORM

```python
class Book(Base):

    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Integer)
```

Used for:

```text
Python
  ↓
Database
```

### Visual

```text
             USER
               ↓
             JSON
               ↓
         Pydantic Model
               ↓
           Validation
               ↓
          FastAPI Code
               ↓
           ORM Model
               ↓
            Session
               ↓
          PostgreSQL
```

---

# 🚀 7. First ORM READ operation

Now let's replace your raw SQL:

```python
db.execute(
    text("SELECT * FROM books")
)
```

with ORM.

```python
@app.get("/get_books")
def get_books(db: Session = Depends(get_db)):

    books = db.query(Book).all()

    return books
```

### What does this mean?

```python
db.query(Book)
```

means:

> Work with the `Book` table.

```python
.all()
```

means:

> Get all books.

So:

```python
db.query(Book).all()
```

is roughly equivalent to:

```sql
SELECT * FROM books;
```

---

# 🔍 8. Get One Book

Raw SQL:

```sql
SELECT *
FROM books
WHERE book_id = 2;
```

ORM:

```python
book = db.query(Book).filter(
    Book.book_id == id
).first()
```

Full endpoint:

```python
@app.get("/books/{id}")
def get_book(id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(
        Book.book_id == id
    ).first()

    if book is None:
        return {
            "message": "Book not found"
        }

    return book
```

### Understand this:

```python
Book.book_id
```

means:

> The `book_id` column of the `Book` ORM model.

```python
Book.book_id == id
```

means:

> Find a row where `book_id` equals the ID.

---

# ➕ 9. CREATE using ORM

This is where ORM becomes really interesting.

### Raw SQL

You previously wrote:

```python
db.execute(
    text("""
        INSERT INTO books
        (title, author, price)
        VALUES (:title, :author, :price)
    """),
    {
        "title": book.title,
        "author": book.author,
        "price": book.price
    }
)

db.commit()
```

### ORM

Much simpler:

```python
new_book = Book(
    title=book.title,
    author=book.author,
    price=book.price
)

db.add(new_book)

db.commit()

db.refresh(new_book)
```

### Think about it:

```text
Book(...)
   ↓
Create Python object
   ↓
db.add()
   ↓
Session
   ↓
db.commit()
   ↓
PostgreSQL
```

---

# 🧠 10. What is `Book(...)`?

This:

```python
new_book = Book(
    title="Python Basics",
    author="John",
    price=500
)
```

creates a Python object.

Think:

```text
new_book
   │
   ├── title = Python Basics
   ├── author = John
   └── price = 500
```

Then:

```python
db.add(new_book)
```

means:

> Add this object to the database session.

Then:

```python
db.commit()
```

means:

> Save it to PostgreSQL.

---

# ✏️ 11. UPDATE using ORM

Raw SQL:

```sql
UPDATE books
SET title = ...
WHERE book_id = ...;
```

ORM:

```python
book.title = updated_book.title
book.author = updated_book.author
book.price = updated_book.price

db.commit()
```

Full idea:

```python
book = db.query(Book).filter(
    Book.book_id == id
).first()

if book is None:
    return {
        "message": "Book not found"
    }

book.title = updated_book.title
book.author = updated_book.author
book.price = updated_book.price

db.commit()
```

Notice:

**You don't write `UPDATE`.**

You simply change the Python object's values.

---

# 🗑️ 12. DELETE using ORM

Raw SQL:

```sql
DELETE FROM books
WHERE book_id = 2;
```

ORM:

```python
book = db.query(Book).filter(
    Book.book_id == id
).first()

if book is None:
    return {
        "message": "Book not found"
    }

db.delete(book)

db.commit()
```

That's it.

---

# ⭐ 13. ORM CRUD Cheat Sheet

This is what you should memorize first:

### CREATE

```python
book = Book(...)
db.add(book)
db.commit()
```

### READ ALL

```python
db.query(Book).all()
```

### READ ONE

```python
db.query(Book).filter(
    Book.book_id == id
).first()
```

### UPDATE

```python
book.title = "New Title"
db.commit()
```

### DELETE

```python
db.delete(book)
db.commit()
```

---

# 🔥 14. Raw SQL → ORM

Keep this comparison in your notes:

| Operation | Raw SQL    | ORM                      |
| --------- | ---------- | ------------------------ |
| Create    | `INSERT`   | `db.add()`               |
| Read all  | `SELECT *` | `.query(Book).all()`     |
| Read one  | `WHERE`    | `.filter()`              |
| Update    | `UPDATE`   | Change object attributes |
| Delete    | `DELETE`   | `db.delete()`            |
| Save      | —          | `db.commit()`            |

---

# 🎯 Your Learning Path

Don't try to learn everything at once.

Learn ORM in this order:

```text
1️⃣ ORM Model
      ↓
2️⃣ Base
      ↓
3️⃣ Column
      ↓
4️⃣ db.query()
      ↓
5️⃣ filter()
      ↓
6️⃣ db.add()
      ↓
7️⃣ db.commit()
      ↓
8️⃣ db.delete()
```

Once these are clear, you'll be able to build the same Book CRUD API **without writing `text("SELECT...")`, `INSERT`, `UPDATE`, or `DELETE` manually**.
