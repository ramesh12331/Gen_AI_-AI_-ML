Absolutely 👍 Since you're a **beginner**, let's forget the 500 error for a moment and build this project **from zero, step by step**.

We'll create a simple FastAPI project where:

```text
Client
  ↓
Send customer data
  ↓
FastAPI
  ↓
Pydantic validates data
  ↓
Calculate total_price
  ↓
Save customer into data.json
```

---

# Step 1 — Create the project

Create a folder:

```text
FastAPI_Project
```

Inside it create **two files**:

```text
FastAPI_Project
│
├── main.py
└── data.json
```

---

# Step 2 — Create `data.json`

Open `data.json`.

Put **only this** inside:

```json
[]
```

### What does `[]` mean?

It means:

> We currently have an empty list of customers.

Later, when we add customers, it will look like:

```json
[
    {
        "customer_id": "C101",
        "customer_name": "RAMESH"
    }
]
```

---

# Step 3 — Install FastAPI

Open the VS Code terminal:

```text
Terminal → New Terminal
```

Run:

```bash
pip install fastapi uvicorn
```

---

# Step 4 — First create a very simple FastAPI

Before Pydantic, let's understand FastAPI itself.

Put this in `main.py`:

```python
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()


# Home API
@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI"
    }
```

Run:

```bash
uvicorn main:app --reload
```

You should see something like:

```text
Uvicorn running on http://127.0.0.1:8000
```

Open:

```text
http://127.0.0.1:8000
```

You should get:

```json
{
    "message": "Welcome to FastAPI"
}
```

---

# Step 5 — Open Swagger

FastAPI automatically gives us Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

You will see your API:

```text
GET /
```

This is where we will **send data** later.

---

# Step 6 — Create our Pydantic model

Now change `main.py` to:

```python
from fastapi import FastAPI
from pydantic import BaseModel


# Create FastAPI application
app = FastAPI()


# Create Pydantic model
class Customer(BaseModel):

    customer_id: str

    customer_name: str

    age: int

    city: str

    product: str

    category: str

    quantity: int

    price: int


# Home API
@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI"
    }
```

Now we have created the **structure of our customer**.

Think of this as a form:

```text
Customer
│
├── customer_id
├── customer_name
├── age
├── city
├── product
├── category
├── quantity
└── price
```

---

# Step 7 — Create POST API

Now add this below the `/` API:

```python
@app.post("/create")
def create_customer(cust: Customer):

    return cust
```

So your complete code is:

```python
from fastapi import FastAPI
from pydantic import BaseModel


# Create FastAPI application
app = FastAPI()


# ============================================================
# PYDANTIC MODEL
# ============================================================

class Customer(BaseModel):

    customer_id: str

    customer_name: str

    age: int

    city: str

    product: str

    category: str

    quantity: int

    price: int


# ============================================================
# HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI"
    }


# ============================================================
# CREATE CUSTOMER
# ============================================================

@app.post("/create")
def create_customer(cust: Customer):

    return cust
```

---

# Step 8 — Send data using Swagger

Go to:

```text
http://127.0.0.1:8000/docs
```

You will see:

```text
POST /create
```

Click:

```text
POST /create
```

Then click:

```text
Try it out
```

Swagger will show a JSON box.

Put this:

```json
{
    "customer_id": "C101",
    "customer_name": "Ramesh",
    "age": 25,
    "city": "Hyderabad",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "price": 50000
}
```

Click:

```text
Execute
```

You should get:

```json
{
    "customer_id": "C101",
    "customer_name": "Ramesh",
    "age": 25,
    "city": "Hyderabad",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "price": 50000
}
```

🎉 **You just sent data to FastAPI.**

---

# Step 9 — Add `total_price`

Now we want:

```text
quantity × price
```

For example:

```text
2 × 50000 = 100000
```

Import `computed_field`:

```python
from pydantic import BaseModel, computed_field
```

Then modify the model:

```python
class Customer(BaseModel):

    customer_id: str
    customer_name: str
    age: int
    city: str
    product: str
    category: str
    quantity: int
    price: int

    @computed_field
    @property
    def total_price(self) -> int:

        return self.quantity * self.price
```

Now:

```python
@app.post("/create")
def create_customer(cust: Customer):

    return cust
```

will return something like:

```json
{
    "customer_id": "C101",
    "customer_name": "Ramesh",
    "age": 25,
    "city": "Hyderabad",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "price": 50000,
    "total_price": 100000
}
```

Notice:

**You don't send `total_price`.**

FastAPI/Pydantic calculates it:

```text
quantity
    ↓
    2
    ×
price
    ↓
50000
    ↓
total_price
    ↓
100000
```

---

# Step 10 — Add name transformation

Now we want:

```text
ramesh
   ↓
RAMESH
```

Import `field_validator`:

```python
from pydantic import (
    BaseModel,
    computed_field,
    field_validator
)
```

Add:

```python
@field_validator("customer_name")
@classmethod
def name_transform(cls, value):

    return value.upper()
```

Your model becomes:

```python
class Customer(BaseModel):

    customer_id: str

    customer_name: str

    age: int

    city: str

    product: str

    category: str

    quantity: int

    price: int


    # Convert customer name to uppercase
    @field_validator("customer_name")
    @classmethod
    def name_transform(cls, value):

        return value.upper()


    # Calculate total price
    @computed_field
    @property
    def total_price(self) -> int:

        return self.quantity * self.price
```

Now send:

```json
{
    "customer_id": "C101",
    "customer_name": "ramesh",
    "age": 25,
    "city": "Hyderabad",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "price": 50000
}
```

Result:

```json
{
    "customer_id": "C101",
    "customer_name": "RAMESH",
    "age": 25,
    "city": "Hyderabad",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "price": 50000,
    "total_price": 100000
}
```

