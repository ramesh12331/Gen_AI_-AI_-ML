Absolutely 👍. Let's build **Phase 1 only**: a simple **Student Management API** with **FastAPI + Pydantic + PostgreSQL + SQLAlchemy ORM + CRUD**.

We will use only **one table** first. No relationships yet.

# 🚀 Phase 1 — Student Management API

## 📁 Folder Structure

```text
student_management_api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
└── requirements.txt
```

---

# 1️⃣ `database.py`

This file handles the **PostgreSQL connection and SQLAlchemy Session**.

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

### 🧠 Remember

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

This is our **SQLAlchemy ORM model**.

```python
from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):

    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    city = Column(String)
```

### 🧠 This means

```text
Python                     PostgreSQL

Student        →          students

student_id     →          student_id
name           →          name
age            →          age
email          →          email
city           →          city
```

---

# 3️⃣ `schemas.py`

This file handles **Pydantic validation**.

```python
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):

    name: str = Field(min_length=2)

    age: int = Field(
        gt=0,
        lt=100
    )

    email: str

    city: str = Field(min_length=2)
```

### Example valid data

```json
{
    "name": "Ravi",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

### Example invalid data

```json
{
    "name": "A",
    "age": -5,
    "email": "ravi@gmail.com",
    "city": "H"
}
```

Pydantic will reject it.

---

# 4️⃣ `main.py`

Now we connect **FastAPI + Pydantic + ORM + PostgreSQL**.

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, Base, engine
from models import Student
from schemas import StudentCreate


app = FastAPI()


# Create database tables
Base.metadata.create_all(bind=engine)


# --------------------------------
# DATABASE SESSION
# --------------------------------

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
        "message": "Student Management API is Working"
    }


# --------------------------------
# GET ALL STUDENTS
# --------------------------------

@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(Student).all()

    return students


# --------------------------------
# GET ONE STUDENT
# --------------------------------

@app.get("/students/{id}")
def get_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.student_id == id
    ).first()

    if student is None:

        return {
            "message": "Student not found"
        }

    return student


# --------------------------------
# CREATE STUDENT
# --------------------------------

@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(

        name=student.name,

        age=student.age,

        email=student.email,

        city=student.city
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student


# --------------------------------
# UPDATE STUDENT
# --------------------------------

@app.put("/students/{id}")
def update_student(
    id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    existing_student = db.query(Student).filter(
        Student.student_id == id
    ).first()

    if existing_student is None:

        return {
            "message": "Student not found"
        }

    existing_student.name = student.name

    existing_student.age = student.age

    existing_student.email = student.email

    existing_student.city = student.city

    db.commit()

    db.refresh(existing_student)

    return existing_student


# --------------------------------
# DELETE STUDENT
# --------------------------------

@app.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.student_id == id
    ).first()

    if student is None:

        return {
            "message": "Student not found"
        }

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }
```

---

# 5️⃣ `requirements.txt`

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
```

Install:

```bash
pip install -r requirements.txt
```

---

# 6️⃣ Create PostgreSQL Database

In PostgreSQL:

```sql
CREATE DATABASE fastapi_db;
```

You don't need to manually create the `students` table.

Because this line:

```python
Base.metadata.create_all(bind=engine)
```

will create it from the ORM model.

```text
models.py
    ↓
class Student
    ↓
Base.metadata.create_all()
    ↓
PostgreSQL
    ↓
students table
```

---

# 7️⃣ Run the Project

Open terminal inside the project folder:

```bash
uvicorn main:app --reload
```

Then open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 8️⃣ Test POST

Choose:

```text
POST /students
```

Click **Try it out**.

Send:

```json
{
    "name": "Ravi",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

You should get something like:

```json
{
    "student_id": 1,
    "name": "Ravi",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

---

# 🧪 9️⃣ Add More Students

### Student 2

```json
{
    "name": "Priya",
    "age": 22,
    "email": "priya@gmail.com",
    "city": "Bangalore"
}
```

### Student 3

```json
{
    "name": "Arjun",
    "age": 20,
    "email": "arjun@gmail.com",
    "city": "Chennai"
}
```

### Student 4

```json
{
    "name": "Sneha",
    "age": 23,
    "email": "sneha@gmail.com",
    "city": "Hyderabad"
}
```

---

# 🔍 10️⃣ Test GET

### Get all students

```text
GET /students
```

### Get one student

```text
GET /students/1
```

The flow is:

```text
/students/1
     ↓
id = 1
     ↓
db.query(Student)
     ↓
.filter(Student.student_id == 1)
     ↓
.first()
     ↓
Student object
```

---

# ✏️ 11️⃣ Test PUT

```text
PUT /students/1
```

Send:

```json
{
    "name": "Ravi Kumar",
    "age": 22,
    "email": "ravikumar@gmail.com",
    "city": "Hyderabad"
}
```

The ORM finds the student:

```python
existing_student = db.query(Student).filter(
    Student.student_id == id
).first()
```

Then we change the Python object:

```python
existing_student.name = student.name
existing_student.age = student.age
existing_student.email = student.email
existing_student.city = student.city
```

Then:

```python
db.commit()
```

SQLAlchemy saves those changes to PostgreSQL.

---

# 🗑️ 12️⃣ Test DELETE

```text
DELETE /students/1
```

ORM:

```python
db.delete(student)
db.commit()
```

---

# 🧠 Phase 1 Architecture

This is the most important thing to understand:

```text
                   Client
                     │
                     ↓
                FastAPI
                     │
                     ↓
              Pydantic Schema
                StudentCreate
                     │
                     ↓
                Validation
                     │
                     ↓
              SQLAlchemy ORM
                  Student
                     │
                     ↓
                  Session
                     │
                     ↓
                PostgreSQL
                  students
```

### Each file has ONE main job

```text
database.py
    ↓
Connection + Session

models.py
    ↓
Database table representation

schemas.py
    ↓
API data validation

main.py
    ↓
API endpoints + CRUD
```

### ⭐ Phase 1 CRUD cheat sheet

```python
# CREATE
db.add(student)
db.commit()


# READ ALL
db.query(Student).all()


# READ ONE
db.query(Student).filter(
    Student.student_id == id
).first()


# UPDATE
student.name = "New Name"
db.commit()


# DELETE
db.delete(student)
db.commit()
```

**Don't move to Phase 2 yet.** First make sure you can explain why `schemas.py`, `models.py`, `SessionLocal`, `Depends(get_db)`, `query()`, `filter()`, `add()`, `commit()`, and `refresh()` are each used. That will make the next phase—**Course + Foreign Key + ORM Relationships**—much easier.
