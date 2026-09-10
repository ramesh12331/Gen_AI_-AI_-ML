# 📘 Pydantic — Chapter: `field_validator()`

Now let's continue from where we stopped. We'll learn **`field_validator()` very slowly**, because this is an important Pydantic concept. Your uploaded notes use Pydantic v2's `field_validator`. 

---

## 1️⃣ What is `field_validator()`?

`field_validator()` is used when **Pydantic's normal validation is not enough** and we want to create our **own/custom validation rule**.

### Simple meaning:

> **`field_validator()` = write your own rule for a field.**

Think:

```text
User Input
    ↓
Pydantic
    ↓
Normal Validation
    ↓
Custom field_validator()
    ↓
Valid / Error
```

---

# 2️⃣ Basic Syntax

```python
from pydantic import BaseModel, field_validator


class Customer(BaseModel):

    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        # custom validation

        return value
```

Let's understand each line.

### `@field_validator("email")`

```python
@field_validator("email")
```

Means:

> "Run this validator whenever the `email` field is validated."

---

### `@classmethod`

```python
@classmethod
```

This allows the validator method to receive the class as `cls`.

For your current Pydantic v2 style, keep this pattern:

```python
@field_validator("email")
@classmethod
def validate_email(cls, value):
```

---

### `value`

```python
def validate_email(cls, value):
```

`value` contains the **current value of the field**.

For example:

```text
email = "anwar@hdfc.com"

        ↓

value = "anwar@hdfc.com"
```

---

# 3️⃣ Simple Example

Let's say our company only accepts:

```text
hdfc.com
icici.com
```

We can create our own validation rule.

```python
from pydantic import BaseModel, field_validator


class Customer(BaseModel):

    email: str

    @field_validator("email")
    @classmethod
    def email_valid(cls, value):

        valid_domains = [
            "hdfc.com",
            "icici.com"
        ]

        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise ValueError("Invalid email domain")

        return value
```

---

# 4️⃣ Dry Run 🧠

Suppose:

```python
customer = Customer(
    email="anwar@hdfc.com"
)
```

The process is:

```text
"anwar@hdfc.com"
        ↓
field_validator("email")
        ↓
value
        ↓
"anwar@hdfc.com"
        ↓
split("@")
        ↓
["anwar", "hdfc.com"]
        ↓
[-1]
        ↓
"hdfc.com"
        ↓
Is it in valid_domains?
        ↓
YES ✅
        ↓
return value
```

Customer is accepted.

---

# 5️⃣ What happens with Gmail?

```python
customer = Customer(
    email="anwar@gmail.com"
)
```

Process:

```text
anwar@gmail.com
       ↓
gmail.com
       ↓
valid_domains?
       ↓
NO ❌
       ↓
raise ValueError()
       ↓
Validation Error
```

So our custom rule rejects the email.

---

# 6️⃣ Why `return value`?

This is very important.

```python
return value
```

means:

> "The value passed validation, so give it back to Pydantic."

Example:

```python
@field_validator("email")
@classmethod
def email_valid(cls, value):

    if "@" not in value:
        raise ValueError("Invalid email")

    return value
```

### Flow:

```text
Valid
 ↓
return value
 ↓
Pydantic accepts it
```

If invalid:

```text
Invalid
 ↓
raise ValueError
 ↓
Pydantic rejects it
```

---

# 7️⃣ `raise ValueError()` 🔴

This:

```python
raise ValueError("Invalid email domain")
```

means:

> "Stop! The data doesn't satisfy my rule."

Example:

```python
if domain not in valid_domains:
    raise ValueError("Invalid email domain")
```

---

# 8️⃣ `field_validator()` Can Also Transform Data

Your notes also show validators being used to **transform** values. 

For example, converting a name to uppercase:

```python
@field_validator("name")
@classmethod
def transform_name(cls, value):

    return value.upper()
```

Input:

```python
name = "anwar"
```

After validation:

```text
anwar
  ↓
upper()
  ↓
ANWAR
```

So:

```python
customer.name
```

becomes:

```text
ANWAR
```

---

# 9️⃣ Age Transformation

Your notes also demonstrate transforming the age:

```python
@field_validator("age", mode="after")
@classmethod
def transform_age(cls, value):

    return value + 10
```

Suppose:

```python
age = 35
```

Then:

```text
35
 ↓
transform_age()
 ↓
35 + 10
 ↓
45
```

So the final value becomes:

```text
45
```

### ⚠️ Important

The `Field()` constraints still apply.

If you have:

```python
age: Annotated[
    int,
    Field(
        gt=20,
        lt=60
    )
]
```

then an input such as:

```python
age = 75
```

fails the `Field()` validation because `75` is not less than `60`. Your uploaded notes specifically highlight this issue. 

For learning the transformation, use:

```python
age = 35
```

---

# 🔟 Complete Example

```python
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated


class Customer(BaseModel):

    name: Annotated[
        str,
        Field(max_length=10)
    ]

    email: EmailStr

    age: Annotated[
        int,
        Field(
            gt=20,
            lt=60
        )
    ]

    @field_validator("email")
    @classmethod
    def email_valid(cls, value):

        valid_domains = [
            "hdfc.com",
            "icici.com"
        ]

        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise ValueError(
                "Email must belong to HDFC or ICICI domain"
            )

        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):

        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def transform_age(cls, value):

        return value + 10


data = {
    "name": "anwar",
    "email": "anwar@hdfc.com",
    "age": 35
}


customer = Customer(**data)

print(customer.name)
print(customer.email)
print(customer.age)
```

### Output

```text
ANWAR
anwar@hdfc.com
45
```

---

# 🧠 Remember These 4 Things

```text
@field_validator("field")
        ↓
Which field?

@classmethod
        ↓
Validator method

value
        ↓
Current field value

return value
        ↓
Accept / return processed value
```

And:

```text
raise ValueError()
        ↓
Reject the value ❌
```

---

# 🎯 Interview Question

### Q: What is `field_validator()` in Pydantic?

**Answer:**

> `field_validator()` is used in Pydantic v2 to define custom validation or transformation logic for a specific model field.

### Q: Why do we use it?

> We use it when built-in Pydantic validation is not sufficient and we need our own business rule.

### Q: What is `value`?

> `value` is the current value of the field being validated.

---

# ⭐ Final Summary

```text
field_validator()
       ↓
Custom validation
       ↓
Can validate
       ↓
Can transform
       ↓
return value → Accept ✅
raise ValueError → Reject ❌
```

### Super-easy memory trick:

> **`Field()` = standard rules**
> **`field_validator()` = my own rules**

Next in your uploaded notes is **Nested Pydantic Models (`Address` inside `Customer`)**. 
