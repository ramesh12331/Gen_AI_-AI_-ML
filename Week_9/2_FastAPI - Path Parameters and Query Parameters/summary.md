I’ll continue from the uploaded FastAPI notes. The next section is **Student Practice Questions → Final Summary → Interview Q&A**, and I’ll keep it beginner-friendly. 

# 🧑‍💻 8. Student Practice Questions

## 🟢 Level 1 — Basic

### Q1️⃣ Get all products

Create:

```text
GET /products
```

Expected:

```python
@app.get("/products")
def get_products():
    return products
```

---

### Q2️⃣ Get product by ID

Create:

```text
GET /products/101
```

Use a **Path Parameter**:

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    ...
```

Why Path?

Because `101` identifies **one specific product**. 

---

### Q3️⃣ Filter by city

Create:

```text
GET /products?city=Hyderabad
```

Use a **Query Parameter**:

```python
@app.get("/products")
def get_products(city: str | None = None):
    ...
```

---

### Q4️⃣ Filter by category

```text
GET /products?category=Electronics
```

Again, use a **Query Parameter**.

---

### Q5️⃣ Minimum price

```text
GET /products?min_price=5000
```

Requirement:

> Return products whose price is **at least ₹5,000**.

Condition:

```python
product["price"] >= min_price
```

These are the first five practice problems in the uploaded notes. 

---

# 🟡 Level 2 — Intermediate Beginner

### Q6️⃣ Multiple Query Parameters

```text
/products?city=Hyderabad&category=Fashion
```

You need:

```python
city
category
```

Both conditions should be satisfied.

```python
if product["city"] == city and product["category"] == category:
```

---

### Q7️⃣ Price Range

```text
/products?min_price=2000&max_price=10000
```

Condition:

```python
product["price"] >= min_price and product["price"] <= max_price
```

---

### Q8️⃣ Query Validation

Make sure:

```text
price >= 1
```

Example:

```python
price: float = Query(..., ge=1)
```

Here:

```text
ge = greater than or equal to
```

So:

```text
price = 100  ✅
price = 1    ✅
price = 0    ❌
```

---

### Q9️⃣ Product Not Found

If product doesn't exist:

```text
404
```

Use:

```python
raise HTTPException(
    status_code=404,
    detail="Product not found"
)
```

---

### Q🔟 DELETE Product

Create:

```text
DELETE /products/{product_id}
```

If deletion succeeds:

```text
204 No Content
```

These Level 2 exercises are directly listed in the notes. 

---

# 🔴 Level 3 — Think Like an Interviewer

These are more important because they test **understanding**, not memorization.

### Q11️⃣ Why is city a Query Parameter?

Answer:

> Because city is normally used as a **filter condition**.

Example:

```text
/products?city=Hyderabad
```

We are asking:

> "Which products match this condition?"

---

### Q12️⃣ Why is product ID a Path Parameter?

Answer:

> Because product ID identifies a **specific resource**.

Example:

```text
/products/101
```

We are asking:

> "Give me exactly product 101."

---

### Q13️⃣ Difference between these?

```text
/products/101
```

and:

```text
/products?id=101
```

Beginner rule:

```text
/products/101
      ↑
   PATH
```

means:

> Specific product.

While:

```text
/products?id=101
         ↑
       QUERY
```

is a query condition/filter.

The notes specifically use this comparison as an interview question. 

---

# 🧠 Q14️⃣ What happens with `age=abc`?

Suppose:

```python
@app.get("/customers")
def get_customers(age: int):
    return {"age": age}
```

But client sends:

```text
/customers?age=abc
```

FastAPI expects:

```text
int
```

but receives:

```text
abc
```

Therefore validation fails and commonly produces:

```text
422 Unprocessable Entity
```



---

# 🧠 Q15️⃣ 404 vs 422

This is **very important**.

### 404

Resource doesn't exist.

```text
/products/999
```

Product 999 doesn't exist:

```text
404 Not Found
```

### 422

Input is invalid.

```text
/products?product_id=abc
```

If `product_id` should be an integer:

```text
422 Validation Error
```

Easy memory:

```text
🔎 404 → I cannot find it.

