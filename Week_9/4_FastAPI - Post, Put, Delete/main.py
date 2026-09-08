from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

# -------------------------
# Model
# -------------------------
 
app = FastAPI()

class Patient(BaseModel):
    name : str
    city : str
    age : int
    gender : str
    height : float
    weight : float

# -------------------------
# Helper Functions
# -------------------------

def load_data():
    with open("patient.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("patient.json", "w") as file:
        json.dump(data, file, indent=4)

# -------------------------
# CREATE
# -------------------------

@app.post("/patients")
def create_patient(patient:Patient):
    data = load_data()
    data.append(patient.model_dump())
    save_data(data)

    return{
        "message" : "Patient created successfully",
        "patient" : patient
    }

# -------------------------
# READ ALL
# -------------------------

@app.get("/patients")
def get_patients():
    data = load_data()
    return data

# -------------------------
# READ ONE
# -------------------------
@app.get("/patients/{name}")
def get_patient(name:str):
    data = load_data()

    for patient in data:
        if patient["name"] == name:
            return patient
    raise HTTPException(
        status_code = 404,
        detail="Patient not found"
    )

# -------------------------
# UPDATE
# -------------------------

@app.put("/patients/{name}")
def update_patient(name: str, updated_patient: Patient):
    data = load_data()

    for patient in data:
        if patient["name"] == name:

            patient["name"] = updated_patient.name
            patient["city"] = updated_patient.city
            patient["age"] = updated_patient.age
            patient["gender"] = updated_patient.gender
            patient["height"] = updated_patient.height
            patient["weight"] = updated_patient.weight

            save_data(data)

            return{
                "message": "Patient updated successfully",
                "patient": patient
            }
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )

# -------------------------
# DELETE
# -------------------------

@app.delete("/patients/{name}")
def delete_patient(name:str):
    data = load_data()

    for patient in data:
        if patient["name"] == name:
            data.remove(patient)
            save_data(data)

            return{
                "message": "Patient deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
        )