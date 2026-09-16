Great 👍 Now let's continue with the **next step: Password Hashing**.

# 🔐 STEP 8 — Create `security.py`

The main idea is:

```text
User password
     ↓
"python123"
     ↓
Hashing
     ↓
"$2b$12$........"
     ↓
Database
```

We **do not store the real password** in the database.

---

## 8.1 Create `security.py`

Your project currently has:

```text
student_management_api/
│
├── main.py
├── database.py
├── security.py   ← CREATE THIS
│
├── models/
├── schemas/
└── routers/
```

Create:

```text
security.py
```

---

## 8.2 Import `CryptContext`

Put this in `security.py`:

```python
from passlib.context import CryptContext
```

### Why?

`CryptContext` gives us password hashing functionality.

---

# 8.3 Create password context

Add:

```python
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
```

### What is `bcrypt`?

`bcrypt` is a password-hashing algorithm.

Think:

```text
Normal password
      ↓
    bcrypt
      ↓
Hashed password
```

For example:

```text
python123
```

might become something like:

```text
$2b$12$LQv3c1yqBW...
```

The actual hash will be different each time.

---

# 8.4 Create `hash_password()`

Add:

```python
def hash_password(password: str):

    return pwd_context.hash(password)
```

This function receives a normal password and returns a hashed password.

Example:

```python
hashed = hash_password("python123")

print(hashed)
```

Output will look similar to:

```text
$2b$12$......................
```

---

# 8.5 Create `verify_password()`

Now we need another function.

```python
def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )
```

This is used during **login**.

---

# 🧠 Why do we need `verify_password()`?

Suppose registration:

```text
User enters:

python123

      ↓
   hash_password()

      ↓
$2b$12$........
```

Database stores:

```text
$2b$12$........
```

Later, during login:

```text
User enters:

python123

      ↓
verify_password()

      ↓
Compare with database hash

      ↓
True ✅
```

If the user enters:

```text
wrong123
```

then:

```text
verify_password()

      ↓

False ❌
```

---

# 8.6 Complete `security.py`

For now, keep it simple.

```python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )
```

---

# 🧪 STEP 9 — Test Password Hashing

Before connecting it to FastAPI, let's understand it.

You can temporarily add this at the bottom of `security.py`:

```python
password = "python123"

hashed_password = hash_password(password)

print("Original password:", password)
print("Hashed password:", hashed_password)

result = verify_password(
    password,
    hashed_password
)

print("Password correct:", result)
```

Run:

```bash
python security.py
```

You should get something similar to:

```text
Original password: python123

Hashed password:
$2b$12$............................

Password correct: True
```

---

# 🔍 Test Wrong Password

Change:

```python
result = verify_password(
    password,
    hashed_password
)
```

to:

```python
result = verify_password(
    "wrong123",
    hashed_password
)
```

Now:

```text
Password correct: False
```

---

# ⚠️ Important

After testing, **remove this testing code**:

```python
password = "python123"

hashed_password = hash_password(password)

print("Original password:", password)
print("Hashed password:", hashed_password)

result = verify_password(
    password,
    hashed_password
)

print("Password correct:", result)
```

Your final `security.py` should contain only:

```python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )
```

---

# 🔐 STEP 10 — Now Create Registration API

Now we will connect:

```text
FastAPI
   ↓
Registration
   ↓
Pydantic Schema
   ↓
Hash Password
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Create:

```text
routers/auth.py
```

---

## 10.1 Imports

Start with:

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRegister
from security import hash_password
```

---

## 10.2 Create router

```python
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
```

This means our URLs will start with:

```text
/auth
```

For example:

```text
/auth/register
/auth/login
```

---

# 10.3 Create database dependency

Use the same pattern you've already learned:

```python
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
```

Remember:

```text
SessionLocal()
     ↓
Database session
     ↓
Use database
     ↓
db.close()
```

---

# 10.4 Create Register API

Now add:

```python
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

# 🧠 Understand This Code Step-by-Step

### 1. User sends data

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

FastAPI puts this into:

```python
user: UserRegister
```

---

### 2. Check username

```python
existing_user = db.query(User).filter(
    User.username == user.username
).first()
```

Meaning:

```text
Database
   ↓
Search users
   ↓
username == "ravi"
```

If Ravi already exists:

```python
if existing_user:
```

return:

```json
{
    "message": "Username already exists"
}
```

---

### 3. Hash password

```python
hashed_password = hash_password(
    user.password
)
```

Input:

```text
python123
```

Output:

```text
$2b$12$................
```

---

### 4. Create User object

```python
new_user = User(
    username=user.username,
    email=user.email,
    password=hashed_password,
    role="student"
)
```

Notice something important:

We store:

```python
password=hashed_password
```

NOT:

```python
password=user.password
```

---

### 5. Add to database

```python
db.add(new_user)
```

Means:

> Add this new User object to the database session.

---

### 6. Save permanently

```python
db.commit()
```

Means:

> Save the change to PostgreSQL.

---

### 7. Get generated ID

```python
db.refresh(new_user)
```

After inserting:

```text
PostgreSQL
     ↓
user_id = 1
```

`refresh()` gets the latest database values back into the Python object.

---

# 📁 Complete `routers/auth.py`

At this stage:

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRegister
from security import hash_password


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

# STEP 11 — Connect `auth.py` to `main.py`

In `main.py`:

```python
from routers import auth
```

And:

```python
app.include_router(auth.router)
```

So your relevant section becomes:

```python
from routers import students
from routers import courses
from routers import marks
from routers import reports
from routers import auth


app.include_router(students.router)
app.include_router(courses.router)
app.include_router(marks.router)
app.include_router(reports.router)
app.include_router(auth.router)
```

---

# 🚀 STEP 12 — Run the API

Start:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You should now see:

```text
Authentication

POST /auth/register
```

---

# 🧪 STEP 13 — Test Registration

Click:

```text
POST /auth/register
```

Then:

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

Click **Execute**.

Expected response:

```json
{
    "message": "User registered successfully",
    "user_id": 1,
    "username": "ravi"
}
```

---

# 🔎 Check PostgreSQL

Your database should now contain:

```text
users
-----------------------------------------------
user_id | username | email          | password
-----------------------------------------------
1       | ravi     | ravi@gmail.com | $2b$12$...
```

Notice:

❌ Database does NOT contain:

```text
python123
```

Instead it contains:

```text
$2b$12$.................
```

That's **password hashing**. 🔐

---

# 🎯 What We Have Built

```text
                 REGISTER

User
 │
 │ username
 │ email
 │ password
 ↓
FastAPI
 │
 ↓
UserRegister
 │
 ↓
Check username
 │
 ↓
hash_password()
 │
 ↓
Hashed password
 │
 ↓
User()
 │
 ↓
db.add()
 │
 ↓
db.commit()
 │
 ↓
PostgreSQL
```

### Next step

The next part is **LOGIN**:

```text
Username + Password
        ↓
Find user
        ↓
Get hashed password
        ↓
verify_password()
        ↓
Correct?
   ↙          ↘
 YES           NO
  ↓             ↓
JWT Token     Reject
```

Then we'll learn **JWT token** from the beginning and add `/auth/login`.
