# 🚦 Part 2 — HTTP Status Codes in FastAPI

Now let's continue from your **Query Parameters → Path Parameters** notes.

The next topic is **HTTP Status Codes**. I'll keep this at **beginner level first**. 

---

# 1. 📖 What is an HTTP Status Code?

Whenever a client sends a request to an API, the server sends back a **response**.

Along with the response, the server sends a **status code**.

It tells us:

> "What happened to your request?"

Example:

```text
GET /products
       ↓
    FastAPI
       ↓
   200 OK
```

So:

```text
200
```

is the HTTP status code.

---

# 2. 🧩 Five Main Categories

HTTP status codes are divided into five groups:

```text
1xx → ℹ️ Informational
2xx → ✅ Success
3xx → 🔄 Redirection
4xx → ❌ Client Error
5xx → 💥 Server Error
```

### 🧠 Easy memory trick

```text
1 → Information
2 → Success
3 → Redirection
4 → Client mistake
5 → Server mistake
```

For your current FastAPI learning, focus mainly on:

```text
200
201
204
400
401
403
404
409
422
500
```

---

# 3. ℹ️ 1xx — Informational

These indicate that the request is being processed or that additional information is involved.

For a FastAPI beginner:

> You don't need to worry much about 1xx codes right now.

Just remember:

```text
1xx → ℹ️ Information
```

---

# 4. ✅ 2xx — Success

These mean:

> The request was successfully processed.

The three most useful ones for you are:

```text
200 → OK
201 → Created
204 → No Content
```

---

# 5. 🟢 200 — OK

## 📖 Meaning

`200 OK` means:

> The request was successful.

The most common example is a successful GET request.

### FastAPI

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def get_products():

    return {
        "message": "Products returned successfully"
    }
```

When you call:

```text
GET /products
```

FastAPI normally returns:

```text
200 OK
```

Response:

```json
{
    "message": "Products returned successfully"
}
```

---

# 6. 🟢 201 — Created

## 📖 Meaning

`201 Created` means:

> A new resource was successfully created.

This is commonly used with:

```text
POST
```

For example:

```text
POST /products
```

### FastAPI

```python
from fastapi import FastAPI, status

app = FastAPI()


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED
)
def create_product():

    return {
        "message": "Product created"
    }
```

Now the response status is:

```text
201 Created
```

### 🧠 Remember

```text
GET  → 200
POST → 201
```

This is a useful beginner interview rule.

---

# 7. 🟢 204 — No Content

## 📖 Meaning

`204 No Content` means:

> The request was successful, but there is no response body.

A common example is DELETE.

```text
DELETE /products/101
```

### FastAPI

```python
from fastapi import FastAPI

app = FastAPI()


@app.delete(
    "/products/{product_id}",
    status_code=204
)
def delete_product(product_id: int):

    # delete product here

    return
```

Successful deletion:

```text
204 No Content
```

There is no JSON response body.

### 🧠 Remember

```text
DELETE → 204
```

when you intentionally return no content.

---

# 8. ❌ 4xx — Client Errors

Now we move to:

```text
4xx → Client Error
```

This generally means:

> There is a problem with the request from the client.

Important codes:

```text
400
401
403
404
409
422
```

---

# 9. 🔴 400 — Bad Request

## 📖 Meaning

The server cannot properly process the request because the request itself is invalid.

Think:

> ❌ "Your request is bad."

Example business scenario:

```text
A client sends an invalid request format or invalid business input
that the API treats as a bad request.
```

For your beginner level, remember:

```text
400 → Bad Request
```

---

# 10. 🔐 401 — Unauthorized

## 📖 Meaning

The client has not provided valid authentication credentials.

Think:

> 🔐 "Who are you?"

Example:

```text
User tries to access a protected API
without valid authentication.
```

Remember:

```text
401 → Authentication problem
```

---

# 11. 🚫 403 — Forbidden

## 📖 Meaning

The user is authenticated, but does not have permission to perform the requested action.

Think:

> 🚫 "I know who you are, but you aren't allowed."

Example:

```text
Normal employee
       ↓
tries to delete an admin account
       ↓
