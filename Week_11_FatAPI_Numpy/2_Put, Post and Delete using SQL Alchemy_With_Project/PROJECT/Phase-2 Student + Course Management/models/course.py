from sqlalchemy import Column, String, Integer
from database import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String)
    duration = Column(Integer)