from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.student import Student
from schemas.student import StudentCreate

router = APIRouter(
    prefix = "/students",
    tags = ["Students"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_students(con:Session = Depends(get_db)):
    students = con.query(Student).all()
    return students

@router.get("/{id}")
def get_student(id:int, con:Session = Depends(get_db)):
    student = con.query(Student).filter(Student.student_id == id).first()

    if student is None:
        return{
            "message" : "Student not found"
        }
    return student

@router.post("/")
def create_student(student:StudentCreate, con:Session = Depends(get_db)):
    new_student = Student(
        name = student.name,
        age = student.age,
        email = student.email,
        city = student.city
    )

    con.add(new_student)
    con.commit()
    con.refresh(new_student)

    return new_student

@router.put("/{id}")
def update_student(id:int, student:StudentCreate, con:Session = Depends(get_db)):
    existing_student = con.query(Student).filter(Student.student_id == id).first()

    if existing_student is None:
        return{
            "message" : "Student not found"
        }

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email
    existing_student.city = student.city

    con.commit()
    con.refresh(existing_student)
    return existing_student

@router.delete("/{id}")
def delete_student(id:int, con:Session = Depends(get_db)):
    student = con.query(Student).filter(Student.student_id == id).first()

    if student is None:
        return{
            "message" : "Student not found"
        }
    con.delete(student)
    con.commit()

    return {
        "message" : "Student deleted successfully"
    }
