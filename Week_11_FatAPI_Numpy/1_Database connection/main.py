from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

@app.get("/")
def home():
    return{"message": "FastAPI is working!"}

@app.get("/test-db")
def test_database():
    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT 1")
        )
    return{
        "message": "PostgreSQL connection successful!"
    }

@app.get("/customers")
def get_customers():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM customers3")
        )
        customers = result.mappings().all()
    return customers

@app.get("/customers/{customer_id}")
def get_customer(customer_id:int):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                select * from customers3 where customer_id = :customer_id
            """),
            {"customer_id":customer_id}
        )
        customer = result.mappings().first()
    if customer is None:
        return {"message": "Customer not found"}
    return customer