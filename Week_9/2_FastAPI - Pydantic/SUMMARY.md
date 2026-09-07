## Pydantic — Final Summary

| Topic                       | Meaning                                            | Simple Memory Trick    | Example                                |
| --------------------------- | -------------------------------------------------- | ---------------------- | -------------------------------------- |
| **BaseModel**               | Creates a Pydantic model                           | Model creator          | `class Customer(BaseModel):`           |
| **EmailStr**                | Validates email format                             | Email checker          | `email: EmailStr`                      |
| **AnyUrl**                  | Validates URL                                      | URL checker            | `linkedin_url: AnyUrl`                 |
| **Field()**                 | Adds extra validation rules                        | Extra rules            | `Field(gt=20, lt=60)`                  |
| **Annotated**               | Combines a type with extra information/rules       | Type + Rules           | `Annotated[str, Field(max_length=10)]` |
| **List**                    | Stores multiple values of a specified type         | Many values            | `products: List[str]`                  |
| **Dict**                    | Defines key and value types                        | Key + Value            | `Dict[str, str]`                       |
| **Optional**                | Field can contain a value or `None`                | Value or None          | `Optional[str] = None`                 |
| **field_validator()**       | Creates custom validation/transformation           | My own rule            | `@field_validator("email")`            |
| **@classmethod**            | Creates a class method                             | `cls` → class          | `def method(cls, value):`              |
| **Email Validator**         | Checks allowed email domains                       | Domain checker         | `if domain not in valid_domains:`      |
| **Name Validator**          | Changes name format                                | Transform name         | `return value.upper()`                 |
| **Age Validator**           | Changes age after validation                       | Transform value        | `return value + 10`                    |
| **Nested Model**            | Uses one Pydantic model inside another             | Model inside model     | `address: Address`                     |
| **`**` Dictionary Unpacking | Converts dictionary values into model arguments    | Dictionary → arguments | `Customer(**data)`                     |
| **Insert Function**         | Receives Pydantic object and performs insert logic | Insert data            | `def insert(cust: Customers):`         |
| **Update Function**         | Receives Pydantic object and performs update logic | Update data            | `def update(cust: Customers):`         |

### ⭐ One-Line Revision

| Pydantic Concept    | Remember               |
| ------------------- | ---------------------- |
| `BaseModel`         | **Create model**       |
| `EmailStr`          | **Check email**        |
| `AnyUrl`            | **Check URL**          |
| `Field()`           | **Add rules**          |
| `Annotated`         | **Type + rules**       |
| `List`              | **Many values**        |
| `Dict`              | **Key + value**        |
| `Optional`          | **Value or None**      |
| `field_validator()` | **Custom rule**        |
| `@classmethod`      | **`cls` means class**  |
| Nested Model        | **Model inside model** |
| `**data`            | **Unpack dictionary**  |

### 🔥 Overall Flow

```text
Input Data
    ↓
Pydantic BaseModel
    ↓
Type Validation
    ↓
Field() Rules
    ↓
Custom field_validator()
    ↓
Valid Data
    ↓
Python Function / FastAPI
    ↓
Database
```

**Main idea:**

> **Pydantic = Define data structure + Validate data + Apply custom rules.**
