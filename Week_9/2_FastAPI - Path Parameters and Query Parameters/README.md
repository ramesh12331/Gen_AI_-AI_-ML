Absolutely. Below is a **beginner-friendly README-style study note** covering your complete FastAPI topic in the same order, with **definitions → syntax → examples → FastAPI code → URLs → business scenarios → retail implementation → practice → final summary → interview Q&A**.

# 📘 FastAPI Parameters & HTTP Status Codes — Beginner README

> 🎯 **Goal:** Understand how FastAPI receives information from URLs, validates it, finds data, and returns the correct HTTP status code.

---

# 🗂️ Table of Contents

1. 🔹 API Parameters
2. 🔍 Query Parameters
3. 🛣️ Path Parameters
4. ⚖️ Query vs Path Parameters
5. 🚦 HTTP Status Codes
6. 💼 Business Scenarios
7. 🛒 Retail Dataset Implementation
8. 🧑‍💻 Student Practice Questions
9. 🧠 Final Summary
10. 🎤 Beginner Interview Questions & Answers

---

# 1. 🔹 API Parameters

## 📖 Definition

**API parameters** are values that we send to an API to tell it **what data we want** or **which specific operation we want to perform**.

For example:

```text
GET /customers/101
```

Here:

```text
101
```

is a parameter.

It tells the API:

> "Give me customer 101."

---

## 🔑 Main types

In FastAPI, beginners mainly work with:

```text
1. Query Parameters
2. Path Parameters
```

### 🔍 Query Parameter

Used mainly for:

* Filtering
* Searching
* Sorting
* Optional conditions

Example:

```text
/customers?city=Hyderabad
```

### 🛣️ Path Parameter

Used mainly for:

* Identifying one specific resource

Example:

```text
/customers/101
```

---

# 2. 🔍 Query Parameters

## 📖 Definition

A **query parameter** is a value passed in the URL after `?`.

Example:

```text
/customers?city=Hyderabad
```

Here:

```text
city = Hyderabad
```

is a query parameter.

---

## 🧩 URL Structure

```text
http://127.0.0.1:8000/customers?city=Hyderabad
```

Breakdown:

```text
http://127.0.0.1:8000
          ↓
       Server

/customers
     ↓
   Endpoint

?
 ↓
Query starts

city=Hyderabad
     ↓
Query parameter
```

---

# 🟢 Simple Query Parameter Example

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/customers")
def get_customers(city: str):
    return {
        "city": city
    }
```

### 🌐 URL

```text
http://127.0.0.1:8000/customers?city=Hyderabad
```

### 📤 Response

```json
{
    "city": "Hyderabad"
}
```

---

# ⭐ Important Point

Notice that we did **not** write:

```python
@app.get("/customers/{city}")
```

We wrote:

```python
@app.get("/customers")
def get_customers(city: str):
```

FastAPI understands that `city` is a **query parameter**.

---

# 🔹 Optional Query Parameters

Sometimes the user may or may not provide a parameter.

For example:

```text
/customers
```

should work.

And:

```text
/customers?city=Hyderabad
```

should also work.

We can use:

```python
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/customers")
def get_customers(city: Optional[str] = None):
    return {
        "city": city
    }
```

### Without parameter

```text
GET /customers
```

Response:

```json
{
    "city": null
}
```

### With parameter

```text
GET /customers?city=Hyderabad
```

Response:

```json
{
    "city": "Hyderabad"
}
```

---

# 🔗 Multiple Query Parameters

We can send multiple query parameters.

Example:

```text
/customers?city=Hyderabad&age=25
```

Here:

```text
city = Hyderabad
age = 25
```

---

## 🧑‍💻 FastAPI Example

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/customers")
def get_customers(city: str, age: int):
    return {
        "city": city,
        "age": age
    }
```

### 🌐 URL

```text
http://127.0.0.1:8000/customers?city=Hyderabad&age=25
```

### 📤 Response

```json
{
    "city": "Hyderabad",
    "age": 25
}
```

---

# 🟡 `Query(None)`

FastAPI provides `Query()` for query parameter configuration and validation.