403 Forbidden
```

### Easy difference

```text
401 → Who are you?
403 → I know you, but you're not allowed.
```

---

# 12. 🔎 404 — Not Found

This is **very important for your FastAPI CRUD practice**.

## 📖 Meaning

The requested resource does not exist.

Suppose our products are:

```python
products = [
    {"product_id": 101, "name": "Laptop"},
    {"product_id": 102, "name": "Mobile"}
]
```

User requests:

```text
GET /products/999
```

But:

```text
999 ❌
```

doesn't exist.

So return:

```text
404 Not Found
```

### FastAPI

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

products = [
    {"product_id": 101, "name": "Laptop"},
    {"product_id": 102, "name": "Mobile"}
]


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

Request:

```text
GET /products/101
```

Response:

```text
200 OK
```

Request:

```text
GET /products/999
```

Response:

```text
404 Not Found
```

---

# 13. ⚔️ 409 — Conflict

## 📖 Meaning

`409 Conflict` means:

> The request conflicts with the current state of the resource.

A common beginner business example:

```text
Product ID 101 already exists.
```

Client tries to create another product using ID 101.

You could return:

```text
409 Conflict
```

Think:

```text
Existing data
      +
New request
      ↓
   Conflict
```

---

# 14. 🛡️ 422 — Validation Error

This is **especially important in FastAPI**.

Suppose:

```python
@app.get("/products")
def get_products(age: int):
    return {
        "age": age
    }
```

The API expects:

```text
age → integer
```

But the client sends:

```text
/products?age=abc
```

FastAPI's validation system sees:

```text
"abc"
  ↓
int ❌
```

So the request fails validation and FastAPI commonly returns:

```text
422
```

### 🧠 Remember

```text
422 → Validation problem
```

---

# 15. 💥 5xx — Server Errors

Now:

```text
5xx → Server Error
```

This means the problem is on the server side or with a service the server depends on.

Important codes:

```text
500
502
503
504
```

---

# 16. 💥 500 — Internal Server Error

## 📖 Meaning

Something unexpected went wrong on the server.

Example:

```text
Python programming error
Database failure
Unexpected exception
```

Think:

> 💥 "The server had a problem."

Remember:

```text
500 → Internal Server Error
```

---

# 17. 🔌 502 — Bad Gateway

A server acting as a gateway/proxy received an invalid response from another server.

Simple example:

```text
Your API
   ↓
Payment Service
   ↓
Invalid response
   ↓
502
```

For now, just remember:

```text
502 → Bad Gateway
```

---

# 18. 🚧 503 — Service Unavailable

Means:

> The service is temporarily unavailable.

Example:

```text
API server under maintenance
```

or:

```text
Dependent service unavailable
```

Remember:

```text
503 → Service Unavailable
```

---

# 19. ⏱️ 504 — Gateway Timeout

Means:

> A gateway/proxy waited too long for another server to respond.

Simple example:

```text
API
 ↓
Payment Server
 ↓
waiting...
 ↓
timeout
 ↓
504
```

Remember:

```text
504 → Gateway Timeout
```

---

# 📊 Complete Status Code Table

|    Code | Meaning               | Simple meaning              |
| ------: | --------------------- | --------------------------- |
|  ℹ️ 100 | Continue              | Informational               |
|   ✅ 200 | OK                    | Request successful          |
|   ✅ 201 | Created               | Resource created            |
|   ✅ 204 | No Content            | Successful, no body         |
|   ❌ 400 | Bad Request           | Invalid request             |
|  🔐 401 | Unauthorized          | Authentication problem      |
|  🚫 403 | Forbidden             | No permission               |
|  🔎 404 | Not Found             | Resource doesn't exist      |
|  ⚔️ 409 | Conflict              | Request conflicts with data |
| 🛡️ 422 | Unprocessable Content | Validation failed           |
|  💥 500 | Internal Server Error | Server problem              |
|  🔌 502 | Bad Gateway           | Upstream response problem   |
|  🚧 503 | Service Unavailable   | Service unavailable         |
|  ⏱️ 504 | Gateway Timeout       | Upstream timeout            |

---

# 🎯 20. Most Important Codes for You

Don't try to memorize everything at once.

Start with these:

```text
             ⭐ BEGINNER FASTAPI

GET successful
      ↓
   200 OK


POST successful
      ↓
  201 Created


DELETE successful
      ↓
  204 No Content


Resource doesn't exist
      ↓
  404 Not Found


Input validation failed
      ↓
  422


Unexpected server problem
      ↓
  500
```

---

# 🧑‍💻 21. Mini FastAPI Example

Let's combine what you've learned so far:

```python
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

products = [
    {
        "product_id": 101,
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000
    },
    {
        "product_id": 102,
        "name": "Mobile",
        "category": "Electronics",
        "price": 25000
    }
]


