Absolutely 👍 **Phase 3** is the most important ORM step so far because now we connect the tables using **ForeignKey + ORM Relationships**.

We will build:

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

So we can answer questions like:

> "What courses did Ravi take and what marks did he get?"

---

# 🚀 Phase 3 — Students + Courses + Marks

## 🎯 What you will learn

```text
1. ForeignKey
2. relationship()
3. One-to-Many relationship
4. Multiple table ORM
5. Create marks
6. Get student's marks
7. Get course's students
8. JOIN-like queries using ORM
```

---

# 📁 1. Final Folder Structure

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
│   └── mark.py
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   ├── course.py
│   └── mark.py
│
├── routers/
│   ├── __init__.py
│   ├── students.py
│   ├── courses.py
│   └── marks.py
│
└── requirements.txt
```

---

# 2️⃣ `database.py`

No major change.

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

# 3️⃣ Student ORM Model

### `models/student.py`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):

    __tablename__ = "students"

    student_id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    age = Column(Integer)

    email = Column(String)

    city = Column(String)

    marks = relationship(
        "Mark",
        back_populates="student"
    )
```

### New part ⭐

```python
marks = relationship(
    "Mark",
    back_populates="student"
)
```

This tells SQLAlchemy:

> A Student can have multiple Mark records.

---

# 4️⃣ Course ORM Model

### `models/course.py`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Course(Base):

    __tablename__ = "courses"

    course_id = Column(
        Integer,
        primary_key=True
    )

    course_name = Column(String)

    duration = Column(Integer)

    marks = relationship(
        "Mark",
        back_populates="course"
    )
```

Again:

```python
marks = relationship(...)
```

means:

> A Course can have multiple Mark records.

---

# 5️⃣ Mark ORM Model ⭐⭐⭐

### `models/mark.py`

This is the new table that connects Students and Courses.

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Mark(Base):

    __tablename__ = "marks"

    mark_id = Column(
        Integer,
        primary_key=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    marks = Column(Integer)

    student = relationship(
        "Student",
        back_populates="marks"
    )

    course = relationship(
        "Course",
        back_populates="marks"
    )
```

---

# 🧠 Understand the Mark Table

The database will look like:

```text
marks

mark_id | student_id | course_id | marks
--------|------------|-----------|------
1       | 1          | 1         | 85
2       | 1          | 2         | 90
3       | 2          | 1         | 78
```

Think:

```text
student_id
    ↓
students.student_id
```

and:

```text
course_id
    ↓
courses.course_id
```

These are **Foreign Keys**.

---

# 6️⃣ `models/__init__.py`

```python
from .student import Student
from .course import Course
from .mark import Mark
```

This is important because SQLAlchemy needs to know about all three models before creating the tables.

---

# 7️⃣ Student Schema

### `schemas/student.py`

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

# 8️⃣ Course Schema

### `schemas/course.py`

```python
from pydantic import BaseModel, Field


class CourseCreate(BaseModel):

    course_name: str = Field(
        min_length=2
    )

    duration: int = Field(
        gt=0
    )
```

---

# 9️⃣ Mark Schema

### `schemas/mark.py`

```python
from pydantic import BaseModel, Field


class MarkCreate(BaseModel):

    student_id: int = Field(
        gt=0
    )

    course_id: int = Field(
        gt=0
    )

    marks: int = Field(
        ge=0,
        le=100
    )
```

This means:

```text
marks
 ↓
minimum = 0
maximum = 100
```

So:

```json
{
    "student_id": 1,
    "course_id": 1,
    "marks": 85
}
```

is valid.

But:

```json
{
    "student_id": 1,
    "course_id": 1,
    "marks": 150
}
```

is invalid.

---

# 🔟 `schemas/__init__.py`

```python
from .student import StudentCreate
from .course import CourseCreate
from .mark import MarkCreate
```

---

# 1️⃣1️⃣ Student Router

### `routers/students.py`

We can keep the same Student CRUD from Phase 2.

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


