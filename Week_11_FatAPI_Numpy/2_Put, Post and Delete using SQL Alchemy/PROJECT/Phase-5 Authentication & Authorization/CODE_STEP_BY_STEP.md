Absolutely 👍 Since you are a **beginner in Authentication**, let's learn Phase 5 **slowly and step-by-step**.

We will **not write everything at once**. First understand the idea, then build each part.

# 🔐 Phase 5 — Authentication

Our goal is:

```text
User
  ↓
Register
  ↓
Password is hashed
  ↓
Database

User
  ↓
Login
  ↓
Check password
  ↓
JWT Token
  ↓
Access protected API
```

We will build these 5 steps:

```text
STEP 1 → Install authentication packages
STEP 2 → Create User database table
STEP 3 → Create User schemas
STEP 4 → Register user + hash password
STEP 5 → Login + JWT token
STEP 6 → Protect API routes
```

Let's start with **STEP 1 only**.

---

# STEP 1 — Install Authentication Packages

You already have the basic packages:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

Now authentication needs two additional packages:

### 1. `passlib`

Used for **password hashing**.

```text
password
   ↓
passlib
   ↓
hashed password
```

### 2. `python-jose`

Used to create and verify **JWT tokens**.

```text
username + password
       ↓
     login
       ↓
  JWT token
       ↓
 access protected API
```

Install them:

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

Then update your requirements file:

```bash
pip freeze > requirements.txt
```

---

# STEP 2 — Create User Table

Now we need a database table for users.

Create:

```text
models/
└── user.py
```

## `models/user.py`

```python
from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        default="student"
    )
```

Don't worry about all the code yet.

Let's understand it.

---

## What is `User`?

```python
class User(Base):
```

This is a Python class representing our database table.

```text
Python                         PostgreSQL

User class       ───────→      users table
```

---

## What does this mean?

```python
__tablename__ = "users"
```

It tells SQLAlchemy:

> Create/use a PostgreSQL table called `users`.

---

## `user_id`

```python
user_id = Column(
    Integer,
    primary_key=True
)
```

This is the unique ID of every user.

Example:

| user_id | username |
| ------: | -------- |
|       1 | ravi     |
|       2 | priya    |
|       3 | amit     |

---

## `username`

```python
username = Column(
    String,
    unique=True,
    nullable=False
)
```

### `String`

Username is text.

### `unique=True`

Two users cannot have the same username.

```text
ravi       ✅
ravi       ❌
```

### `nullable=False`

Username cannot be empty/NULL.

---

## `email`

```python
email = Column(
    String,
    unique=True,
    nullable=False
)
```

Same idea.

Two users cannot register with the same email.

---

## `password`

```python
password = Column(
    String,
    nullable=False
)
```

This stores the **hashed password**, not the original password.

Very important:

```text
User enters:

python123

       ↓

Hashing

       ↓

$2b$12$.........

       ↓

Database
```

We should **never store plain passwords** like:

```text
python123
```

---

## `role`

```python
role = Column(
    String,
    default="student"
)
```

This tells us what type of user it is.

For example:

```text
ravi    → student
admin   → admin
```

Later we can use this for **authorization**.

---

# STEP 3 — Update `models/__init__.py`

Your current file contains:

```python
from .student import Student
from .course import Course
from .mark import Mark
```

Add `User`:

```python
from .student import Student
from .course import Course
from .mark import Mark
from .user import User
```

Now Python can do:

```python
from models import User
```

---

# STEP 4 — Update `main.py`

We need SQLAlchemy to know about the new `User` model before creating tables.

Add:

```python
from models.user import User
```

Your important part of `main.py` becomes:

```python
from fastapi import FastAPI

from database import Base, engine

from models.student import Student
from models.course import Course
from models.mark import Mark
from models.user import User

from routers import students
from routers import courses
from routers import marks
from routers import reports
from routers import auth


app = FastAPI(
    title="Student Management API"
)


Base.metadata.create_all(bind=engine)


app.include_router(students.router)
app.include_router(courses.router)
app.include_router(marks.router)
app.include_router(reports.router)
app.include_router(auth.router)


@app.get("/")
def home():

    return {
        "message": "Student Management API is Working"
    }
```

### Why do we import `User`?

Because:

```python
Base.metadata.create_all(bind=engine)
```

needs to know about the `User` model.

Think:

```text
User class
   ↓
SQLAlchemy knows User
   ↓
create_all()
   ↓
PostgreSQL
   ↓
users table
```

---

# STEP 5 — Create User Schema

Now we need to tell FastAPI:

> What information should the user send?

Create:

```text
schemas/
└── user.py
```

Put:

```python
from pydantic import BaseModel, Field


class UserRegister(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: str

    password: str = Field(
        min_length=6
    )
```

This schema is used during registration.

For example:

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

---

# Why don't we put `user_id`?

Because the database creates the ID.

User sends:

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

Database creates:

```text
user_id = 1
```

So:

```text
Client
  ↓
username
email
password
  ↓
FastAPI
  ↓
Database
  ↓
user_id automatically created
```

---

# STEP 6 — Create Login Schema

Add this to the same file:

```python
class UserLogin(BaseModel):

    username: str

    password: str
```

Now the complete `schemas/user.py` is:

```python
from pydantic import BaseModel, Field


class UserRegister(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: str

    password: str = Field(
        min_length=6
    )


class UserLogin(BaseModel):

    username: str

    password: str
```

---

# STEP 7 — Update `schemas/__init__.py`

Add:

```python
from .user import UserRegister, UserLogin
```

So:

```python
from .student import StudentCreate
from .course import CourseCreate
from .mark import MarkCreate

from .user import UserRegister, UserLogin
```

---

# 🧠 Stop and Understand Here

At this point we have:

```text
                 AUTHENTICATION

                       │
                       ↓
              ┌─────────────────┐
              │   User Model    │
              │   user.py       │
              └────────┬────────┘
                       │
                       ↓
                PostgreSQL
                       │
                       ↓
                  users table


              ┌─────────────────┐
              │  User Schema    │
              │  user.py        │
              └────────┬────────┘
                       │
                       ↓
                 FastAPI input
```

We have **not created registration yet**.

That's the next important step.

---

# 📁 Your Project Now

Your structure should look like this:

```text
student_management_api/
│
├── main.py
├── database.py
├── security.py        ← we'll create this next
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── mark.py
│   └── user.py        ← NEW
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── mark.py
│   └── user.py        ← NEW
│
├── routers/
│   ├── __init__.py
│   ├── students.py
│   ├── courses.py
│   ├── marks.py
│   ├── reports.py
│   └── auth.py        ← we'll create this next
│
├── requirements.txt
└── venv/
```

## What we learned

| File               | Purpose                          |
| ------------------ | -------------------------------- |
| `models/user.py`   | Database `users` table           |
| `schemas/user.py`  | Validate registration/login data |
| `main.py`          | Register the User model          |
| `requirements.txt` | Authentication packages          |

### The most important concept

```text
MODEL
  ↓
Database structure

SCHEMA
  ↓
API input structure
```

Next, the **most important beginner step** is `security.py`, where we'll learn **password hashing** with a very simple example before putting it into the registration API.