```python
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/customers")
def get_customers(city: str | None = Query(None)):
    return {
        "city": city
    }
```

### Meaning

```python
Query(None)
```

means:

> The query parameter is optional and its default value is `None`.

---

# 🛡️ Validation using `Query()`

Suppose age should be between 18 and 60.

```python
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/customers")
def get_customers(
    age: int = Query(..., ge=18, le=60)
):
    return {
        "age": age
    }
```

### Meaning

```text
ge = greater than or equal to
le = less than or equal to
```

Therefore:

```text
18 ✅
25 ✅
60 ✅

17 ❌
61 ❌
```

---

# 🔎 Filtering Data Using Query Parameters

Suppose we have:

```python
customers = [
    {
        "id": 1,
        "name": "Ravi",
        "city": "Hyderabad",
        "age": 25
    },
    {
        "id": 2,
        "name": "Anil",
        "city": "Chennai",
        "age": 30
    },
    {
        "id": 3,
        "name": "Sita",
        "city": "Hyderabad",
        "age": 22
    }
]
```

We can filter by city.

```python
@app.get("/customers")
def get_customers(city: str | None = None):

    if city is None:
        return customers

    result = []

    for customer in customers:
        if customer["city"] == city:
            result.append(customer)

    return result
```

### 🌐 URL

```text
/customers?city=Hyderabad
```

### 📤 Result

```json
[
    {
        "id": 1,
        "name": "Ravi",
        "city": "Hyderabad",
        "age": 25
    },
    {
        "id": 3,
        "name": "Sita",
        "city": "Hyderabad",
        "age": 22
    }
]
```

---

# 3. 🛣️ Path Parameters

## 📖 Definition

A **path parameter** is a value included directly inside the URL path.

Example:

```text
/customers/101
```

Here:

```text
101
```

is the path parameter.

---

# 🧑‍💻 Basic Syntax

```python
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {
        "customer_id": customer_id
    }
```

### 🌐 URL

```text
http://127.0.0.1:8000/customers/101
```

### 📤 Response

```json
{
    "customer_id": 101
}
```

---

# 🔎 Finding One Customer

```python
from fastapi import FastAPI

app = FastAPI()

customers = [
    {"id": 101, "name": "Ravi", "city": "Hyderabad"},
    {"id": 102, "name": "Anil", "city": "Chennai"},
    {"id": 103, "name": "Sita", "city": "Bangalore"}
]


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    return {
        "message": "Customer not found"
    }
```

### 🌐 Request

```text
GET /customers/102
```

### 📤 Response

```json
{
    "id": 102,
    "name": "Anil",
    "city": "Chennai"
}
```

---

# 🛡️ Path Validation using `Path()`

We can validate path parameters.

```python
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/customers/{customer_id}")
def get_customer(
    customer_id: int = Path(..., ge=1)
):
    return {
        "customer_id": customer_id
    }
```

Here:

```python
ge=1
```

means:

```text
customer_id >= 1
```

Therefore:

```text
/customers/101   ✅
/customers/1     ✅
/customers/0     ❌
/customers/-5    ❌
```

---

# ⚖️ 4. Query vs Path Parameters

This is **very important for interviews**.

| Feature      | Query Parameter 🔍          | Path Parameter 🛣️              |
| ------------ | --------------------------- | ------------------------------- |
| Example      | `/customers?city=Hyderabad` | `/customers/101`                |
| Main purpose | Filtering/searching         | Identifying resource            |
| Usually      | Optional                    | Required                        |
| Location     | After `?`                   | Inside URL path                 |
| Multiple     | Easy                        | Usually one resource identifier |
| Example      | `?age=25`                   | `/customers/101`                |

---

## 🧠 Easy Rule

Think:

> 🔍 **Query = "Which conditions?"**

> 🛣️ **Path = "Which exact resource?"**

### Example

```text
/customers/101
```

Means:

> Give me customer 101.

But:

```text
/customers?city=Hyderabad
```

Means:

> Give me customers from Hyderabad.

---

# 🚦 5. HTTP Status Codes

HTTP status codes tell the client **what happened with the request**.

There are five major groups:

