from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, Literal
import json


app = FastAPI()


# ============================================================
# MODELS
# ============================================================

class Patient(BaseModel):

    id: int = Field(gt=0)
    name: str = Field(min_length=2, max_length=50)
    city: str
    age: int = Field(gt=0, le=120)
    gender: Literal["male", "female"]
    height: float = Field(gt=0)
    weight: float = Field(gt=0)


class PatientUpdate(BaseModel):

    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=0, le=120)
    gender: Optional[Literal["male", "female"]] = None
    height: Optional[float] = Field(default=None, gt=0)
    weight: Optional[float] = Field(default=None, gt=0)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_data():

    with open("patients.json", "r") as file:
        return json.load(file)


def save_data(data):

    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)


def find_patient(patient_id):

    data = load_data()

    for patient in data:

        if patient["id"] == patient_id:
            return patient

    return None


# ============================================================
# CREATE
# ============================================================

@app.post("/patients")
def create_patient(patient: Patient):

    data = load_data()

    # Check duplicate ID

    for existing_patient in data:

        if existing_patient["id"] == patient.id:

            raise HTTPException(
                status_code=400,
                detail="Patient ID already exists"
            )

    data.append(patient.model_dump())

    save_data(data)

    return {
        "message": "Patient created successfully",
        "data": patient
    }


# ============================================================
# READ ALL
# ============================================================

@app.get("/patients")
def get_all_patients():

    data = load_data()

    return {
        "count": len(data),
        "data": data
    }


# ============================================================
# READ ONE
# ============================================================

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):

    patient = find_patient(patient_id)

    if patient is None:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# ============================================================
# PUT - FULL UPDATE
# ============================================================

@app.put("/patients/{patient_id}")
def update_patient(
    patient_id: int,
    updated_patient: Patient
):

    data = load_data()

    for index, patient in enumerate(data):

        if patient["id"] == patient_id:

            # Make sure ID cannot change

            updated_data = updated_patient.model_dump()

            updated_data["id"] = patient_id

            data[index] = updated_data

            save_data(data)

            return {
                "message": "Patient updated successfully",
                "data": updated_data
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# ============================================================
# PATCH - PARTIAL UPDATE
# ============================================================

@app.patch("/patients/{patient_id}")
def partial_update_patient(
    patient_id: int,
    patient_update: PatientUpdate
):

    data = load_data()

    for patient in data:

        if patient["id"] == patient_id:

            update_data = patient_update.model_dump(
                exclude_unset=True
            )

            patient.update(update_data)

            save_data(data)

            return {
                "message": "Patient partially updated",
                "data": patient
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# ============================================================
# DELETE
# ============================================================

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):

    data = load_data()

    for index, patient in enumerate(data):

        if patient["id"] == patient_id:

            deleted_patient = data.pop(index)

            save_data(data)

            return {
                "message": "Patient deleted successfully",
                "data": deleted_patient
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# ============================================================
# SEARCH
# ============================================================

@app.get("/search")
def search_patients(
    city: Optional[str] = None,
    gender: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None
):

    data = load_data()

    result = data

    if city:

        result = [
            patient
            for patient in result
            if patient["city"].lower() == city.lower()
        ]

    if gender:

        result = [
            patient
            for patient in result
            if patient["gender"].lower() == gender.lower()
        ]

    if min_age is not None:

        result = [
            patient
            for patient in result
            if patient["age"] >= min_age
        ]

    if max_age is not None:

        result = [
            patient
            for patient in result
            if patient["age"] <= max_age
        ]

    return {
        "count": len(result),
        "data": result
    }


# ============================================================
# PAGINATION
# ============================================================

@app.get("/patients-page")
def get_patients_page(
    page: int = Query(default=1, gt=0),
    limit: int = Query(default=5, gt=0, le=100)
):

    data = load_data()

    start = (page - 1) * limit

    end = start + limit

    result = data[start:end]

    return {
        "page": page,
        "limit": limit,
        "count": len(result),
        "data": result
    }