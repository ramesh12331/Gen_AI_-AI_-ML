from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRegister
from security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user:UserRegister, con:Session = Depends(get_db)):
    existing_user = con.query(User).filter(User.username == user.username).first()

    if existing_user:
        return {
            "message": "Username already exists"
        }

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        username = user.username,
        email = user.email,
        password = hashed_password,
        role = "student"
    )
    con.add(new_user)
    con.commit()

    con.refresh(new_user)

    return{
        "message": "User registered successfully",
        "user_id": new_user.user_id,
        "username": new_user.username
    }