```text
1xx → ℹ️ Informational
2xx → ✅ Success
3xx → 🔄 Redirection
4xx → ❌ Client Error
5xx → 💥 Server Error
```

---

# ℹ️ 1xx — Informational

These indicate that the request is being processed or more information is expected.

For beginner FastAPI development, you don't normally need to manually work with 1xx responses.

---

# ✅ 2xx — Success

## 200 — OK

Used when the request was successfully completed.

Example:

```text
GET /customers
```

```python
@app.get("/customers")
def get_customers():
    return customers
```

Typically returns:

```text
200 OK
```

---

## 201 — Created

Used when a new resource is successfully created.

For example:

```text
POST /customers
```

In FastAPI:

```python
from fastapi import FastAPI, status

app = FastAPI()


@app.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer():
    return {
        "message": "Customer created"
    }
```

Response status:

```text
201 Created
```

---

## 204 — No Content

Used when the request succeeds but there is no response body.

Common example:

```text
DELETE /customers/101
```

```python
@app.delete(
    "/customers/{customer_id}",
    status_code=204
)
def delete_customer(customer_id: int):
    # delete customer
    return
```

---

# ❌ 4xx — Client Errors

These generally mean there is something wrong with the client's request.

---

## 400 — Bad Request

The request is invalid.

Example:

```text
The API expects valid data, but the client sends an invalid request.
```

---

## 🔐 401 — Unauthorized

Authentication is missing or invalid.

Think:

> "Who are you?"

Example:

```text
User tries to access an API without valid authentication.
```

---

## 🚫 403 — Forbidden

The user is authenticated but does not have permission.

Think:

> "I know who you are, but you are not allowed."

---

## 🔎 404 — Not Found

The requested resource does not exist.

Example:

```text
GET /customers/999
```

If customer 999 doesn't exist:

```text
404 Not Found
```

FastAPI:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    if customer_id != 101:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "id": 101,
        "name": "Ravi"
    }
```

---

# ⚔️ 409 — Conflict

Used when the request conflicts with existing data.

Example:

```text
POST /customers
```

Trying to create another customer with an ID that already exists.

```text
409 Conflict
```

---

# 🛡️ 422 — Validation Error

This is particularly important in FastAPI.

Suppose:

```python
@app.get("/customers")
def get_customers(age: int):
    return {"age": age}
```

User sends:

```text
/customers?age=abc
```

But:

```python
age: int
```

expects an integer.

FastAPI's validation system rejects the input and commonly returns:

```text
422
```

---

# 💥 5xx — Server Errors

These indicate that something went wrong on the server side.

---

## 500 — Internal Server Error

Unexpected server-side error.

Example:

```text
Database failure
Programming error
Unexpected exception
```

---

## 502 — Bad Gateway

A server acting as a gateway/proxy received an invalid response from an upstream service.

---

## 503 — Service Unavailable

The service is temporarily unavailable.

Example:

```text
Server overloaded
Maintenance
Dependent service unavailable
```

---

## 504 — Gateway Timeout

A gateway/proxy did not receive a response from an upstream service in time.

---

# 🧠 HTTP Status Code Cheat Sheet

| Code    | Meaning               | Beginner Example           |
| ------- | --------------------- | -------------------------- |
| ℹ️ 100  | Continue              | Informational              |
| ✅ 200   | OK                    | GET successful             |
| ✅ 201   | Created               | POST successful            |
| ✅ 204   | No Content            | DELETE successful          |
| ❌ 400   | Bad Request           | Invalid request            |
| 🔐 401  | Unauthorized          | Authentication required    |
| 🚫 403  | Forbidden             | No permission              |
| 🔎 404  | Not Found             | Customer doesn't exist     |
| ⚔️ 409  | Conflict              | Duplicate/conflicting data |
| 🛡️ 422 | Validation Error      | Invalid input type/value   |
| 💥 500  | Internal Server Error | Unexpected server error    |
| 🔌 502  | Bad Gateway           | Upstream response problem  |
| 🚧 503  | Service Unavailable   | Service unavailable        |
| ⏱️ 504  | Gateway Timeout       | Upstream timeout           |

---

# 6. 💼 Business Scenarios

Let's understand these concepts using real business situations.

## 🏪 Scenario 1 — Find customers by city

```text
GET /customers?city=Hyderabad
```

Use:

```text
🔍 Query Parameter
```

Why?

Because `city` is a **filter**.

---

## 🏪 Scenario 2 — Find customer by ID

```text
GET /customers/101
```

Use:

```text
🛣️ Path Parameter
```

Why?

Because `101` identifies one specific customer.

---

## 🏪 Scenario 3 — Find products by category

```text
GET /products?category=Electronics
```

Use:

```text
🔍 Query Parameter
```

---

## 🏪 Scenario 4 — Find products by price

```text
GET /products?price=500
```

Or:

```text
GET /products?min_price=500&max_price=2000
```

Use:

```text
🔍 Query Parameters
```

---

## 🏪 Scenario 5 — Delete customer

```text
DELETE /customers/101
```

Use:

```text
🛣️ Path Parameter
```

because we are identifying the customer to delete.

Successful response:

```text
204 No Content
```

---

# 7. 🛒 Retail Dataset Implementation

Let's build a **simple beginner-friendly Retail API**.

## 📊 Sample Dataset

```python
products = [
    {
        "product_id": 101,
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "city": "Hyderabad"
    },
    {
        "product_id": 102,
        "name": "Mobile",
        "category": "Electronics",
        "price": 25000,
        "city": "Chennai"
    },
    {
        "product_id": 103,
        "name": "Shoes",
        "category": "Fashion",
        "price": 2500,
        "city": "Hyderabad"
    },
    {
        "product_id": 104,
        "name": "Watch",
        "category": "Fashion",
        "price": 5000,
        "city": "Bangalore"
    }
]
```

---

# 🧑‍💻 Complete Beginner Code

```python
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()


