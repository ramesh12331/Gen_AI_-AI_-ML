Absolutely 👍. Since you have completed **Phase 1–4**, Phase 5 should introduce a major real-world backend concept:

# 🚀 Phase 5 — Authentication & Authorization

We will add:

* 🔐 User registration
* 🔑 Password hashing
* 🎫 JWT login
* 🛡️ Protected routes
* 👤 Current logged-in user
* 🔒 Role-based access (`admin` / `student`)

We will **not remove your Student/Course/Marks functionality**. We will add authentication around the existing project.

---

# 1. Phase 5 Architecture

Your project becomes:

```text
Client
  │
  ├── Register
  │       ↓
  │   Password Hash
  │       ↓
  │   PostgreSQL
  │
  └── Login
          ↓
      Verify Password
          ↓
       JWT Token
          ↓
    Authorization Header
          ↓
     Protected API
```

Example:

```text
POST /auth/register
POST /auth/login
GET  /auth/me
```

Then later:

```text
POST /students/
      ↓
   JWT required
      ↓
   Logged-in user
      ↓
   Create Student
```

---

# 📁 2. New Folder Structure

Add these files:

```text
student_management_api/
│
├── main.py
├── database.py
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── mark.py
│   └── user.py              ← NEW
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   ├── mark.py
│   └── user.py              ← NEW
│
├── routers/
│   ├── __init__.py
│   ├── students.py
│   ├── courses.py
│   ├── marks.py
│   ├── reports.py
│   └── auth.py              ← NEW
│
├── security.py               ← NEW
│
└── requirements.txt
```

---

# 3. Install Phase 5 Packages

Activate your virtual environment:

```bash
venv\Scripts\activate
```

Install:

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

Or install everything:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-jose[cryptography] passlib[bcrypt]
```

Update:

```bash
pip freeze > requirements.txt
```

---

# 4. `models/user.py`

Create the User ORM model.

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

---

# 🧠 Why store `password`?

We will **never store the actual password**.

User enters:

```text
mypassword123
```

We convert it into a hash:

```text
$2b$12$............
```

Database stores the hash.

```text
Password
   ↓
Hash
   ↓
PostgreSQL
```

---

# 5. Update `models/__init__.py`

Add `User`:

```python
from .student import Student
from .course import Course
from .mark import Mark
from .user import User
```

This is important so SQLAlchemy knows about the new model.

---

# 6. `schemas/user.py`

Create Pydantic schemas.

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


class UserResponse(BaseModel):

    user_id: int

    username: str

    email: str

    role: str


class Token(BaseModel):

    access_token: str

    token_type: str
```

---

# 7. Update `schemas/__init__.py`

```python
from .student import StudentCreate
from .course import CourseCreate
from .mark import MarkCreate

from .user import (
    UserRegister,
    UserLogin,
    UserResponse,
    Token
)
```

---

# 8. `security.py`

This file handles:

* Password hashing
* Password verification
* JWT creation
* JWT decoding

```python
from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
from jose import jwt


SECRET_KEY = "my-super-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# --------------------------------
# PASSWORD HASH
# --------------------------------

def hash_password(password: str):

    return pwd_context.hash(password)


# --------------------------------
# VERIFY PASSWORD
# --------------------------------

def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# --------------------------------
# CREATE JWT
# --------------------------------

def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
```

---

# 🧠 Password Flow

Suppose user registers:

```text
password = "python123"
```

Our code:

```python
hash_password("python123")
```

produces something like:

```text
$2b$12$................
```

We save that.

Later during login:

```text
User password
      ↓
verify_password()
      ↓
Compare with hash
      ↓
Correct?
      ↓
JWT token
```

---

# 9. `routers/auth.py`

Now create authentication routes.

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User

from schemas.user import (
    UserRegister,
    UserLogin
)

