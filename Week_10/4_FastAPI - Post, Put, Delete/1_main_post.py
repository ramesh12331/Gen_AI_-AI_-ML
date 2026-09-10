from fastapi import FastAPI
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

# ##############################################

# FastAPI nundi FastAPI class ni import chestunnam
from fastapi import FastAPI

# Pydantic nundi BaseModel ni import chestunnam
# Request data validation kosam BaseModel use chestam
from pydantic import BaseModel

# JSON file ni read/write cheyyadaniki json module import chestunnam
import json


# -------------------------
# APP
# -------------------------

# FastAPI application object create chestunnam
# Ee 'app' object meeda manam API routes create chestam
app = FastAPI()


# -------------------------
# MODEL
# -------------------------

# Patient ane Pydantic model create chestunnam
# Client nundi vachina data ee structure lo undali
class Patient(BaseModel):

    # Patient name string ga undali
    name: str

    # Patient city string ga undali
    city: str

    # Patient age integer ga undali
    age: int

    # Patient gender string ga undali
    gender: str

    # Patient height float ga undali
    height: float

    # Patient weight float ga undali
    weight: float


# -------------------------
# HELPER FUNCTIONS
# -------------------------

# patient.json file nundi existing data ni read cheyyadaniki
# load_data() function create chestunnam
def load_data():

    # patient.json file ni read mode ("r") lo open chestunnam
    with open("patient.json", "r") as file:

        # JSON data ni Python object/list ga convert chesi return chestunnam
        return json.load(file)


# Python data ni patient.json file lo save cheyyadaniki
# save_data() function create chestunnam
def save_data(data):

    # patient.json file ni write mode ("w") lo open chestunnam
    with open("patient.json", "w") as file:

        # Python data ni JSON format lo convert chesi file lo save chestunnam
        # indent=4 valla JSON readable format lo untundi
        json.dump(data, file, indent=4)


# -------------------------
# CREATE
# -------------------------

# POST request kosam /patients endpoint create chestunnam
@app.post("/patients")

# create_patient function POST request ni handle chestundi
def create_patient(patient: Patient):

    # patient.json nundi existing patient data ni load chestunnam
    data = load_data()

    # Pydantic patient object ni dictionary ga convert chestunnam
    # Aa dictionary ni existing data list ki add chestunnam
    data.append(patient.model_dump())

    # Updated data ni patient.json file lo save chestunnam
    save_data(data)

    # Client ki response return chestunnam
    return {
        "message": "Patient created successfully",

        # Created patient details ni response lo send chestunnam
        "patient": patient
    }