products = [
    {
        "product_id": 101,
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "city": "Hyderabad"
    },
    {
        "product_id": 102,
        "name": "Mobile",
        "category": "Electronics",
        "price": 25000,
        "city": "Chennai"
    },
    {
        "product_id": 103,
        "name": "Shoes",
        "category": "Fashion",
        "price": 2500,
        "city": "Hyderabad"
    },
    {
        "product_id": 104,
        "name": "Watch",
        "category": "Fashion",
        "price": 5000,
        "city": "Bangalore"
    }
]


# Get all products
@app.get("/products")
def get_products():
    return products


# Filter products
@app.get("/products/filter")
def filter_products(
    city: str | None = Query(None),
    category: str | None = Query(None),
    min_price: float | None = Query(None),
    max_price: float | None = Query(None)
):

    result = products

    if city is not None:
        result = [
            product for product in result
            if product["city"] == city
        ]

    if category is not None:
        result = [
            product for product in result
            if product["category"] == category
        ]

    if min_price is not None:
        result = [
            product for product in result
            if product["price"] >= min_price
        ]

    if max_price is not None:
        result = [
            product for product in result
            if product["price"] <= max_price
        ]

    return result


# Get product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["product_id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
```

---

# 🌐 Swagger URLs

After starting FastAPI:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

This gives you the interactive **Swagger UI**.

---

## 🔍 Get All Products

```text
GET /products
```

---

## 🏙️ Filter by City

```text
GET /products/filter?city=Hyderabad
```

---

## 🏷️ Filter by Category

```text
GET /products/filter?category=Electronics
```

---

## 💰 Filter by Price

```text
GET /products/filter?min_price=3000
```

---

## 🔗 Multiple Filters

```text
GET /products/filter?city=Hyderabad&category=Fashion
```

Or:

```text
GET /products/filter?min_price=2000&max_price=10000
```

Or:

```text
GET /products/filter?city=Hyderabad&category=Fashion&min_price=2000
```

---

## 🛣️ Find Product by ID

```text
GET /products/101
```

Result:

```json
{
    "product_id": 101,
    "name": "Laptop",
    "category": "Electronics",
    "price": 55000,
    "city": "Hyderabad"
}
```

---

# 🧠 One Important Beginner Concept

Suppose you have:

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
```

The URL is:

