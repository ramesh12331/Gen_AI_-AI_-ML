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


# ##################################################################################
# ============================================================
# IMPORTS
# ============================================================

# FastAPI -> used to create our API
# HTTPException -> used to send error responses like 404
from fastapi import FastAPI, HTTPException

# BaseModel -> used to create Pydantic models
# Pydantic checks whether the incoming data has the correct type
from pydantic import BaseModel

# json -> used to read and write data in JSON format
import json


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

# Create a FastAPI application
# 'app' is the main object of our API
app = FastAPI()


# ============================================================
# PYDANTIC MODEL
# ============================================================

# Patient is a Pydantic model
#
# This model defines what data a patient should have.
#
# Example:
# {
#     "name": "Ramesh",
#     "city": "Hyderabad",
#     "age": 25,
#     "gender": "Male",
#     "height": 5.8,
#     "weight": 70.5
# }

class Patient(BaseModel):

    # Patient name must be a string
    name: str

    # Patient city must be a string
    city: str

    # Patient age must be an integer
    age: int

    # Patient gender must be a string
    gender: str

    # Patient height must be a float
    height: float

    # Patient weight must be a float
    weight: float


# ============================================================
# HELPER FUNCTION - LOAD DATA
# ============================================================

def load_data():

    # Open patient.json file in read mode
    #
    # "r" means READ
    #
    # with open() automatically closes the file
    # after we finish using it.
    with open("patient.json", "r") as file:

        # json.load(file)
        #
        # Reads the JSON data from the file
        # and converts it into Python data.
        #
        # JSON list  -> Python list
        # JSON object -> Python dictionary
        return json.load(file)


# ============================================================
# HELPER FUNCTION - SAVE DATA
# ============================================================

def save_data(data):

    # Open patient.json file in write mode
    #
    # "w" means WRITE
    #
    # If the file already contains data,
    # write mode replaces the old content.
    with open("patient.json", "w") as file:

        # Convert Python data into JSON
        # and save it inside patient.json
        #
        # indent=4 makes the JSON file
        # easy for humans to read.
        json.dump(data, file, indent=4)


# ============================================================
# CREATE - POST
# ============================================================

# @app.post("/patients")
#
# This creates a POST API endpoint.
#
# POST is normally used to CREATE new data.
#
# URL:
# http://127.0.0.1:8000/patients
#
@app.post("/patients")
def create_patient(patient: Patient):

    # Load existing patient data from patient.json
    data = load_data()

    # patient.model_dump()
    #
    # Converts the Pydantic Patient object
    # into a normal Python dictionary.
    #
    # Example:
    #
    # Patient object
    #       ↓
    # Dictionary
    #
    # {
    #     "name": "Ramesh",
    #     "city": "Hyderabad",
    #     "age": 25,
    #     ...
    # }
    #
    # data.append()
    # adds the new patient to the existing list.
    data.append(patient.model_dump())

    # Save the updated list back into patient.json
    save_data(data)

    # Send response back to the user
    return {
        "message": "Patient created successfully",

        # Return the patient that was created
        "patient": patient
    }


# ============================================================
# READ ALL - GET
# ============================================================

# @app.get("/patients")
#
# GET is normally used to READ data.
#
# This endpoint returns ALL patients.
#
# URL:
# http://127.0.0.1:8000/patients
#
@app.get("/patients")
def get_patients():

    # Read all patient data from JSON file
    data = load_data()

    # Return the complete patient list
    return data


# ============================================================
# READ ONE - GET
# ============================================================

# @app.get("/patients/{name}")
#
# {name} is a path parameter.
#
# Example:
#
# /patients/Ramesh
#
# Here:
# name = "Ramesh"
#
@app.get("/patients/{name}")
def get_patient(name: str):

    # Load all patients from JSON
    data = load_data()

    # Go through each patient one by one
    #
    # patient represents one dictionary
    # from the data list.
    for patient in data:

        # Check whether the patient's name
        # matches the name given in the URL.
        #
        # Example:
        #
        # URL name = "Ramesh"
        #
        # patient["name"] = "Ramesh"
        #
        # Both are equal -> return patient
        if patient["name"] == name:

            # Return the matching patient
            return patient

    # If the for loop finishes and
    # no patient was found,
    # return HTTP 404 error.
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# ============================================================
# UPDATE - PUT
# ============================================================

# PUT is normally used to UPDATE existing data.
#
# URL:
# /patients/{name}
#
# Example:
#
# /patients/Ramesh
#
# We will search for Ramesh
# and replace his old information.
#
@app.put("/patients/{name}")
def update_patient(name: str, updated_patient: Patient):

    # Load existing patient data
    data = load_data()

    # Go through every patient
    for patient in data:

        # Find the patient using the name
        if patient["name"] == name:

            # Replace old name with new name
            patient["name"] = updated_patient.name

            # Replace old city with new city
            patient["city"] = updated_patient.city

            # Replace old age with new age
            patient["age"] = updated_patient.age

            # Replace old gender with new gender
            patient["gender"] = updated_patient.gender

            # Replace old height with new height
            patient["height"] = updated_patient.height

            # Replace old weight with new weight
            patient["weight"] = updated_patient.weight

            # Save the updated data to patient.json
            save_data(data)

            # Return success response
            return {
                "message": "Patient updated successfully",

                # Return the updated patient
                "patient": patient
            }

    # If patient was not found
    # return 404 error.
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# ============================================================
# DELETE - DELETE
# ============================================================

# DELETE is normally used to DELETE data.
#
# URL:
#
# /patients/{name}
#
# Example:
#
# /patients/Ramesh
#
# This will search for Ramesh
# and remove him from the JSON file.
#
@app.delete("/patients/{name}")
def delete_patient(name: str):

    # Load existing patient data
    data = load_data()

    # Go through every patient
    for patient in data:

        # Check whether the patient name
        # matches the name from the URL.
        if patient["name"] == name:

            # Remove that patient from the list
            data.remove(patient)

            # Save the updated list to JSON
            save_data(data)

            # Return success message
            return {
                "message": "Patient deleted successfully"
            }

    # If patient was not found
    # return 404 error.
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )