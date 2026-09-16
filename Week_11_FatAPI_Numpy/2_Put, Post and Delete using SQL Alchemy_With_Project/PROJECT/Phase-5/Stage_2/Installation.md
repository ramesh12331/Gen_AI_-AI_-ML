Yes 👍 Let's do **only the installation part** first.

# 🔐 Phase 5 — Authentication Installation

Since your Student Management API already has FastAPI, SQLAlchemy, PostgreSQL, etc., we only need to install the **new authentication packages**.

## Step 1 — Activate your virtual environment

Open **Command Prompt / PowerShell** inside your project folder:

```bash
cd student_management_api
```

Then activate:

```bash
venv\Scripts\activate
```

You should see something like:

```text
(venv) D:\...\student_management_api>
```

---

## Step 2 — Install authentication packages

Run:

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

These two packages are for:

| Package                     | Why we need it                  |
| --------------------------- | ------------------------------- |
| `python-jose[cryptography]` | Create and verify JWT tokens 🔑 |
| `passlib[bcrypt]`           | Hash and verify passwords 🔐    |

### Simple flow

```text
             Authentication
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
   Password              JWT
    Security            Security
        │                   │
        ↓                   ↓
 passlib[bcrypt]      python-jose
```

---

## Step 3 — Verify installation

Run:

```bash
pip show python-jose
```

and:

```bash
pip show passlib
```

You should see package information.

You can also run:

```bash
pip list
```

and look for:

```text
python-jose
passlib
```

---

## Step 4 — Update `requirements.txt`

After successful installation:

```bash
pip freeze > requirements.txt
```

Now your `requirements.txt` will contain your existing packages plus the authentication packages.

---

## Step 5 — Test the packages

Run:

```bash
python -c "from passlib.context import CryptContext; from jose import jwt; print('Authentication packages working!')"
```

Expected:

```text
Authentication packages working!
```

---

# ✅ Installation Complete

Your environment is now ready:

```text
FastAPI
   │
   ├── SQLAlchemy
   ├── PostgreSQL
   ├── Pydantic
   │
   └── Authentication
          │
          ├── Passlib + bcrypt
          │       ↓
          │   Password Hashing
          │
          └── python-jose
                  ↓
              JWT Token
```

**Next:** We'll create `models/user.py` and understand the **User table** step-by-step.
