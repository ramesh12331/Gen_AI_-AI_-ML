# 🐍 Pydantic — Beginner Summary

Pydantic in FastAPI is mainly used to **define the structure of incoming data and validate it**.

Think:

```text
Client / Swagger
      ↓
   JSON Data
      ↓
   Pydantic
      ↓
   Validation
      ↓
 FastAPI
      ↓
 Database
```

---

## 1. What is Pydantic?

Pydantic lets you create a **model** that describes what data your API expects.

```python
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    price: int
```

This means:

```text
Book
 ├── title  → string
 ├── author → string
 └── price  → integer
```

---

# 2. `BaseModel`

```python
from pydantic import BaseModel
```

Then:

```python
class Book(BaseModel):
```

`BaseModel` gives your class Pydantic's validation features.

Think:

```text
BaseModel
    ↓
Pydantic features
    ↓
Book model
```

---

# 3. Data Types

```python
class Book(BaseModel):

    title: str
    author: str
    price: int
```

### `str`

```python
title: str
```

Means:

> title should be text.

Example:

```json
{
    "title": "Python Basics"
}
```

### `int`

```python
price: int
```

Means:

> price should be an integer.

Example:

```json
{
    "price": 500
}
```

---

# 4. Pydantic Validation

You can add rules using `Field`.

```python
from pydantic import BaseModel, Field

class Book(BaseModel):

    title: str = Field(min_length=2)

    author: str = Field(min_length=2)

    price: int = Field(gt=0)
```

Now Pydantic checks the data before your database code runs.

---

# 5. Important `Field()` Rules

### `min_length`

```python
title: str = Field(min_length=2)
```

Minimum 2 characters.

```text
"A"       ❌
"Python"  ✅
```

---

### `max_length`

```python
title: str = Field(max_length=100)
```

Maximum 100 characters.

---

### `gt`

Means **greater than**.

```python
price: int = Field(gt=0)
```

```text
500  ✅
1    ✅
0    ❌
-10  ❌
```

---

### `ge`

Means **greater than or equal to**.

```python
price: int = Field(ge=0)
```

```text
500  ✅
0    ✅
-10  ❌
```

---

### `lt`

Means **less than**.

```python
price: int = Field(lt=1000)
```

```text
500  ✅
999  ✅
1000 ❌
```

---

### `le`

Means **less than or equal to**.

```python
price: int = Field(le=1000)
```

```text
1000 ✅
1001 ❌
```

---

# 6. Pydantic with POST

Instead of:

```python
def add_book(
    title: str,
    author: str,
    price: int
):
```

we use:

```python
def add_book(book: Book):
```

Now FastAPI expects a JSON request body.

```json
{
    "title": "Python Basics",
    "author": "John Smith",
    "price": 500
}
```

---

# 7. Where does `book.title` come from?

Your model:

```python
class Book(BaseModel):

    title: str
    author: str
    price: int
```

Client sends:

```json
{
    "title": "Python Basics",
    "author": "John Smith",
    "price": 500
}
```

Pydantic creates a `Book` object:

```text
book
 │
 ├── title  → "Python Basics"
 ├── author → "John Smith"
 └── price  → 500
```

Therefore:

```python
book.title
```

gives:

```text
Python Basics
```

```python
book.author
```

gives:

```text
John Smith
```

```python
book.price
```

gives:

```text
500
```

---

# 8. Pydantic + SQL

You can then send the validated values to SQLAlchemy:

```python
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
```

The flow is:

```text
JSON
 ↓
Pydantic
 ↓
Validation
 ↓
book.title
book.author
book.price
 ↓
SQLAlchemy
 ↓
PostgreSQL
```

---

# 9. What happens when validation fails?

Suppose your rules are:

```python
price: int = Field(gt=0)
```

But user sends:

```json
{
    "title": "Python",
    "author": "John",
    "price": -500
}
```

Pydantic checks:

```text
price = -500
     ↓
Is -500 > 0?
     ↓
NO ❌
     ↓
Validation Error
     ↓
Database INSERT does not run
```

FastAPI automatically returns a validation error response.

---

# 10. Pydantic vs PostgreSQL

This distinction is very important.

### Pydantic

Checks the **API input**:

```text
Is price an integer?
Is price greater than 0?
Is title long enough?
```

### PostgreSQL

Stores the **data**:

```text
books table
     ↓
title
author
price
```

So:

```text
Pydantic = Validation 🛡️

PostgreSQL = Storage 🗄️
```

---

# ⭐ Beginner Cheat Sheet

```python
from pydantic import BaseModel, Field
```

### Basic model

```python
class Book(BaseModel):

    title: str
    author: str
    price: int
```

### With validation

```python
class Book(BaseModel):

    title: str = Field(min_length=2, max_length=100)

    author: str = Field(min_length=2, max_length=100)

    price: int = Field(gt=0)
```

### Use in POST

```python
def add_book(book: Book):
```

### Access values

```python
book.title
book.author
book.price
```

---

# 🎯 Remember These 5 Things

```text
1️⃣ BaseModel
   ↓
   Creates Pydantic model

2️⃣ Type hints
   ↓
   str, int, float, bool

3️⃣ Field()
   ↓
   Adds validation rules

4️⃣ book.title
   ↓
   Gets validated data

5️⃣ Pydantic
   ↓
   Validates BEFORE database operation
```

### One-line definition 🧠

> **Pydantic is used in FastAPI to define the expected data structure and validate incoming data before processing it.**
