Absolutely 👍. **Phase 4** is where we start using the relationships we created in Phase 3 to get useful combined information.

# 🚀 Phase 4 — JOIN, Filtering & Student Reports

### Phase progression

```text
Phase 1
   ↓
Student CRUD

Phase 2
   ↓
Student + Course CRUD

Phase 3
   ↓
Marks + ForeignKey + relationship()

Phase 4 ⭐
   ↓
JOIN
   ↓
Filtering
   ↓
Student Course Report
   ↓
Course Student Report
   ↓
Average Marks
```

We will keep your existing Phase 3 code and **add new functionality**.

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
│   ├── marks.py
│   └── reports.py       ← NEW
│
└── requirements.txt
```

The main new file is:

```text
routers/reports.py
```

---

# 1️⃣ `database.py`

No change.

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

# 2️⃣ `models/student.py`

Keep your Phase 3 model:

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

---

# 3️⃣ `models/course.py`

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

---

# 4️⃣ `models/mark.py`

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

# 5️⃣ `models/__init__.py`

```python
from .student import Student
from .course import Course
from .mark import Mark
```

---

# ⭐ 6️⃣ New `routers/reports.py`

This is the most important new file in Phase 4.

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.student import Student
from models.course import Course
from models.mark import Mark


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
```

Now let's add our report APIs.

---

# 7️⃣ Get All Student Marks With Course Name

```python
@router.get("/student-marks")
def get_student_marks(
    db: Session = Depends(get_db)
):

    result = (
        db.query(
            Student.name,
            Course.course_name,
            Mark.marks
        )
        .join(
            Mark,
            Student.student_id == Mark.student_id
        )
        .join(
            Course,
            Course.course_id == Mark.course_id
        )
        .all()
    )

    return result
```

Call:

```text
GET /reports/student-marks
```

You get:

```json
[
    {
        "name": "Ravi",
        "course_name": "Python",
        "marks": 85
    },
    {
        "name": "Ravi",
        "course_name": "SQL",
        "marks": 90
    },
    {
        "name": "Ravi",
        "course_name": "FastAPI",
        "marks": 88
    },
    {
        "name": "Priya",
        "course_name": "Python",
        "marks": 78
    }
]
```

---

# 🧠 Understand the JOIN

Database:

```text
students
    │
    │ student_id
    ↓
  marks
    ↑
    │ course_id
    │
 courses
```

Our ORM:

```python
db.query(
    Student.name,
    Course.course_name,
    Mark.marks
)
```

means:

> I want these three pieces of information.

Then:

```python
.join(
    Mark,
    Student.student_id == Mark.student_id
)
```

connects:

```text
students.student_id
        =
marks.student_id
```

Then:

```python
.join(
    Course,
    Course.course_id == Mark.course_id
)
```

connects:

```text
courses.course_id
        =
marks.course_id
```

So:

```text
Student + Marks + Course
          ↓
        JOIN
          ↓
Combined result
```

---

# 8️⃣ Get One Student's Complete Report

Now create:

```text
GET /reports/student/{student_id}
```

Add to `reports.py`:

```python
@router.get("/student/{student_id}")
def get_student_report(
    student_id: int,
    db: Session = Depends(get_db)
):

    result = (
        db.query(
            Student.name,
            Course.course_name,
            Mark.marks
        )
        .join(
            Mark,
            Student.student_id == Mark.student_id
        )
        .join(
            Course,
            Course.course_id == Mark.course_id
        )
        .filter(
            Student.student_id == student_id
        )
        .all()
    )

    if not result:

        return {
            "message": "Student or marks not found"
        }

    return result
```

Call:

```text
GET /reports/student/1
```

For Ravi:

```json
[
    {
        "name": "Ravi",
        "course_name": "Python",
        "marks": 85
    },
    {
        "name": "Ravi",
        "course_name": "SQL",
        "marks": 90
    },
    {
        "name": "Ravi",
        "course_name": "FastAPI",
        "marks": 88
    }
]
```

---

# 9️⃣ Filter Students by City

Now let's add filtering.

Create this endpoint in `routers/students.py`:

```python
@router.get("/search/by-city")
def get_students_by_city(
    city: str,
    db: Session = Depends(get_db)
):

    students = db.query(Student).filter(
        Student.city == city
    ).all()

    return students
```

Call:

```text
GET /students/search/by-city?city=Hyderabad
```

Result:

```json
[
    {
        "student_id": 1,
        "name": "Ravi",
        "age": 21,
        "email": "ravi@gmail.com",
        "city": "Hyderabad"
    }
]
```

---

# ⚠️ Important Route Order

Because you already have:

```python
@router.get("/{id}")
```

put this route:

```python
@router.get("/search/by-city")
```

**before**:

```python
@router.get("/{id}")
```

Otherwise FastAPI may interpret:

```text
/search/by-city
```

as the `{id}` path.

So the order should be:

```python
@router.get("/search/by-city")
def get_students_by_city(...):
    ...


@router.get("/{id}")
def get_student(...):
    ...
```

---

# 🔟 Filter Marks Greater Than a Value

Add to `routers/marks.py`:

```python
@router.get("/search/")
def get_marks_above(
    minimum: int,
    db: Session = Depends(get_db)
):

    marks = db.query(Mark).filter(
        Mark.marks >= minimum
    ).all()

    return marks
```

Call:

```text
GET /marks/search/?minimum=85
```

This returns marks:

```text
85
90
88
92
87
```

---

# 1️⃣1️⃣ Get Students With Marks

Now create another useful JOIN:

```python
@router.get("/students-with-marks")
def get_students_with_marks(
    db: Session = Depends(get_db)
):

    result = (
        db.query(
            Student.name,
            Mark.marks
        )
        .join(
            Mark,
            Student.student_id == Mark.student_id
        )
        .all()
    )

    return result
```

Result:

```json
[
    {
        "name": "Ravi",
        "marks": 85
    },
    {
        "name": "Ravi",
        "marks": 90
    },
    {
        "name": "Ravi",
        "marks": 88
    },
    {
        "name": "Priya",
        "marks": 78
    }
]
```

---

# 1️⃣2️⃣ Get Course + Student + Marks

Add:

```python
@router.get("/course-students")
def get_course_students(
    db: Session = Depends(get_db)
):

    result = (
        db.query(
            Course.course_name,
            Student.name,
            Mark.marks
        )
        .join(
            Mark,
            Course.course_id == Mark.course_id
        )
        .join(
            Student,
            Student.student_id == Mark.student_id
        )
        .all()
    )

    return result
```

Result:

```json
[
    {
        "course_name": "Python",
        "name": "Ravi",
        "marks": 85
    },
    {
        "course_name": "SQL",
        "name": "Ravi",
        "marks": 90
    },
    {
        "course_name": "Python",
        "name": "Priya",
        "marks": 78
    }
]
```

---

# ⭐ 1️⃣3️⃣ Average Marks

Now we introduce SQL functions through ORM.

At the top of `reports.py` add:

```python
from sqlalchemy import func
```

Then:

```python
@router.get("/student-average/{student_id}")
def get_student_average(
    student_id: int,
    db: Session = Depends(get_db)
):

    result = (
        db.query(
            Student.name,
            func.avg(Mark.marks).label("average_marks")
        )
        .join(
            Mark,
            Student.student_id == Mark.student_id
        )
        .filter(
            Student.student_id == student_id
        )
        .group_by(
            Student.name
        )
        .first()
    )

    if result is None:

        return {
            "message": "Student or marks not found"
        }

    return {
        "student": result.name,
        "average_marks": round(
            float(result.average_marks),
            2
        )
    }
```

Call:

```text
GET /reports/student-average/1
```

For Ravi:

```json
{
    "student": "Ravi",
    "average_marks": 87.67
}
```

Because:

```text
85 + 90 + 88
--------------
      3

= 87.67
```

---

# 1️⃣4️⃣ Update `main.py`

Now register the new report router.

```python
from fastapi import FastAPI

from database import Base, engine

from models.student import Student
from models.course import Course
from models.mark import Mark

from routers import students
from routers import courses
from routers import marks
from routers import reports


app = FastAPI(
    title="Student Management API"
)


Base.metadata.create_all(bind=engine)


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


@app.get("/")
def home():

    return {
        "message": "Student Management API is Working"
    }
```

---

# 1️⃣5️⃣ `routers/__init__.py`

Keep it empty:

```python
```

---

# 🧪 1️⃣6️⃣ Phase 4 APIs

After running:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You will have:

```text
Students
│
├── GET    /students/
├── GET    /students/{id}
├── POST   /students/
├── PUT    /students/{id}
├── DELETE /students/{id}
└── GET    /students/search/by-city


Courses
│
├── GET
├── POST
├── PUT
└── DELETE


Marks
│
├── GET
├── POST
├── PUT
├── DELETE
└── GET /marks/search/


Reports ⭐
│
├── GET /reports/student-marks
├── GET /reports/student/{student_id}
├── GET /reports/students-with-marks
├── GET /reports/course-students
└── GET /reports/student-average/{student_id}
```

---

# 🧠 1️⃣7️⃣ Understand JOIN in Simple Way

Suppose we have:

### Students

```text
student_id | name
-----------|------
1          | Ravi
2          | Priya
```

### Marks

```text
student_id | course_id | marks
-----------|-----------|------
1          | 1         | 85
1          | 2         | 90
2          | 1         | 78
```

### Courses

```text
course_id | course_name
----------|------------
1         | Python
2         | SQL
```

A JOIN combines them:

```text
Ravi + Python + 85
Ravi + SQL    + 90
Priya + Python + 78
```

Visual:

```text
             STUDENTS
                │
                │ student_id
                ↓
              MARKS
                │
                │ course_id
                ↓
             COURSES
```

So `marks` acts as the **bridge**.

---

# 🔥 1️⃣8️⃣ ORM JOIN Pattern

Remember this pattern:

```python
db.query(
    Student.name,
    Course.course_name,
    Mark.marks
)
.join(
    Mark,
    Student.student_id == Mark.student_id
)
.join(
    Course,
    Course.course_id == Mark.course_id
)
.all()
```

Think:

```text
query()
   ↓
What columns do I want?

join()
   ↓
Which table do I connect?

filter()
   ↓
Which records do I want?

group_by()
   ↓
How do I group them?

all() / first()
   ↓
Get the result
```

---

# ⭐ Phase 4 Cheat Sheet

```text
JOIN
↓
Combine tables

FILTER
↓
Select specific records

GROUP BY
↓
Group records

func.avg()
↓
Calculate average

relationship()
↓
Navigate between related ORM objects
```

### Your project now looks like:

```text
                         FastAPI
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
         Students        Courses          Marks
             │              │              │
             └──────────────┼──────────────┘
                            ↓
                       Foreign Keys
                            ↓
                       Relationships
                            ↓
                           JOIN
                            ↓
                         Reports
                            ↓
                Useful Combined Data
```

**Phase 4 is the point where you're moving from basic CRUD to real backend/database development.** The next natural step after this would be **Phase 5: authentication + password hashing + JWT login + protected routes**.