```text
/products/101
```

But:

```python
@app.get("/products")
def get_products(category: str | None = None):
```

The URL is:

```text
/products?category=Electronics
```

### Remember:

```text
/products/101
       ↑
   Path Parameter


/products?category=Electronics
          ↑
     Query Parameter
```

---

# 8. 🧑‍💻 Student Practice Questions

Try solving these **without looking at the answers first**.

## 🟢 Level 1 — Basic

### Q1

Create an endpoint:

```text
GET /products
```

that returns all products.

---

### Q2

Create an endpoint to find a product using:

```text
/product_id
```

Expected URL:

```text
/products/101
```

---

### Q3

Create a query parameter:

```text
/products?city=Hyderabad
```

to filter products by city.

---

### Q4

Create:

```text
/products?category=Electronics
```

to filter products by category.

---

### Q5

Create:

```text
/products?min_price=5000
```

to return products costing at least ₹5,000.

---

# 🟡 Level 2 — Intermediate Beginner

### Q6

Create multiple query parameters:

```text
/products?city=Hyderabad&category=Fashion
```

---

### Q7

Create:

```text
/products?min_price=2000&max_price=10000
```

---

### Q8

Use `Query()` to make price validation:

```text
price >= 1
```

---

### Q9

If product doesn't exist, return:

```text
404
```

with:

```json
{
    "detail": "Product not found"
}
```

---

### Q10

Create a DELETE endpoint:

```text
DELETE /products/{product_id}
```

and return:

```text
204 No Content
```

when deletion succeeds.

---

# 🔴 Level 3 — Think Like an Interviewer

### Q11

Why should city be a query parameter rather than a path parameter?

---

### Q12

Why should product ID usually be a path parameter?

---

### Q13

What is the difference between:

```text
/products/101
```

and:

```text
/products?id=101
```

---

### Q14

What happens if:

```python
age: int
```

but the user sends:

```text
?age=abc
```

---

### Q15

When would you return `404` instead of `422`?

---

# 🧠 Final Summary

## 🔹 API Parameters

Parameters allow the client to send information to an API.

```text
API Parameters
      │
      ├── 🔍 Query Parameters
      │
      └── 🛣️ Path Parameters
```

---

## 🔍 Query Parameter

Used mainly for:

```text
Filtering
Searching
Optional conditions
```

Example:

```text
/products?category=Electronics
```

Syntax:

```python
@app.get("/products")
def get_products(category: str | None = None):
    ...
```

---

## 🛣️ Path Parameter

Used mainly to identify a specific resource.

Example:

```text
/products/101
```

Syntax:

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    ...
```

---

# ⚖️ Query vs Path — Golden Rule

```text
🛣️ PATH
"Which exact resource?"

Example:
GET /products/101


🔍 QUERY
"What conditions/filter do I want?"

Example:
GET /products?category=Electronics
```

---

# 🚦 HTTP Status Codes

Remember this:

```text
1xx → ℹ️ Information

2xx → ✅ Success

3xx → 🔄 Redirection

4xx → ❌ Client Error

5xx → 💥 Server Error
```

### Most important for your beginner FastAPI level:

```text
200 → GET successful
201 → POST created
204 → DELETE successful / no body

400 → Bad request
401 → Authentication required
403 → Permission denied
404 → Resource not found
409 → Conflict
422 → Validation error

500 → Server error
```

---

# 🎯 FastAPI Beginner Mental Model

When a request comes to your API, think:

```text
                 🌐 Client
                    │
                    ▼
             🛣️ URL / Request
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      🛣️ Path             🔍 Query
      /101             ?city=Hyd
          │                   │
          └─────────┬─────────┘
                    ▼
             ⚙️ FastAPI
                    │
                    ▼
              🛡️ Validation
                    │
                    ▼
              🔎 Find/Filter
                    │
                    ▼
             📤 Response
                    │
                    ▼
             🚦 Status Code
