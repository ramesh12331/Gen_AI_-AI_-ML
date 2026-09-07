Yes 👍 You want **very basic FastAPI CRUD**, without `Annotated`, `Optional`, `Literal`, validators, etc.

Let's keep it simple and use your **Patient** model with a JSON file.

### `day5.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()


# -------------------------
# Model
# -------------------------

class Patient(BaseModel):
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float


# -------------------------
# Helper Functions
# -------------------------

def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)


def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)


# -------------------------
# CREATE
# -------------------------

@app.post("/patients")
def create_patient(patient: Patient):

    data = load_data()

    data.append(patient.model_dump())

    save_data(data)

    return {
        "message": "Patient created successfully",
        "patient": patient
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
def get_patient(name: str):

    data = load_data()

    for patient in data:

        if patient["name"] == name:
            return patient

    raise HTTPException(
        status_code=404,
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

            return {
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
def delete_patient(name: str):

    data = load_data()

    for patient in data:

        if patient["name"] == name:

            data.remove(patient)

            save_data(data)

            return {
                "message": "Patient deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
```

### `patients.json`

```json
[
    {
        "name": "Ramesh",
        "city": "Hyderabad",
        "age": 25,
        "gender": "male",
        "height": 170.5,
        "weight": 65.0
    },
    {
        "name": "Sita",
        "city": "Vijayawada",
        "age": 30,
        "gender": "female",
        "height": 160.0,
        "weight": 55.0
    }
]
```

## CRUD in simple form

### 1. CREATE

```text
POST /patients
```

Body:

```json
{
    "name": "Anil",
    "city": "Bangalore",
    "age": 28,
    "gender": "male",
    "height": 175.5,
    "weight": 70.0
}
```

### 2. READ ALL

```text
GET /patients
```

### 3. READ ONE

```text
GET /patients/Ramesh
```

### 4. UPDATE

```text
PUT /patients/Ramesh
```

Body:

```json
{
    "name": "Ramesh",
    "city": "Chennai",
    "age": 26,
    "gender": "male",
    "height": 171.0,
    "weight": 68.0
}
```

### 5. DELETE

```text
DELETE /patients/Ramesh
```

### Run

```bash
uvicorn day5:app --reload
```

Then:

```text
http://127.0.0.1:8000/docs
```

This is the **basic CRUD version** I recommend learning first. Once this is clear, we can add `PatientUpdate` for **partial updates**.
