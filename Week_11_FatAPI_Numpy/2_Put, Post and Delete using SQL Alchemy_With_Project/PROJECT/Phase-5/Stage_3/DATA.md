Sure 👍 Here is **sample User data** for testing your `/auth/register` API.

### 👤 User 1 — Student

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

### 👤 User 2 — Student

```json
{
    "username": "priya",
    "email": "priya@gmail.com",
    "password": "fastapi123"
}
```

### 👤 User 3 — Student

```json
{
    "username": "amit",
    "email": "amit@gmail.com",
    "password": "sql12345"
}
```

### 👤 User 4 — Student

```json
{
    "username": "sneha",
    "email": "sneha@gmail.com",
    "password": "student123"
}
```

### 👤 User 5 — Student

```json
{
    "username": "arjun",
    "email": "arjun@gmail.com",
    "password": "python456"
}
```

## 🧪 Test in Swagger

Open:

```text
http://127.0.0.1:8000/docs
```

Choose:

```text
POST /auth/register
```

Start with Ravi:

```json
{
    "username": "ravi",
    "email": "ravi@gmail.com",
    "password": "python123"
}
```

Expected response:

```json
{
    "message": "User registered successfully",
    "user_id": 1,
    "username": "ravi"
}
```

Then register the other users one by one.

### ⚠️ Important

For `/auth/register`, **do not send**:

```json
{
    "user_id": 1,
    "role": "student"
}
```

The database creates `user_id`, and your code automatically sets:

```python
role="student"
```

So the user only sends:

```text
username
email
password
```

After registration, we can move to the **LOGIN step** and learn exactly how `username + password → JWT token` works.