🛡️ 422 → Your input is invalid.
```



---

# 📘 9. Final Summary

## 🔍 Query Parameters

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

Basic syntax:

```python
@app.get("/products")
def get_products(category: str | None = None):
    ...
```



---

## 🛣️ Path Parameters

Used mainly to identify a **specific resource**.

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

# ⚖️ Golden Rule

This is the **most important thing to remember**:

```text
🛣️ PATH
   ↓
"Which exact resource?"

GET /products/101
```

versus:

```text
🔍 QUERY
   ↓
"What conditions/filter?"

GET /products?category=Electronics
```



### 🧠 Memory Trick

> **PATH = WHO / WHICH ONE?**
> **QUERY = FILTER / SEARCH / CONDITIONS** 

---

# 🚦 HTTP Status Codes — Must Know

|        Code | Meaning               | Remember               |
| ----------: | --------------------- | ---------------------- |
|  🟢 **200** | OK                    | GET successful         |
|  🟢 **201** | Created               | POST created           |
|  🟢 **204** | No Content            | DELETE successful      |
|  🔴 **400** | Bad Request           | Invalid request        |
|  🔐 **401** | Unauthorized          | Authentication         |
|  🚫 **403** | Forbidden             | No permission          |
|  🔎 **404** | Not Found             | Resource doesn't exist |
|  ⚔️ **409** | Conflict              | Duplicate/conflict     |
| 🛡️ **422** | Validation Error      | Invalid input          |
|  💥 **500** | Internal Server Error | Server problem         |



---

# 🎯 FastAPI Request Flow

Understand this flow instead of memorizing individual pieces:

```text
              🌐 CLIENT
                  │
                  ▼
             🛣️ URL / Request
                  │
          ┌───────┴───────┐
          ▼               ▼
      🛣️ PATH          🔍 QUERY
      /101             ?city=Hyd
          │               │
          └───────┬───────┘
                  ▼
              ⚙️ FastAPI
                  │
                  ▼
             🛡️ Validation
                  │
                  ▼
             🔎 Find / Filter
                  │
                  ▼
              📤 Response
                  │
                  ▼
             🚦 Status Code
```

This is the mental model provided in your notes. 

---

# 🎤 Beginner Interview Q&A

### 1. What is an API parameter?

> An API parameter is a value sent by the client to provide information to the API. Common FastAPI parameters include query and path parameters. 

### 2. What is a Query Parameter?

> A value passed in the URL after `?`, commonly used for filtering and searching.

```text
/products?category=Electronics
```

### 3. What is a Path Parameter?

> A value included directly in the URL path, commonly used to identify a specific resource.

```text
/products/101
```



### 4. What is `Query()`?

> `Query()` is used to configure and validate query parameters.

```python
age: int = Query(..., ge=18, le=60)
```

This means age must be between **18 and 60**. 

### 5. What does `Query(None)` mean?

> The query parameter is optional and its default value is `None`.

```python
city: str | None = Query(None)
```



### 6. What is `Path()`?

> `Path()` is used to configure and validate path parameters.

```python
product_id: int = Path(..., ge=1)
```



---

# 🏆 Your 7 Most Important Codes

Don't try to memorize every HTTP status code right now.

Start with these:

```text
200 → 👀 GET → Successfully returned

201 → ➕ POST → Created

204 → 🗑️ DELETE → Success, no body

400 → ❌ Bad Request

404 → 🔎 Not Found

422 → 🛡️ Validation Failed

500 → 💥 Server Problem
```



---

# ⭐ Your Current Learning Order

You have now covered:

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
```

The next natural step in your notes is:

```text
🔟 CRUD + Error Handling
        ↓
FastAPI
   +
Pydantic
   +
JSON / Database
   +
HTTPException
   +
Status Codes
```



### 🧠 Final one-line memory

```text
🛣️ PATH = Specific resource
🔍 QUERY = Filter/search
🛡️ Query()/Path() = Validation/configuration
🚦 Status code = What happened?
```

That completes this **FastAPI Parameters + HTTP Status Codes** section from your notes.
