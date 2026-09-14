Absolutely 👍. Since **Phase 1 = Student CRUD** is clear, Phase 2 should add **Course management**.

We will **not add Marks or relationships yet**. That comes in Phase 3.

# 🚀 Phase 2 — Student + Course Management

## 🎯 What we learn in Phase 2

We now have **two independent tables**:

```text
students
courses
```

You will practice:

* Multiple ORM models
* Multiple Pydantic schemas
* Multiple routers
* CRUD for Course
* How a larger FastAPI project is organized

---

# 📁 1. Folder Structure

Change your project to:

```text
student_management_api/
│
├── main.py
├── database.py
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   └── course.py
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   └── course.py
│
├── routers/
│   ├── __init__.py
│   ├── students.py
│   └── courses.py
│
└── requirements.txt
```

### Why are we creating folders now?

In Phase 1:

```text
models.py
schemas.py
main.py
```

was okay because the project was small.

Now we have more resources:

```text
Student
Course
```

So we separate them:

```text
models/
    student.py
    course.py

schemas/
    student.py
    course.py

routers/
    students.py
    courses.py
```

---

# 1️⃣ `database.py`

Same database configuration:

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

---

# 2️⃣ `models/__init__.py`

For now, keep it simple:

```python
from .student import Student
from .course import Course
```

This allows us to import both models from `models`.

---

# 3️⃣ `models/student.py`

This is our Student ORM model.

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

---

# 4️⃣ `models/course.py`

Now create our second ORM model.

```python
from sqlalchemy import Column, Integer, String
from database import Base


class Course(Base):

    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)

    course_name = Column(String)

    duration = Column(Integer)
```

Our database now has:

```text
PostgreSQL
     │
     ├── students
     │
     └── courses
```

---

# 5️⃣ `schemas/__init__.py`

```python
from .student import StudentCreate
from .course import CourseCreate
```

---

# 6️⃣ `schemas/student.py`

Pydantic validation for Student.

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

---

# 7️⃣ `schemas/course.py`

Pydantic validation for Course.

```python
from pydantic import BaseModel, Field


class CourseCreate(BaseModel):

    course_name: str = Field(min_length=2)

    duration: int = Field(gt=0)
```

For example:

```json
{
    "course_name": "Python",
    "duration": 6
}
```

Pydantic checks:

```text
course_name → string → minimum 2 characters
duration    → integer → greater than 0
```

---

# 8️⃣ `routers/students.py`

Now move Student CRUD out of `main.py`.

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.student import Student
from schemas.student import StudentCreate


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# --------------------------------
# GET ALL STUDENTS
# --------------------------------

@router.get("/")
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(Student).all()

    return students


# --------------------------------
# GET ONE STUDENT
# --------------------------------

@router.get("/{id}")
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

@router.post("/")
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

@router.put("/{id}")
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

@router.delete("/{id}")
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

# 9️⃣ `routers/courses.py`

Now we create CRUD for Course.

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.course import Course
from schemas.course import CourseCreate


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# --------------------------------
# GET ALL COURSES
# --------------------------------

@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):

    courses = db.query(Course).all()

    return courses


# --------------------------------
# GET ONE COURSE
# --------------------------------

@router.get("/{id}")
def get_course(
    id: int,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.course_id == id
    ).first()

    if course is None:
        return {
            "message": "Course not found"
        }

    return course


# --------------------------------
# CREATE COURSE
# --------------------------------

@router.post("/")
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    new_course = Course(
        course_name=course.course_name,
        duration=course.duration
    )

    db.add(new_course)

    db.commit()

    db.refresh(new_course)

    return new_course


# --------------------------------
# UPDATE COURSE
# --------------------------------

