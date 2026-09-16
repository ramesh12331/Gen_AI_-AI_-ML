from fastapi import FastAPI
from database import Base, engine

from models import student, course

from routers import students, courses

app = FastAPI(
    title="Student Management API"
)

# Create database tables

Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(students.router)
app.include_router(courses.router)

@app.get("/")
def home():
    return{
        "message" : "Student Management API is Working"
    }


