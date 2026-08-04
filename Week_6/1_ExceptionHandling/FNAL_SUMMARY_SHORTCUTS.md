# ⚡ Python Exception Handling — Final Summary Shortcuts

Use this as your **last-minute interview revision sheet**.

| 🔑 Keyword / Error  | 🧠 Shortcut to Remember             |
| ------------------- | ----------------------------------- |
| `SyntaxError`       | ❌ Python grammar mistake            |
| `NameError`         | ❌ Variable/name not found           |
| `IndexError`        | ❌ Index not available               |
| `KeyError`          | ❌ Dictionary key not available      |
| `TypeError`         | ❌ Wrong/incompatible type           |
| `ValueError`        | ❌ Correct type idea, invalid value  |
| `AttributeError`    | ❌ Method/attribute not available    |
| `ZeroDivisionError` | ❌ Divide by `0`                     |
| `FileNotFoundError` | ❌ File not found                    |
| `try`               | 🧪 Put risky code here              |
| `except`            | 🛡️ Handle the error                |
| `else`              | ✅ Runs when **no exception** occurs |
| `finally`           | 🔄 Runs **always**                  |
| `raise`             | 🚨 Manually generate an exception   |
| `Exception as e`    | 📩 Get the error message            |
| Custom Exception    | 🧬 Your own exception class         |

## 🧠 Golden Shortcut

```text
try     → TRY the risky code 🧪
except  → ERROR? Handle it 🛡️
else    → NO ERROR? Run it ✅
finally → ALWAYS run it 🔄
raise   → CREATE/SIGNAL an error 🚨
```

### ⭐ Basic Syntax

```python
try:
    # risky code

except Exception as e:
    print(e)

else:
    # runs if no exception

finally:
    # always runs
```

### 🚨 `raise` Shortcut

```python
if problem:
    raise Exception("Error message")
```

Think:

```text
Condition True
     ↓
raise
     ↓
Exception 🚨
```

### 🧬 Custom Exception Shortcut

```python
class MyException(Exception):
    pass
```

Use:

```python
raise MyException("Something went wrong")
```

Handle:

```python
try:
    # code

except MyException as e:
    print(e)
```

## 🏗️ OOP + Exception Shortcut

This is the most important pattern from your chapter:

```python
class BalanceException(Exception):
    pass


class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise BalanceException(
                "Insufficient Balance"
            )

        self.balance -= amount


account = Bank(5000)

try:
    account.withdraw(2000)

except BalanceException as e:
    print(e)

else:
    print("Success")

finally:
    print("Completed")
```

Remember the flow:

```text
🏗️ Class
   ↓
📦 Object
   ↓
🔧 Method
   ↓
🔍 Check Condition
   ↓
🚨 raise
   ↓
🧬 Custom Exception
   ↓
🛡️ except
```

## 🎯 Real-Time Shortcut Table

| Application    | Condition          | Exception           |
| -------------- | ------------------ | ------------------- |
| 🏧 ATM         | `amount > balance` | `BalanceException`  |
| 💰 Amount      | `amount <= 0`      | `AmountException`   |
| 🔐 Login       | Wrong credentials  | `LoginException`    |
| 📱 Device      | Wrong device       | `SecurityException` |
| 🎓 Student     | Invalid marks      | `MarksException`    |
| 👨‍💼 Employee | Invalid salary     | `SalaryException`   |
| 🛒 Shopping    | `quantity > stock` | `StockException`    |

## 🔥 One-Line Interview Answers

**Exception:** 🚨 An error that occurs during program execution.

**Exception Handling:** 🛡️ Handling runtime errors without abruptly stopping the program.

**`try`:** 🧪 Contains risky code.

**`except`:** 🛡️ Handles an exception.

**`else`:** ✅ Executes when no exception occurs.

**`finally`:** 🔄 Executes whether an exception occurs or not.

**`raise`:** 🚨 Manually raises an exception.

**Custom Exception:** 🧬 A user-defined exception created by inheriting from `Exception`.

**`Exception as e`:** 📩 Stores the caught exception object so we can access its error message.

## 🏆 MASTER SHORTCUT

```text
            🧪 TRY
              │
        ┌─────┴─────┐
        │           │
     ERROR 🚨    NO ERROR ✅
        │           │
        ▼           ▼
     EXCEPT        ELSE
        │           │
        └─────┬─────┘
              ▼
          FINALLY 🔄
```

### 💡 Remember only this for interviews:

> **TRY → Risky Code 🧪 | EXCEPT → Error 🛡️ | ELSE → Success ✅ | FINALLY → Always 🔄 | RAISE → Create/Signal Error 🚨**

And for OOP:

> **Class → Object → Method → Condition → `raise` → Custom Exception → `except`** ⭐