---

# Step 11 — Now create `load_data()`

Now we want to **save the customer into `data.json`**.

Import JSON:

```python
import json
```

Create:

```python
def load_data():

    with open("data.json", "r") as file:

        data = json.load(file)

    return data
```

### What is happening?

```text
data.json
    ↓
open()
    ↓
json.load()
    ↓
Python list
```

For example:

```json
[]
```

becomes:

```python
[]
```

---

# Step 12 — Create `save_data()`

Now create:

```python
def save_data(data):

    with open("data.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )
```

This does the opposite:

```text
Python list
    ↓
json.dump()
    ↓
data.json
```

---

# Step 13 — Finally save the customer

Now change:

```python
@app.post("/create")
def create_customer(cust: Customer):

    return cust
```

to:

```python
@app.post("/create")
def create_customer(cust: Customer):

    # Load existing customers
    data = load_data()

    # Add new customer
    data.append(cust.model_dump())

    # Save updated data
    save_data(data)

    # Return success message
    return {
        "message": "Customer created successfully"
    }
```

---

# Step 14 — FINAL CODE

Now your complete beginner project is:

```python
# ============================================================
# IMPORTS
# ============================================================

from fastapi import FastAPI
from pydantic import (
    BaseModel,
    computed_field,
    field_validator
)

import json


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI()


# ============================================================
# PYDANTIC MODEL
# ============================================================

class Customer(BaseModel):

    # Customer ID
    customer_id: str

    # Customer name
    customer_name: str

    # Customer age
    age: int

    # Customer city
    city: str

    # Product name
    product: str

    # Product category
    category: str

    # Quantity purchased
    quantity: int

    # Price of one product
    price: int


    # --------------------------------------------------------
    # FIELD VALIDATOR
    # --------------------------------------------------------

    # Convert customer name to uppercase
    #
    # "ramesh"
    #     ↓
    # "RAMESH"

    @field_validator("customer_name")
    @classmethod
    def name_transform(cls, value):

        return value.upper()


    # --------------------------------------------------------
    # COMPUTED FIELD
    # --------------------------------------------------------

    # Calculate total price
    #
    # quantity × price

    @computed_field
    @property
    def total_price(self) -> int:

        return self.quantity * self.price


# ============================================================
# LOAD DATA FROM JSON
# ============================================================

def load_data():

    # Open data.json in read mode
    with open("data.json", "r") as file:

        # Convert JSON into Python object
        data = json.load(file)

    return data


# ============================================================
# SAVE DATA INTO JSON
# ============================================================

def save_data(data):

    # Open data.json in write mode
    with open("data.json", "w") as file:

        # Convert Python object into JSON
        json.dump(
            data,
            file,
            indent=4
        )


# ============================================================
# HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI"
    }


# ============================================================
# CREATE CUSTOMER API
# ============================================================

@app.post("/create")
def create_customer(cust: Customer):

    # --------------------------------------------------------
    # STEP 1
    # Load existing customer data
    # --------------------------------------------------------

    data = load_data()


    # --------------------------------------------------------
    # STEP 2
    # Add new customer
    # --------------------------------------------------------

    # Convert Pydantic object into dictionary
    data.append(
        cust.model_dump()
    )


    # --------------------------------------------------------
    # STEP 3
    # Save updated data
    # --------------------------------------------------------

    save_data(data)


    # --------------------------------------------------------
    # STEP 4
    # Return success response
    # --------------------------------------------------------

    return {
        "message": "Customer created successfully"
    }
```

---

# Step 15 — `data.json`

Before sending data, make sure:

```json
[]
```

Then use Swagger:

```text
http://127.0.0.1:8000/docs
```

Send:

```json
{
    "customer_id": "C101",
    "customer_name": "ramesh",
    "age": 25,
    "city": "Hyderabad",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "price": 50000
}
```

Click **Execute**.

You get:

```json
{
    "message": "Customer created successfully"
}
```

Now open `data.json`.

You should see:

```json
[
    {
        "customer_id": "C101",
        "customer_name": "RAMESH",
        "age": 25,
        "city": "Hyderabad",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 2,
        "price": 50000,
        "total_price": 100000
    }
]
```

---

# 🧠 Understand the whole project

This is the most important part:

```text
                  YOU
                   │
                   │ JSON data
                   ↓
          ┌─────────────────┐
          │     FastAPI     │
          │   POST /create  │
          └────────┬────────┘
                   │
                   ↓
          ┌─────────────────┐
          │    Pydantic     │
          │    Customer     │
          └────────┬────────┘
                   │
             Validate data
                   │
                   ↓
        ┌──────────────────────┐
        │  Field Validator     │
        │  ramesh → RAMESH     │
        └──────────┬───────────┘
                   │
                   ↓
        ┌──────────────────────┐
        │   Computed Field     │
        │  2 × 50000 = 100000  │
        └──────────┬───────────┘
                   │
                   ↓
            model_dump()
                   │
                   ↓
             Python dict
                   │
                   ↓
             data.append()
                   │
                   ↓
            save_data()
                   │
                   ↓
              data.json
```

### Remember these 7 things

```text
1. main.py
   → FastAPI code

2. data.json
   → Stores our customer data

3. BaseModel
   → Defines customer structure

4. @field_validator
   → Changes/validates input

5. @computed_field
   → Calculates values

6. load_data()
   → Reads data.json

7. save_data()
   → Writes data.json
```

**Don't jump to duplicate checking, `HTTPException`, `PUT`, `DELETE`, or `model_validator` yet.** First get this simple **POST → Pydantic → calculate → save to JSON** flow working. Then the next step will be much easier to understand.
