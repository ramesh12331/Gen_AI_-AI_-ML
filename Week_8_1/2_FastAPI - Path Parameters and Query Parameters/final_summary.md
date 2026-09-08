# 🎯 FastAPI — Final Summary

Here is the **complete beginner-level revision summary** of the topics you have covered so far, based on your class notes and uploaded material. 

---

## 1. 🚀 FastAPI

**Definition:**

> FastAPI is a modern Python web framework used to build APIs and backend applications quickly.

### Main purpose

```text
FastAPI
   ↓
Build REST APIs
   ↓
GET / POST / PUT / DELETE
   ↓
Receive + return data
   ↓
Backend development
   ↓
Automatic API documentation
```

---

# 2. 🏃 Uvicorn

**Definition:**

> Uvicorn is an ASGI web server used to run FastAPI applications.

### Run command

```bash
python -m uvicorn day1:app --reload
```

Remember:

```text
day1
 ↓
Python file

app
 ↓
FastAPI object

--reload
 ↓
Automatically restart when code changes
```



---

# 3. 🛡️ Pydantic

**Definition:**

> Pydantic is used for data validation and data parsing.

Example:

```python
from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    age: int
    city: str
```

Meaning:

```text
name → string
age  → integer
city → string
```

FastAPI uses Pydantic for request validation. 

---

# 4. 📄 JSON

**Definition:**

> JSON is a lightweight format used to store and exchange data.

Example:

```json
{
    "customer_name": "Ramesh",
    "age": 25,
    "city": "Hyderabad"
}
```

Read JSON:

```python
with open("data.json", "r") as f:
    data = json.load(f)
```

Remember:

```text
json.load()
    ↓
JSON file
    ↓
Python data
```



---

# 5. 🔍 Query Parameters

Query parameters are mainly used for:

```text
Filtering
Searching
Optional conditions
```

Example:

```text
/city?city=Hyderabad
```

Here:

```text
city=Hyderabad
       ↑
Query Parameter
```

FastAPI:

```python
@app.get("/city")
def city_info(city: str):
    ...
```

---

# 6. 🛣️ Path Parameters

Path parameters are mainly used to identify a **specific resource**.

Example:

```text
/customers/C011
```

FastAPI:

```python
@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    ...
```

Remember:

```text
🛣️ PATH
→ Which exact resource?

🔍 QUERY
→ Which filter/condition?
```

---

# 7. 🧩 Important Keywords

### `str`

```python
city: str
```

➡️ Text/string.

### `int`

```python
age: int
```

➡️ Whole number.

### `float`

```python
price: float
```

➡️ Decimal number.

### `None`

```python
Query(None)
```

➡️ Optional/default value.

### `...`

```python
Path(...)
```

➡️ Required parameter.

---

# 8. 🛡️ Query() and Path()

### Query

```python
city: str = Query(None)
```

Means:

```text
🔍 Query parameter
+
Optional
```

### Path

```python
customer_id: str = Path(...)
```

Means:

```text
🛣️ Path parameter
+
Required
```

---

# 9. ⚖️ Query vs Path

| 🔍 Query                         | 🛣️ Path          |
| -------------------------------- | ----------------- |
| Filtering                        | Identifying       |
| Searching                        | Specific resource |
| Usually optional                 | Usually required  |
| `/products?category=Electronics` | `/products/101`   |
| `Query()`                        | `Path()`          |

### ⭐ Golden Rule

```text
/products/101
      ↓
🛣️ PATH
"Give me product 101"


/products?category=Electronics
          ↓
🔍 QUERY
"Filter products by category"
```

---

# 10. 🔄 Basic API Data Flow

Your retail API follows this pattern:

```text
👤 Client
   ↓
🌐 API Request
   ↓
🚀 FastAPI
   ↓
📂 JSON Data
   ↓
🔄 Loop
   ↓
🔎 Condition
   ↓
📋 Result
   ↓
📤 Response
```

For example:

```python
for customer in customers:

    if customer["city"] == city:
        result.append(customer)

return result
```

---

# 11. 🛒 Retail Business APIs

Your notes contain these important endpoints: 

```text
GET /customers
        ↓
👥 All customers


GET /products
        ↓
🛍️ All products


GET /cities
        ↓
🌆 All cities


GET /city?city=Hyderabad
        ↓
🏙️ Customers by city


GET /category?category=Electronics
        ↓
🏷️ Customers by category


GET /major?age=25
        ↓
🎂 Customers age >= 25


GET /products/price?price=50000
        ↓
💰 Products below price


GET /sales/total
        ↓
🧮 Total sales
```

---

# 12. 🚦 HTTP Status Codes

```text
1xx → ℹ️ Information
2xx → ✅ Success
3xx → 🔄 Redirection
4xx → ❌ Client Error
5xx → 💥 Server Error
```

### ⭐ Most important

```text
200 → ✅ OK
201 → ✅ Created
204 → ✅ No Content

400 → ❌ Bad Request
401 → 🔐 Unauthorized
403 → 🚫 Forbidden
404 → 🔎 Not Found
409 → ⚔️ Conflict
422 → 🛡️ Validation Error

500 → 💥 Internal Server Error
502 → 🔌 Bad Gateway
503 → 🚧 Service Unavailable
504 → ⏱️ Gateway Timeout
```

---

# 13. 🧠 Status Code Memory Trick

```text
GET successful
     ↓
   200


POST created
     ↓
   201


DELETE successful + no body
     ↓
   204


Resource doesn't exist
     ↓
   404


Input validation failed
     ↓
   422


Unexpected server problem
     ↓
   500
```

---

# 14. 🎯 Most Important Beginner Concepts

If you remember only these, you have a good foundation:

```text
🚀 FastAPI
→ Build API

🏃 Uvicorn
→ Run API

🛡️ Pydantic
→ Validate data

📄 JSON
→ Store/exchange data

@app.get()
→ Create GET endpoint

🔍 Query
→ Filter/search

🛣️ Path
→ Identify resource

Query(None)
→ Optional

Path(...)
→ Required

str
→ Text

int
→ Whole number

float
→ Decimal

json.load()
→ Read JSON

for
→ Loop through data

if
→ Check condition

append()
→ Add matching data

return
→ Send response

404
→ Not found

422
→ Validation error
```

---

# 🏆 Final Interview Answer

If an interviewer asks:

### **"Explain what you have learned in FastAPI."**

You can answer:

> **FastAPI is a Python web framework used to build REST APIs. I learned how to create GET endpoints using `@app.get()`, run the application using Uvicorn, read data from JSON files, and use query and path parameters. Query parameters are mainly used for filtering and searching, while path parameters are used to identify specific resources. I also learned basic validation concepts using Pydantic, `Query()` and `Path()`, and HTTP status codes such as 200, 201, 204, 404, 422 and 500.**

### 🎯 One-line memory:

```text
🚀 FastAPI → Build
🏃 Uvicorn → Run
🛡️ Pydantic → Validate
📄 JSON → Store/Exchange
🔍 Query → Filter
🛣️ Path → Identify
🚦 Status Code → Tell what happened
```

This is the **core foundation** you should be comfortable with before moving into **FastAPI CRUD operations**.
