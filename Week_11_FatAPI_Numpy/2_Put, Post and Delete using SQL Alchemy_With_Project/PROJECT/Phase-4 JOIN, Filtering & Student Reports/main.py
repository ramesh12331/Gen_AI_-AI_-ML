from fastapi import FastAPI
from database import Base, engine

from models import student, course

from routers import students, courses, marks, reports

app = FastAPI(
    title="Student Management API"
)

# Create database tables

Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(marks.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return{
        "message" : "Student Management API is Working"
    }


