from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Student
from database import SessionLocal, Base, engine
from schemas import StudentCreate

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def home():
    return{
        "message" : "Student Management API is Working"
    }

@app.get("/students")
def get_students(connection:Session = Depends(get_db)):
    students = connection.query(Student).all()
    return students

@app.get("/students/{id}")
def get_student(id:int, connection:Session = Depends(get_db)):
    student = connection.query(Student).filter(Student.student_id == id).first()
    if student is None:
        return{
            "message" : "Student not found"
        }
    return student

@app.post("/student")
def create_student(student:StudentCreate, connection:Session = Depends(get_db)):
    new_student = Student(
        name = student.name,
        age = student.age,
        email = student.email,
        city = student.city
    )
    connection.add(new_student)
    connection.commit()
    connection.refresh(new_student)

    return new_student

@app.put("/student/{id}")
def update_student(id:int, student:StudentCreate, connection:Session = Depends(get_db)):
    existing_student = connection.query(Student).filter(Student.student_id == id).first()

    if existing_student is None:
        return{
            "message" : "Student not found"
        }
    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email
    existing_student.city = student.city

    connection.commit()
    connection.refresh(existing_student)

    return existing_student

@app.delete("/student/{id}")
def delete_student(id:int, connection:Session = Depends(get_db)):
    student = connection.query(Student).filter(Student.student_id == id).first()

    if student is None:
        return {
            "message" : "Student Not Found"
        }
    connection.delete(student)
    connection.commit()

    return{
        "message" : "Student deleted successfully"
    }