from security import (
    hash_password,
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# --------------------------------
# REGISTER
# --------------------------------

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:

        return {
            "message": "Username already exists"
        }


    hashed_password = hash_password(
        user.password
    )


    new_user = User(

        username=user.username,

        email=user.email,

        password=hashed_password,

        role="student"
    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return {
        "message": "User registered successfully",

        "user_id": new_user.user_id,

        "username": new_user.username
    }
```

---

# 🔑 10. Login Endpoint

Add this below the register endpoint:

```python
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()


    if existing_user is None:

        return {
            "message": "Invalid username or password"
        }


    password_correct = verify_password(
        user.password,
        existing_user.password
    )


    if not password_correct:

        return {
            "message": "Invalid username or password"
        }


    access_token = create_access_token({

        "sub": str(existing_user.user_id),

        "username": existing_user.username,

        "role": existing_user.role

    })


    return {

        "access_token": access_token,

        "token_type": "bearer"

    }
```

---

# 🧠 Login Flow

Suppose:

```text
username = Ravi
password = python123
```

Request:

```text
POST /auth/login
```

```json
{
    "username": "Ravi",
    "password": "python123"
}
```

Server:

```text
Find Ravi
   ↓
Get password hash
   ↓
Verify password
   ↓
Correct?
   ↓
Create JWT
   ↓
Return token
```

Response:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

---

# 1️⃣1️⃣ Current User Authentication

Now we need a function that reads the JWT.

Add to `security.py`:

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
```

---

# 1️⃣2️⃣ Protected Endpoint

We can now protect an endpoint.

In `routers/students.py`, import:

```python
from security import get_current_user
```

Then create:

```python
@router.get("/profile")
def student_profile(
    current_user = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user": current_user
    }
```

Now:

```text
GET /students/profile
```

requires a JWT token.

---

# ⚠️ Route Order

Put:

```python
@router.get("/profile")
```

**before**:

```python
@router.get("/{id}")
```

So your routes should be:

```python
@router.get("/profile")
def student_profile(...):
    ...


@router.get("/{id}")
def get_student(...):
    ...
```

Otherwise `/profile` can be interpreted as `{id}`.

---

# 1️⃣3️⃣ Protect Create Student

You can also require login to create students.

Change:

```python
@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
```

to:

```python
@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
```

Now:

```text
POST /students/
```

requires authentication.

---

# 1️⃣4️⃣ Protect Update

```python
@router.put("/{id}")
def update_student(
    id: int,
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
```

---

# 1️⃣5️⃣ Protect Delete

```python
@router.delete("/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
```

---

# 1️⃣6️⃣ Update `main.py`

Import the new model:

```python
from models.user import User
```

Import auth:

```python
from routers import auth
```

Then register:

```python
app.include_router(auth.router)
```

Complete:

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


Base.metadata.create_all(
    bind=engine
)


app.include_router(
    students.router
)

app.include_router(
    courses.router
)

app.include_router(
    marks.router
)

app.include_router(
    reports.router
)

app.include_router(
    auth.router
)


@app.get("/")
def home():

    return {
        "message": "Student Management API is Working"
    }
```

---

# 🧪 1️⃣7️⃣ Test Registration

Open:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
POST /auth/register
```

Send:

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

Expected:

```json
{
    "message": "User registered successfully",
    "user_id": 1,
    "username": "ravi"
}
```

---

# 🧪 1️⃣8️⃣ Test Login

Go to:

```text
POST /auth/login
```

Send:

```json
{
    "username": "ravi",
    "password": "python123"
}
```

You'll receive:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

Copy the `access_token`.

---

# 🔐 1️⃣9️⃣ Authorize Swagger

In Swagger UI, click:

```text
Authorize 🔒
```

Enter:

```text
Bearer eyJhbGciOiJIUzI1NiIs...
```

Then click:

```text
Authorize
```

Now Swagger sends:

```http
Authorization: Bearer <token>
```

with protected requests.

---

# 🧠 2️⃣0️⃣ JWT Flow

This is the most important concept in Phase 5:

```text
             REGISTER
                 │
                 ↓
           Plain Password
                 │
                 ↓
           Password Hash
                 │
                 ↓
             Database


              LOGIN
                 │
                 ↓
        Username + Password
                 │
                 ↓
          Verify Password
                 │
                 ↓
              JWT Token
                 │
                 ↓
              Client
                 │
                 ↓
        Authorization Header
                 │
                 ↓
          Protected API
                 │
                 ↓
        get_current_user()
                 │
                 ↓
             Allow/Deny
```

---

# 🔥 2️⃣1️⃣ What Does JWT Contain?

Our token contains:

```python
{
    "sub": "1",
    "username": "ravi",
    "role": "student"
}
```

`sub` means **subject** — here we're using it for the user's ID.

The token also has an expiration:

```python
"exp": expire
```

So the token is not valid forever.

---

# 🛡️ 2️⃣2️⃣ Authentication vs Authorization

Very important interview concept.

### Authentication

> **Who are you?**

Example:

```text
Login
 ↓
Username + Password
 ↓
JWT
```

### Authorization

> **What are you allowed to do?**

Example:

```text
Student
 ↓
Can view marks

Admin
 ↓
Can delete students
```

So:

```text
Authentication
       ↓
   Who are you?
       ↓
Authorization
       ↓
What can you do?
```

---

# 🎯 Phase 5 Learning Map

```text
Phase 1
Student CRUD
     ↓
Phase 2
Student + Course
     ↓
Phase 3
Marks + ForeignKey + Relationships
     ↓
Phase 4
JOIN + Reports + Filtering
     ↓
Phase 5 ⭐
Authentication
     ↓
Password Hashing
     ↓
JWT
     ↓
Protected Routes
     ↓
Authorization
```

### ⭐ Important beginner takeaway

You now have **four different layers**:

```text
FastAPI
   ↓
Pydantic
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL
```

Phase 5 adds a security layer:

```text
FastAPI
   ↓
Authentication 🔐
   ↓
Pydantic
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL
```

**One security note:** for a real production app, don't hard-code `SECRET_KEY` in `security.py`; put it in an environment variable and use a strong randomly generated secret. Also, if your existing database already has data, adding the `users` table is fine, but changing existing table structures later should be handled with migrations such as Alembic rather than relying on `create_all()`.
