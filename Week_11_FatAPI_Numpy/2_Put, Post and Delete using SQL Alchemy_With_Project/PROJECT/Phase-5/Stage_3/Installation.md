Sure 👍 For the **current step (Login + JWT)**, there is **no new installation** if you already installed the Phase 5 packages.

## 🔐 Phase 5 — JWT Installation

### 1. Activate your virtual environment

```bash
cd student_management_api
```

```bash
venv\Scripts\activate
```

You should see:

```text
(venv) ...
```

### 2. Install JWT package

If you haven't already installed it:

```bash
pip install python-jose[cryptography]
```

### 3. Password hashing package

Make sure this is also installed:

```bash
pip install passlib[bcrypt]
```

### 4. Install both at once

You can also simply run:

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

### 5. Update requirements

```bash
pip freeze > requirements.txt
```

### 6. Check installation

```bash
pip show python-jose
```

```bash
pip show passlib
```

You should see information for both packages.

### 7. Test imports

```bash
python -c "from jose import jwt; from passlib.context import CryptContext; print('JWT and Password Hashing are working!')"
```

Expected:

```text
JWT and Password Hashing are working!
```

---

### 📦 What each package does

```text
python-jose
     ↓
JWT Token
     ↓
Login authentication

passlib + bcrypt
     ↓
Password hashing
     ↓
Secure password storage
```

You are now ready for the next step: **protecting an API with JWT (`get_current_user`)**.