@router.get("/")
def get_students(
    db: Session = Depends(get_db)
):

    return db.query(Student).all()


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

# 1️⃣2️⃣ Course Router

### `routers/courses.py`

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


@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):

    return db.query(Course).all()


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

# 1️⃣3️⃣ Marks Router ⭐

### `routers/marks.py`

This is the important new part.

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.mark import Mark
from models.student import Student
from models.course import Course
from schemas.mark import MarkCreate


router = APIRouter(
    prefix="/marks",
    tags=["Marks"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# --------------------------------
# GET ALL MARKS
# --------------------------------

@router.get("/")
def get_marks(
    db: Session = Depends(get_db)
):

    return db.query(Mark).all()


# --------------------------------
# GET ONE MARK
# --------------------------------

@router.get("/{id}")
def get_mark(
    id: int,
    db: Session = Depends(get_db)
):

    mark = db.query(Mark).filter(
        Mark.mark_id == id
    ).first()

    if mark is None:
        return {
            "message": "Mark not found"
        }

    return mark


# --------------------------------
# CREATE MARK
# --------------------------------

@router.post("/")
def create_mark(
    mark: MarkCreate,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.student_id == mark.student_id
    ).first()

    if student is None:
        return {
            "message": "Student not found"
        }


    course = db.query(Course).filter(
        Course.course_id == mark.course_id
    ).first()

    if course is None:
        return {
            "message": "Course not found"
        }


    new_mark = Mark(
        student_id=mark.student_id,
        course_id=mark.course_id,
        marks=mark.marks
    )

    db.add(new_mark)

    db.commit()

    db.refresh(new_mark)

    return new_mark


# --------------------------------
# UPDATE MARK
# --------------------------------

@router.put("/{id}")
def update_mark(
    id: int,
    mark: MarkCreate,
    db: Session = Depends(get_db)
):

    existing_mark = db.query(Mark).filter(
        Mark.mark_id == id
    ).first()

    if existing_mark is None:
        return {
            "message": "Mark not found"
        }


    existing_mark.student_id = mark.student_id

    existing_mark.course_id = mark.course_id

    existing_mark.marks = mark.marks

    db.commit()

    db.refresh(existing_mark)

    return existing_mark


# --------------------------------
# DELETE MARK
# --------------------------------

@router.delete("/{id}")
def delete_mark(
    id: int,
    db: Session = Depends(get_db)
):

    mark = db.query(Mark).filter(
        Mark.mark_id == id
    ).first()

    if mark is None:
        return {
            "message": "Mark not found"
        }

    db.delete(mark)

    db.commit()

    return {
        "message": "Mark deleted successfully"
    }
```

---

# 1️⃣4️⃣ Relationship APIs ⭐

Now let's use the ORM relationship.

Add these endpoints to `routers/students.py`:

```python
@router.get("/{id}/marks")
def get_student_marks(
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

    return student.marks
```

Now:

```text
GET /students/1/marks
```

returns all marks belonging to student 1.

---

# 1️⃣5️⃣ Course Marks

Add to `routers/courses.py`:

```python
@router.get("/{id}/marks")
def get_course_marks(
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

    return course.marks
```

Now:

```text
GET /courses/1/marks
```

returns all marks for course 1.

---

# 1️⃣6️⃣ `main.py`

```python
from fastapi import FastAPI

from database import Base, engine

# Import all models
from models.student import Student
from models.course import Course
from models.mark import Mark

# Import routers
from routers import students
from routers import courses
from routers import marks


app = FastAPI(
    title="Student Management API"
)


# Create tables
Base.metadata.create_all(bind=engine)


# Register routers
app.include_router(students.router)

app.include_router(courses.router)

app.include_router(marks.router)


@app.get("/")
def home():

    return {
        "message": "Student Management API is Working"
    }
```

---

# 1️⃣7️⃣ `routers/__init__.py`

Leave it empty:

```python
```

---

# 🧪 1️⃣8️⃣ Test in Swagger

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You should see:

```text
Students
    GET
    POST
    PUT
    DELETE
    GET /students/{id}/marks

Courses
    GET
    POST
    PUT
    DELETE
    GET /courses/{id}/marks

Marks
    GET
    POST
    PUT
    DELETE
```

---

# 🧪 1️⃣9️⃣ Add Students

### Student 1

```json
{
    "name": "Ravi",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

### Student 2

```json
{
    "name": "Priya",
    "age": 22,
    "email": "priya@gmail.com",
    "city": "Bangalore"
}
```

---

# 🧪 2️⃣0️⃣ Add Courses

### Course 1

```json
{
    "course_name": "Python",
    "duration": 6
}
```

### Course 2

```json
{
    "course_name": "SQL",
    "duration": 3
}
```

---

# 🧪 2️⃣1️⃣ Add Marks

Now we connect them.

```text
Student 1 = Ravi
Course 1  = Python
Marks     = 85
```

POST:

```text
POST /marks/
```

```json
{
    "student_id": 1,
    "course_id": 1,
    "marks": 85
}
```

Another:

```json
{
    "student_id": 1,
    "course_id": 2,
    "marks": 90
}
```

Another:

```json
{
    "student_id": 2,
    "course_id": 1,
    "marks": 78
}
```

Your database becomes:

```text
students

1 | Ravi  | 21 | ravi@gmail.com  | Hyderabad
2 | Priya | 22 | priya@gmail.com | Bangalore
```

```text
courses

1 | Python | 6
2 | SQL    | 3
```

```text
marks

1 | 1 | 1 | 85
2 | 1 | 2 | 90
3 | 2 | 1 | 78
```

---

# 🧠 2️⃣2️⃣ Understand the Relationship

This is the most important part of Phase 3.

```text
                 students
                    │
                    │
             student_id = 1
                    │
                    ↓
                  marks
                    ↑
                    │
              course_id = 1
                    │
                    │
                 courses
```

For Ravi:

```text
Ravi
 ↓
student_id = 1
 ↓
marks
 ├── Python → 85
 └── SQL    → 90
```

---

# ⭐ What `relationship()` Does

In `Student`:

```python
marks = relationship(
    "Mark",
    back_populates="student"
)
```

It allows:

```python
student.marks
```

to access the student's marks.

Similarly in `Mark`:

```python
student = relationship(
    "Student",
    back_populates="marks"
)
```

allows:

```python
mark.student
```

to access the student.

So:

```text
student.marks
     ↓
List of Mark objects
```

and:

```text
mark.student
     ↓
Student object
```

---

# ⭐ What `ForeignKey()` Does

This:

```python
student_id = Column(
    Integer,
    ForeignKey("students.student_id")
)
```

means:

> `marks.student_id` must refer to a valid `students.student_id`.

And:

```python
course_id = Column(
    Integer,
    ForeignKey("courses.course_id")
)
```

means:

> `marks.course_id` must refer to a valid `courses.course_id`.

---

# 🎯 Phase 3 Big Picture

```text
                    FastAPI
                       │
            ┌──────────┼──────────┐
            ↓          ↓          ↓
        Students    Courses     Marks
            │          │          │
            ↓          ↓          ↓
        Student      Course       Mark
          ORM          ORM        ORM
            │          │          │
            │          │          │
            └──────────┼──────────┘
                       ↓
                 Foreign Keys
                       ↓
                  Relationships
                       ↓
                  PostgreSQL
```

### Phase progression

```text
Phase 1
   ↓
Student CRUD
   ↓
Phase 2
   ↓
Student + Course CRUD
   ↓
Phase 3
   ↓
Student + Course + Marks
   ↓
ForeignKey
   ↓
relationship()
   ↓
Multiple-table queries
```

**One important beginner note:** if you already have `students` and `courses` tables from Phase 2, `create_all()` will create the new `marks` table, but it will **not modify existing tables**. That's fine here because we're only adding the new `marks` table.
---
---
![main img](./img/img.png)