from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Integer)