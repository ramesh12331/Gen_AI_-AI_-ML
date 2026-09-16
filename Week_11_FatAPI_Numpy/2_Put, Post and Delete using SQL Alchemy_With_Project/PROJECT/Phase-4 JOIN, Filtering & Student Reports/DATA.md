Sure 👍 Here is a **complete consistent dataset** for your Phase 4 project. Use the data in this order: **Students → Courses → Marks** because `marks` depends on existing `student_id` and `course_id`.

## 👨‍🎓 1. Students — POST `/students/`

### Student 1

```json
{
  "name": "Ravi Kumar",
  "age": 21,
  "email": "ravi@gmail.com",
  "city": "Hyderabad"
}
```

### Student 2

```json
{
  "name": "Priya Sharma",
  "age": 22,
  "email": "priya@gmail.com",
  "city": "Bangalore"
}
```

### Student 3

```json
{
  "name": "Amit Reddy",
  "age": 20,
  "email": "amit@gmail.com",
  "city": "Hyderabad"
}
```

### Student 4

```json
{
  "name": "Sneha Patel",
  "age": 23,
  "email": "sneha@gmail.com",
  "city": "Mumbai"
}
```

### Student 5

```json
{
  "name": "Arjun Rao",
  "age": 21,
  "email": "arjun@gmail.com",
  "city": "Chennai"
}
```

Expected IDs:

```text
1 → Ravi Kumar
2 → Priya Sharma
3 → Amit Reddy
4 → Sneha Patel
5 → Arjun Rao
```

---

# 📚 2. Courses — POST `/courses/`

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

### Course 3

```json
{
  "course_name": "FastAPI",
  "duration": 4
}
```

### Course 4

```json
{
  "course_name": "Java",
  "duration": 5
}
```

### Course 5

```json
{
  "course_name": "Data Science",
  "duration": 8
}
```

Expected IDs:

```text
1 → Python
2 → SQL
3 → FastAPI
4 → Java
5 → Data Science
```

---

# 📝 3. Marks — POST `/marks/`

Now connect the students and courses.

### Ravi → Python

```json
{
  "student_id": 1,
  "course_id": 1,
  "marks": 85
}
```

### Ravi → SQL

```json
{
  "student_id": 1,
  "course_id": 2,
  "marks": 90
}
```

### Ravi → FastAPI

```json
{
  "student_id": 1,
  "course_id": 3,
  "marks": 88
}
```

### Ravi → Java

```json
{
  "student_id": 1,
  "course_id": 4,
  "marks": 82
}
```

---

### Priya → Python

```json
{
  "student_id": 2,
  "course_id": 1,
  "marks": 78
}
```

### Priya → SQL

```json
{
  "student_id": 2,
  "course_id": 2,
  "marks": 85
}
```

### Priya → Data Science

```json
{
  "student_id": 2,
  "course_id": 5,
  "marks": 91
}
```

---

### Amit → Python

```json
{
  "student_id": 3,
  "course_id": 1,
  "marks": 92
}
```

### Amit → FastAPI

```json
{
  "student_id": 3,
  "course_id": 3,
  "marks": 87
}
```

### Amit → Data Science

```json
{
  "student_id": 3,
  "course_id": 5,
  "marks": 89
}
```

---

### Sneha → SQL

```json
{
  "student_id": 4,
  "course_id": 2,
  "marks": 75
}
```

### Sneha → Java

```json
{
  "student_id": 4,
  "course_id": 4,
  "marks": 80
}
```

### Sneha → Data Science

```json
{
  "student_id": 4,
  "course_id": 5,
  "marks": 84
}
```

---

### Arjun → Python

```json
{
  "student_id": 5,
  "course_id": 1,
  "marks": 88
}
```

### Arjun → SQL

```json
{
  "student_id": 5,
  "course_id": 2,
  "marks": 93
}
```

### Arjun → FastAPI

```json
{
  "student_id": 5,
  "course_id": 3,
  "marks": 90
}
```

---

# 🧠 Final Database Relationship

After inserting everything:

```text
STUDENTS
────────────────────────
1  Ravi Kumar
2  Priya Sharma
3  Amit Reddy
4  Sneha Patel
5  Arjun Rao


COURSES
────────────────────────
1  Python
2  SQL
3  FastAPI
4  Java
5  Data Science


MARKS
────────────────────────────────
student_id  course_id  marks
    1          1         85
    1          2         90
    1          3         88
    1          4         82

    2          1         78
    2          2         85
    2          5         91

    3          1         92
    3          3         87
    3          5         89

    4          2         75
    4          4         80
    4          5         84

    5          1         88
    5          2         93
    5          3         90
```

## 🔗 Example JOIN

For:

```text
student_id = 1
```

the JOIN gives:

```text
Ravi Kumar
    │
    ├── Python      → 85
    ├── SQL         → 90
    ├── FastAPI     → 88
    └── Java        → 82
```

So you can test your Phase 4 APIs with meaningful data:

```text
GET /reports/student-marks
GET /reports/student/1
GET /reports/student-average/1
GET /reports/course-students
GET /students/search/by-city?city=Hyderabad
GET /marks/search/?minimum=85
```

For Ravi, the average is **86.25**.