@router.put("/{id}")
def update_course(
    id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    existing_course = db.query(Course).filter(
        Course.course_id == id
    ).first()

    if existing_course is None:
        return {
            "message": "Course not found"
        }

    existing_course.course_name = course.course_name

    existing_course.duration = course.duration

    db.commit()

    db.refresh(existing_course)

    return existing_course


# --------------------------------
# DELETE COURSE
# --------------------------------

@router.delete("/{id}")
def delete_course(
    id: int,
    db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.course_id == id
    ).first()

    if course is None:
        return {
            "message": "Course not found"
        }

    db.delete(course)

    db.commit()

    return {
        "message": "Course deleted successfully"
    }
```

---

# 🔟 `main.py`

Now `main.py` becomes very small.

```python
from fastapi import FastAPI

from database import Base, engine

from models.student import Student
from models.course import Course

from routers import students
from routers import courses


app = FastAPI(
    title="Student Management API"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register routers
app.include_router(students.router)

app.include_router(courses.router)


@app.get("/")
def home():

    return {
        "message": "Student Management API is Working"
    }
```

---

# 1️⃣1️⃣ `routers/__init__.py`

You can leave this empty:

```python
```

---

# 1️⃣2️⃣ `requirements.txt`

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
```

If your virtual environment is already activated from Phase 1, you **don't need to reinstall everything**.

You can simply run:

```bash
pip install -r requirements.txt
```

---

# 🗄️ 1️⃣3️⃣ Database Tables

You only need the database:

```sql
CREATE DATABASE fastapi_db;
```

You **do not need to manually create** the tables.

This line:

```python
Base.metadata.create_all(bind=engine)
```

creates:

```text
students
courses
```

based on your ORM models.

---

# ▶️ 1️⃣4️⃣ Run the Project

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You should now see:

```text
Student Management API

Students
  GET    /students/
  GET    /students/{id}
  POST   /students/
  PUT    /students/{id}
  DELETE /students/{id}

Courses
  GET    /courses/
  GET    /courses/{id}
  POST   /courses/
  PUT    /courses/{id}
  DELETE /courses/{id}
```

---

# 🧪 1️⃣5️⃣ Test Courses

### POST `/courses/`

Send:

```json
{
    "course_name": "Python",
    "duration": 6
}
```

Response:

```json
{
    "course_id": 1,
    "course_name": "Python",
    "duration": 6
}
```

Add another:

```json
{
    "course_name": "SQL",
    "duration": 3
}
```

Another:

```json
{
    "course_name": "FastAPI",
    "duration": 4
}
```

Database:

```text
courses

course_id | course_name | duration
----------|-------------|---------
1         | Python      | 6
2         | SQL         | 3
3         | FastAPI     | 4
```

---

# 🧠 The New Concept: Router

This is the **main new concept in Phase 2**.

In Phase 1:

```text
main.py
   ↓
Student CRUD
```

Now:

```text
main.py
   │
   ├───────────────┐
   ↓               ↓
students.py    courses.py
   ↓               ↓
Student CRUD    Course CRUD
```

`APIRouter()`:

```python
router = APIRouter(
    prefix="/students",
    tags=["Students"]
)
```

means:

> Put all Student-related endpoints into this router.

So:

```python
@router.get("/")
```

becomes:

```text
GET /students/
```

And:

```python
@router.get("/{id}")
```

becomes:

```text
GET /students/{id}
```

because we already defined:

```python
prefix="/students"
```

---

# ⭐ Phase 2 Architecture

```text
                         FastAPI
                            │
                         main.py
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
       students router              courses router
              │                           │
              ↓                           ↓
       Student Schema               Course Schema
       (Pydantic)                   (Pydantic)
              │                           │
              ↓                           ↓
       Student Model                Course Model
       (SQLAlchemy)                 (SQLAlchemy)
              │                           │
              └─────────────┬─────────────┘
                            ↓
                         Session
                            ↓
                       PostgreSQL
                       ┌────────┐
                       │students│
                       │courses │
                       └────────┘
```

# 🎯 What you should understand before Phase 3

Phase 1 taught:

```text
ORM CRUD
```

Phase 2 adds:

```text
Multiple Models
      +
Multiple Schemas
      +
APIRouter
      +
Project Structure
```

Then **Phase 3** is where this becomes much more interesting:

```text
Student
   │
   │ student_id
   ↓
Marks
   ↑
   │ course_id
   │
Course
```

That phase will teach you **ForeignKey + ORM relationships + joins + fetching a student's courses/marks**.
