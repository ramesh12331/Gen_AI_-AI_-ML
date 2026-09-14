Absolutely 👍 Let's understand the **PUT method** very slowly using your Student Management API.

# ✏️ What is PUT?

`PUT` means:

> **Find an existing record and update its data.**

For example, suppose PostgreSQL has:

```text
students

student_id | name  | age | email           | city
-----------|-------|-----|-----------------|----------
1          | Ravi  | 21  | ravi@gmail.com  | Hyderabad
```

Now Ravi changes his information:

```json
{
    "name": "Ravi Kumar",
    "age": 22,
    "email": "ravikumar@gmail.com",
    "city": "Bangalore"
}
```

We want to update **student_id = 1**.

---

# 1️⃣ PUT URL

Our endpoint is:

```python
@app.put("/students/{id}")
```

So we call:

```text
PUT /students/1
```

Here:

```text
/students/1
          ↑
          id = 1
```

That `1` tells us **which student we want to update**.

---

# 2️⃣ PUT Function

Our function is:

```python
@app.put("/students/{id}")
def update_student(
    id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
```

There are **three important things** here:

```text
id
↓
Which student?

student
↓
New information

db
↓
Database connection/session
```

Think:

```text
PUT /students/1

        ↓

id = 1

        +

New student data

        +

Database session
```

---

# 3️⃣ First: Find the Student

This is the most important line:

```python
existing_student = db.query(Student).filter(
    Student.student_id == id
).first()
```

Let's break it down.

### `db.query(Student)`

Means:

> Look at the `students` table through the `Student` ORM model.

```text
db.query(Student)
       ↓
students table
```

---

### `.filter()`

We want a particular student.

```python
.filter(
    Student.student_id == id
)
```

If:

```text
id = 1
```

then logically:

```python
Student.student_id == 1
```

Meaning:

> Find the student whose `student_id` is 1.

---

### `.first()`

```python
.first()
```

means:

> Give me the first matching record.

So:

```python
existing_student = db.query(Student).filter(
    Student.student_id == id
).first()
```

means:

> Find student number 1 and give me that student object.

---

# 4️⃣ What is `existing_student`?

Suppose database contains:

```text
student_id = 1
name = Ravi
age = 21
email = ravi@gmail.com
city = Hyderabad
```

After the query:

```python
existing_student
```

contains a Python ORM object representing that database row.

Conceptually:

```text
existing_student
       ↓
Student object
       ↓
id = 1
name = Ravi
age = 21
email = ravi@gmail.com
city = Hyderabad
```

---

# 5️⃣ Check If Student Exists

We have:

```python
if existing_student is None:
    return {
        "message": "Student not found"
    }
```

Why?

Because maybe the user requests:

```text
PUT /students/100
```

but student `100` doesn't exist.

Then:

```python
existing_student
```

will be:

```text
None
```

So we stop.

---

# 6️⃣ Now Update the Student ⭐

Suppose the request contains:

```json
{
    "name": "Ravi Kumar",
    "age": 22,
    "email": "ravikumar@gmail.com",
    "city": "Bangalore"
}
```

Pydantic gives us:

```python
student.name
student.age
student.email
student.city
```

Now we update the existing ORM object:

```python
existing_student.name = student.name
existing_student.age = student.age
existing_student.email = student.email
existing_student.city = student.city
```

This is the key concept.

### Before

```text
existing_student

name  = Ravi
age   = 21
email = ravi@gmail.com
city  = Hyderabad
```

### After

```text
existing_student

name  = Ravi Kumar
age   = 22
email = ravikumar@gmail.com
city  = Bangalore
```

We are changing the **Python ORM object**.

---

# 7️⃣ Is Database Updated Yet?

❌ Not permanently yet.

We need:

```python
db.commit()
```

This is very important.

```text
Change Python object
       ↓
db.commit()
       ↓
Save changes to PostgreSQL
```

So:

```python
db.commit()
```

means:

> Save the changes made during this transaction to the database.

---

# 8️⃣ Why `refresh()`?

Then we have:

```python
db.refresh(existing_student)
```

This tells SQLAlchemy:

> Get the latest version of this record from the database and refresh my Python object.

Then:

```python
return existing_student
```

returns the updated student.

---

# 🧩 Complete PUT Code

```python
@app.put("/students/{id}")
def update_student(
    id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    # 1. Find existing student
    existing_student = db.query(Student).filter(
        Student.student_id == id
    ).first()

    # 2. Check student exists
    if existing_student is None:
        return {
            "message": "Student not found"
        }

    # 3. Update values
    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email
    existing_student.city = student.city

    # 4. Save changes
    db.commit()

    # 5. Refresh object
    db.refresh(existing_student)

    # 6. Return updated student
    return existing_student
```

---

# 🎯 Understand PUT With a Real Example

Database initially:

```text
students

1 | Ravi | 21 | ravi@gmail.com | Hyderabad
```

We send:

```text
PUT /students/1
```

with:

```json
{
    "name": "Ravi Kumar",
    "age": 22,
    "email": "ravikumar@gmail.com",
    "city": "Bangalore"
}
```

### Step 1

```text
id = 1
```

↓

Find student 1.

### Step 2

```python
db.query(Student)
```

↓

Look at students.

### Step 3

```python
.filter(Student.student_id == 1)
```

↓

Find student 1.

### Step 4

```python
.first()
```

↓

Get student object.

### Step 5

```python
existing_student.name = student.name
```

↓

Change Ravi → Ravi Kumar.

### Step 6

```python
existing_student.age = student.age
```

↓

Change 21 → 22.

### Step 7

```python
db.commit()
```

↓

Save changes to PostgreSQL.

### Final database

```text
students

1 | Ravi Kumar | 22 | ravikumar@gmail.com | Bangalore
```

---

# 🧠 The Most Important Concept

Don't think of PUT as:

```text
PUT
 ↓
SQL UPDATE
```

When using ORM, think:

```text
PUT request
     ↓
Find existing ORM object
     ↓
Change object values
     ↓
commit()
     ↓
Database updated
```

Or remember this **5-step formula**:

```text
🔍 FIND
   ↓
✏️ CHANGE
   ↓
💾 COMMIT
   ↓
🔄 REFRESH
   ↓
📤 RETURN
```

### In code:

```python
# FIND
existing_student = db.query(Student).filter(
    Student.student_id == id
).first()

# CHANGE
existing_student.name = student.name
existing_student.age = student.age

# SAVE
db.commit()

# REFRESH
db.refresh(existing_student)

# RETURN
return existing_student
```

**This is the core pattern you should memorize for ORM UPDATE.**
