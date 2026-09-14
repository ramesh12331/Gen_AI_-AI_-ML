Sure 👍 Since **Phase 1 is already installed**, Phase 2 does **not require any new Python packages**. We are only adding folders/files and using the same packages.

# 🚀 Phase 2 Installation & Setup

## 1️⃣ Go to Your Project

```bash
cd student_management_api
```

If you haven't created the project yet:

```bash
mkdir student_management_api
cd student_management_api
```

---

## 2️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

You should see:

```text
(venv) C:\...\student_management_api>
```

---

## 3️⃣ Install Packages

If you already completed Phase 1, you can skip this.

Otherwise:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

Or using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Verify Packages

```bash
pip list
```

You should have:

```text
fastapi
uvicorn
SQLAlchemy
psycopg2-binary
pydantic
```

---

# 🐘 5️⃣ PostgreSQL

Make sure PostgreSQL is running.

You need the database:

```sql
CREATE DATABASE fastapi_db;
```

If you already created `fastapi_db` in Phase 1, **don't create it again**.

Your connection in `database.py`:

```python
DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"
```

Change the username/password if yours are different.

---

# 📁 6️⃣ Create Phase 2 Folders

Inside `student_management_api`:

```bash
mkdir models
mkdir schemas
mkdir routers
```

Then create these files:

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

You can create the files directly in VS Code.

---

# ▶️ 7️⃣ Run Phase 2

From the project root:

```bash
uvicorn main:app --reload
```

You should see:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 8️⃣ Open Swagger

Open:

```text
http://127.0.0.1:8000/docs
```

You should see:

```text
Student Management API

Students
    GET
    POST
    PUT
    DELETE

Courses
    GET
    POST
    PUT
    DELETE
```

---

# 🧪 9️⃣ Check Database Tables

Because we have:

```python
Base.metadata.create_all(bind=engine)
```

SQLAlchemy will create:

```text
fastapi_db
    │
    ├── students
    │
    └── courses
```

You can check in PostgreSQL:

```sql
SELECT * FROM students;
```

and:

```sql
SELECT * FROM courses;
```

---

# ⭐ Complete Installation Commands

For a **fresh setup**, run:

```bash
mkdir student_management_api
cd student_management_api

python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic

pip freeze > requirements.txt

uvicorn main:app --reload
```

For your **existing Phase 1 project**, simply:

```bash
cd student_management_api

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

### 🧠 Phase 2 requires no new library

```text
Phase 1
   ↓
FastAPI
Pydantic
SQLAlchemy
PostgreSQL
   ↓
Phase 2
   ↓
Same packages ✅
+
routers/
+
multiple models
+
multiple schemas
```

So you can focus on learning **`APIRouter` and the new project structure** rather than installing anything new.