# 🔍 Query Parameter
@app.get("/products")
def get_products(
    category: str | None = Query(None)
):

    if category is None:
        return products

    result = []

    for product in products:

        if product["category"] == category:
            result.append(product)

    return result


# 🛣️ Path Parameter
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

# 🌐 22. Try These URLs

### 🟢 All products

```text
http://127.0.0.1:8000/products
```

Expected:

```text
200 OK
```

---

### 🔍 Electronics products

```text
http://127.0.0.1:8000/products?category=Electronics
```

Expected:

```text
200 OK
```

---

### 🛣️ Existing product

```text
http://127.0.0.1:8000/products/101
```

Expected:

```text
200 OK
```

---

### 🔎 Non-existing product

```text
http://127.0.0.1:8000/products/999
```

Expected:

```text
404 Not Found
```

---

# 📚 23. Swagger Practice

Start your application:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

You can test your API interactively.

### Swagger flow

```text
🌐 /docs
   ↓
📋 Select endpoint
   ↓
▶️ Try it out
   ↓
✏️ Enter parameters
   ↓
▶️ Execute
   ↓
📤 See response
   ↓
🚦 See status code
```

---

# 🧠 24. Quick Test — Don't Look at Answers

### Question 1

A GET request successfully returns products.

What status code?

```text
A) 201
B) 404
C) 200
D) 500
```

---

### Question 2

You successfully create a new product.

What status code?

```text
A) 200
B) 201
C) 404
D) 422
```

---

### Question 3

You request product ID `999`, but it doesn't exist.

```text
A) 200
B) 201
C) 404
D) 500
```

---

### Question 4

API expects:

```python
age: int
```

Client sends:

```text
age=abc
```

Which status code commonly occurs in FastAPI validation?

```text
A) 200
B) 201
C) 404
D) 422
```

---

### Question 5

An unexpected error occurs inside your server.

```text
A) 400
B) 404
C) 422
D) 500
```

---

# 🎤 25. Beginner Interview Questions

### Q1. What is an HTTP status code?

**Answer:**

> An HTTP status code is a number returned by the server that tells the client what happened to its request.

---

### Q2. What does 200 mean?

**Answer:**

> `200 OK` means the request was successfully processed.

---

### Q3. What does 201 mean?

**Answer:**

> `201 Created` means a new resource was successfully created.

---

### Q4. What does 204 mean?

**Answer:**

> `204 No Content` means the request was successful but the server returns no response body.

---

### Q5. What does 404 mean?

**Answer:**

> `404 Not Found` means the requested resource does not exist.

---

### Q6. What does 422 mean in FastAPI?

**Answer:**

> `422` commonly indicates that the request data failed FastAPI's validation.

---

### Q7. Difference between 401 and 403?

**Answer:**

> `401` means valid authentication is missing or invalid. `403` means the client is authenticated but does not have permission to perform the operation.

Easy memory:

```text
401 → 🔐 Who are you?
403 → 🚫 You're not allowed.
```

---

### Q8. Difference between 404 and 422?

**Answer:**

> `404` means the requested resource was not found. `422` means the submitted data failed validation.

Example:

```text
/products/999
      ↓
404
```

because the product doesn't exist.

But:

```text
/products?age=abc
             ↓
            422
```

because an integer was expected.

---

### Q9. What does 500 mean?

**Answer:**

> `500 Internal Server Error` means an unexpected problem occurred on the server.

---

# 🏆 Final Memory Map

```text
                 🚦 HTTP STATUS CODES
                         │
        ┌────────────────┼────────────────┐
        │                │                │
       1xx              2xx              4xx/5xx
        │                │                │
   ℹ️ Information      ✅ Success       ❌ Errors
                         │
               ┌─────────┼─────────┐
               │         │         │
              200       201       204
               │         │         │
              GET       POST     DELETE
```

And:

```text
4xx → 👤 Client/request problem

400 → Bad Request
401 → Authentication
403 → Permission
404 → Resource not found
409 → Conflict
422 → Validation


5xx → 🖥️ Server problem

500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
504 → Gateway Timeout
```

### ⭐ Your most important beginner combination

```text
🔍 Query Parameter
       +
🛣️ Path Parameter
       +
🛡️ Validation
       +
🚦 Status Code
       ↓
      API
```

**Next topic: 💼 Business Scenarios + 🛒 Retail Dataset implementation**, where we'll take these concepts and build realistic FastAPI questions such as **filter products by city/category/price, get product by ID, handle 404, and decide the correct status code**.
