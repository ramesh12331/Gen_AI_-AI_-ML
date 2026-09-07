# 📘 Pydantic — `Annotated`

Since you're learning Pydantic chapter-wise, let's understand **`Annotated` from the basics**.

## 🔹 What is `Annotated`?

`Annotated` allows us to write:

> **A data type + additional information/rules**

Think of it like:

```text
Annotated
   ↓
Type + Extra Rules
```

For example:

```python
from typing import Annotated
from pydantic import BaseModel, Field


class Customer(BaseModel):

    name: Annotated[
        str,
        Field(max_length=20)
    ]
```

Here:

```python
name: Annotated[
    str,
    Field(max_length=20)
]
```

means:

* `str` → `name` must be a string
* `Field(max_length=20)` → name can have maximum 20 characters

---

# 🔹 Why do we use `Annotated`?

Without `Annotated`:

```python
name: str = Field(max_length=20)
```

With `Annotated`:

```python
name: Annotated[
    str,
    Field(max_length=20)
]
```

Both can apply the validation rule.

`Annotated` is especially useful when you want to keep the **type and its metadata/validation information together**.

---

# 🔹 Your Example

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Annotated


class Customer(BaseModel):

    name: Annotated[
        str,
        Field(
            max_length=12,
            title="name of the customer",
            description="heyy give me your name"
        )
    ]

    email: EmailStr

    linkedin_url: AnyUrl
```

Let's understand it piece by piece.

### `name`

```python
name: Annotated[
    str,
    Field(
        max_length=12,
        title="name of the customer",
        description="heyy give me your name"
    )
]
```

### Breakdown:

```text
name
 ↓
Annotated
 ↓
str
 ↓
Field()
 ↓
max_length = 12
title = name of the customer
description = heyy give me your name
```

So:

**`Annotated` = combine a type with additional metadata/rules.**

---

# 🔹 What is `Field()` doing here?

```python
Field(
    max_length=12,
    title="name of the customer",
    description="heyy give me your name"
)
```

| Parameter       | Meaning               |
| --------------- | --------------------- |
| `max_length=12` | Maximum 12 characters |
| `title=`        | Field title           |
| `description=`  | Field description     |

For example:

```python
customer = Customer(
    name="Ramesh",
    email="ramesh@gmail.com",
    linkedin_url="https://linkedin.com"
)
```

`Ramesh` has 6 characters, so it is valid.

But:

```python
name="abcdefghijklmnop"
```

has more than 12 characters, so Pydantic raises a validation error.

---

# 🧠 Easy Memory Trick

Remember:

```text
Annotated = TYPE + EXTRA INFORMATION
```

Example:

```python
Annotated[
    str,
    Field(max_length=12)
]
```

Read it as:

> **"This is a string, and here are some extra rules for it."**

---

# ⭐ `Annotated` vs `Field`

```python
# Normal style
name: str = Field(max_length=12)
```

```python
# Annotated style
name: Annotated[
    str,
    Field(max_length=12)
]
```

Both are useful.

### Remember:

> **`Field()` = gives extra rules**

> **`Annotated` = attaches those extra rules to the type**

---

## 🎯 Final Summary

```text
Annotated
   ↓
Type + Metadata/Rules
   ↓
Field()
   ↓
Validation / Documentation
```

The most important syntax to remember:

```python
from typing import Annotated
from pydantic import BaseModel, Field

class Customer(BaseModel):

    name: Annotated[
        str,
        Field(max_length=12)
    ]
```

**One-line interview answer:**

> `Annotated` is a Python typing feature used to attach additional metadata or constraints to a type, and in Pydantic it is commonly used with `Field()` for validation and schema information.

