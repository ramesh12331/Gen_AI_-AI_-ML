Sure 👍 Here are the **complete installation commands for Phase 1**, from creating the project to running the FastAPI application.

# 🚀 Phase 1 — Installation Commands

## 1️⃣ Create Project Folder

Open Command Prompt / PowerShell:

```bash
mkdir student_management_api
cd student_management_api
```

---

## 2️⃣ Create Virtual Environment ⭐

```bash
python -m venv venv
```

Activate it on **Windows**:

```bash
venv\Scripts\activate
```

You should see:

```text
(venv) C:\...\student_management_api>
```

That means the virtual environment is active.

---

## 3️⃣ Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 4️⃣ Install Required Packages

For our Phase 1 project:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

### What each package does

| Package           | Purpose                        |
| ----------------- | ------------------------------ |
| `fastapi`         | 🚀 Build API                   |
| `uvicorn`         | ▶️ Run FastAPI                 |
| `sqlalchemy`      | 🔄 ORM + database interaction  |
| `psycopg2-binary` | 🐘 Connect Python → PostgreSQL |
| `pydantic`        | ✅ Validate API data            |

---

## 5️⃣ Check Installation

```bash
pip list
```

You should see packages such as:

```text
fastapi
pydantic
psycopg2-binary
SQLAlchemy
uvicorn
```

---

# 🐘 6️⃣ PostgreSQL Setup

Make sure **PostgreSQL is installed and running**.

Create the database:

```sql
CREATE DATABASE fastapi_db;
```

Then our `database.py` uses:

```python
DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/fastapi_db"
```

Change:

```text
postgres
```

to your PostgreSQL username if different.

Change:

```text
ramesh
```

to your actual PostgreSQL password.

---

# 📁 7️⃣ Create Project Files

Your folder should contain:

```text
student_management_api/
│
├── venv/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
└── requirements.txt
```

You can create the files in VS Code.

---

# 📦 8️⃣ Create `requirements.txt`

Put this inside:

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
```

Later, you can install everything with one command:

```bash
pip install -r requirements.txt
```

### ⭐ Better workflow

After installing everything, save the exact installed versions:

```bash
pip freeze > requirements.txt
```

Then another computer can install the same dependencies with:

```bash
pip install -r requirements.txt
```

---

# ▶️ 9️⃣ Run FastAPI

Make sure your virtual environment is active:

```bash
venv\Scripts\activate
```

Then:

```bash
uvicorn main:app --reload
```

You should see something similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 🔟 Open Swagger UI

Go to:

```text
http://127.0.0.1:8000/docs
```

You should see:

```text
Student Management API

GET     /students
GET     /students/{id}
POST    /students
PUT     /students/{id}
DELETE  /students/{id}
```

---

# 🧪 1️⃣1️⃣ Quick Test

First test:

```text
GET /
```

Expected:

```json
{
    "message": "Student Management API is Working"
}
```

Then:

```text
POST /students
```

Send:

```json
{
    "name": "Ravi",
    "age": 21,
    "email": "ravi@gmail.com",
    "city": "Hyderabad"
}
```

---

# 🧠 Complete Command Cheat Sheet

```bash
# Create project
mkdir student_management_api

# Enter project
cd student_management_api

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install packages
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic

# Save dependencies
pip freeze > requirements.txt

# Run application
uvicorn main:app --reload
```

### Your complete flow

```text
1. Create folder
       ↓
2. Create venv
       ↓
3. Activate venv
       ↓
4. Install packages
       ↓
5. Create PostgreSQL database
       ↓
6. Create 4 Python files
       ↓
7. Write Phase 1 code
       ↓
8. Run uvicorn
       ↓
9. Open /docs
       ↓
10. Test CRUD
```

**One important beginner habit:** always activate `venv` before installing packages or running the project.