```

---

# 🎤 Beginner FastAPI Interview Questions & Answers

## 1. What is a parameter in an API?

**Answer:**

An API parameter is a value sent by the client to provide information to the API. In FastAPI, common parameters include query parameters and path parameters.

---

## 2. What is a query parameter?

**Answer:**

A query parameter is a parameter passed in the URL after `?`. It is commonly used for filtering and searching.

Example:

```text
/products?category=Electronics
```

---

## 3. What is a path parameter?

**Answer:**

A path parameter is a value included directly in the URL path. It is commonly used to identify a specific resource.

Example:

```text
/products/101
```

---

## 4. What is the difference between query and path parameters?

**Answer:**

A path parameter usually identifies a specific resource, while a query parameter is commonly used for filtering or optional conditions.

Example:

```text
/products/101
```

uses a path parameter.

```text
/products?category=Electronics
```

uses a query parameter.

---

## 5. What is `Query()` in FastAPI?

**Answer:**

`Query()` is used to configure and validate query parameters.

Example:

```python
age: int = Query(..., ge=18, le=60)
```

This requires age to be between 18 and 60.

---

## 6. What does `Query(None)` mean?

**Answer:**

It means the query parameter is optional and its default value is `None`.

Example:

```python
city: str | None = Query(None)
```

---

## 7. What is `Path()`?

**Answer:**

`Path()` is used to configure and validate path parameters.

Example:

```python
product_id: int = Path(..., ge=1)
```

---

## 8. What does HTTP 200 mean?

**Answer:**

`200 OK` means the request was successfully processed.

Common example:

```text
GET request successful
```

---

## 9. What does HTTP 201 mean?

**Answer:**

`201 Created` means a new resource was successfully created.

Common example:

```text
POST /products
```

---

## 10. What does HTTP 204 mean?

**Answer:**

`204 No Content` means the request was successful but the server does not return a response body.

A common example is a successful DELETE operation.

---

## 11. What does HTTP 404 mean?

**Answer:**

`404 Not Found` means the requested resource does not exist.

Example:

```text
GET /products/999
```

when product 999 doesn't exist.

---

## 12. What does HTTP 422 mean?

**Answer:**

`422` indicates that the request data failed validation.

For example:

```python
age: int
```

but the client sends:

```text
age=abc
```

FastAPI's validation system can return a 422 response.

---

## 13. What is HTTP 500?

**Answer:**

`500 Internal Server Error` means an unexpected error occurred on the server.

---

## 14. What is the difference between 404 and 422?

**Answer:**

```text
404 → Requested resource doesn't exist.

422 → Input failed validation.
```

Example:

```text
/products/999
```

where product 999 doesn't exist → **404**

But:

```text
/products?product_id=abc
```

when an integer is expected → **422**

---

## 15. Which status code is normally used after creating a resource?

**Answer:**

```text
201 Created
```

---

## 16. Which status code is commonly used for a successful GET?

**Answer:**

```text
200 OK
```

---

## 17. Which status code is commonly used for successful DELETE with no response body?

**Answer:**

```text
204 No Content
```

---

# ⭐ Interview Memory Trick

Remember these **7 codes first**:

```text
        🚦 FASTAPI STATUS CODES

200 → 👀 GET → "I found/returned it"
201 → ➕ POST → "I created it"
204 → 🗑️ DELETE → "Done, nothing to return"

400 → ❌ Bad request
404 → 🔎 Not found
422 → 🛡️ Validation failed
500 → 💥 Server problem
```

And remember:

```text
🛣️ PATH  → WHO / WHICH ONE?

🔍 QUERY  → FILTER / SEARCH / CONDITIONS
```

### 🎯 Your learning order

For your current beginner stage, I recommend mastering these in this order:

```text
1️⃣ API Parameters
      ↓
2️⃣ Query Parameters
      ↓
3️⃣ Path Parameters
      ↓
4️⃣ Query vs Path
      ↓
5️⃣ Query() and Path()
      ↓
6️⃣ Filtering
      ↓
7️⃣ HTTP Status Codes
      ↓
8️⃣ Business Scenarios
      ↓
9️⃣ Retail API Practice
      ↓
🔟 CRUD + Error Handling
```

Once these are comfortable, the next natural step is **FastAPI CRUD with Pydantic models + JSON file/database + proper `HTTPException` + status codes**.
