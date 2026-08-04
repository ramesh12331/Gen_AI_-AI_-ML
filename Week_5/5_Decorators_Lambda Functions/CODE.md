These screenshots are from your **31-07-2026 Python Session**. The topics covered are:

1. Lists & Memory (`sys.getsizeof()`)
2. Functions
3. Generators (`yield`)
4. `next()`
5. `filter()`
6. `lambda`
7. Common mistake (`list` object is not callable)

Below is the cleaned-up code in VS Code format with simple explanations.

---

# 1. Creating a List using while loop

```python
# ============================================
# CREATE LIST USING WHILE LOOP
# ============================================

numbers = []

i = 0

while i <= 200:
    numbers.append(i)
    i += 1

print(numbers)
```

### Output

```
[0, 1, 2, 3, ..., 200]
```

---

# 2. Checking List Memory

```python
import sys

numbers = []

i = 0

while i <= 200:
    numbers.append(i)
    i += 1

print(sys.getsizeof(numbers))
```

Example Output

```
1912
```

### Explanation

`sys.getsizeof()` returns the memory occupied by the list in bytes.

---

# 3. Wrong Way

```python
for i in range(1, 201):
    numbers = []
    numbers.append(i)

print(numbers)
```

Output

```
[200]
```

### Why?

Every loop creates a **new empty list**, so previous values are lost.

---

# 4. Correct Way

```python
numbers = []

for i in range(1, 201):
    numbers.append(i)

print(numbers)
```

Output

```
[1,2,3,4,5,...,200]
```

---

# 5. Memory Check Again

```python
import sys

numbers = []

for i in range(1, 201):
    numbers.append(i)

print(sys.getsizeof(numbers))
```

Output (may vary)

```
1656
```

---

# 6. Normal Function

```python
def generate():

    i = 0

    while i <= 200:
        print(i, end=" ")
        i += 1


generate()
```

Output

```
0 1 2 3 4 5 ... 200
```

---

# 7. Generator Function

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


generate()
```

Output

```
<generator object generate at 0x...>
```

### Why?

`yield` returns a **generator object** instead of executing everything immediately.

---

# 8. Using next()

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

print(next(a))
print(next(a))
print(next(a))
```

Output

```
0
1
2
```

---

# 9. Using for loop with Generator

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

for value in a:
    print(value, end=" ")
```

Output

```
0 1 2 3 4 ... 200
```

---

# 10. Convert Generator into List

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

numbers = []

for value in a:
    numbers.append(value)

print(numbers)
```

Output

```
[0,1,2,3,...,200]
```

---

# 11. Memory of Generator Result

```python
import sys

def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

numbers = []

for value in a:
    numbers.append(value)

print(sys.getsizeof(numbers))
```

Output

```
1912
```

---

# 12. Filter Example

```python
numbers = [1,2,3,4,5,6,7,8,9]


def even(x):

    if x % 2 == 0:
        return True


result = filter(even, numbers)

print(result)
```

Output

```
<filter object at 0x...>
```

---

# 13. Convert Filter to List

```python
numbers = [1,2,3,4,5,6,7,8,9]


def even(x):

    return x % 2 == 0


result = list(filter(even, numbers))

print(result)
```

Output

```
[2, 4, 6, 8]
```

---

# 14. Common Error

```python
list = [1,2,3]

result = list(filter(even, list))
```

Output

```
TypeError:
'list' object is not callable
```

### Why?

You stored a list in the variable named `list`, which hides Python's built-in `list()` function.

❌ Wrong

```python
list = [1,2,3]
```

✅ Correct

```python
numbers = [1,2,3]
```

---

# 15. Filter using Lambda

```python
numbers = [1,2,3,4,5,6,7,8,9]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

Output

```
[2, 4, 6, 8]
```

---

# Quick Revision

| Topic                          | Purpose                                      |
| ------------------------------ | -------------------------------------------- |
| `append()`                     | Add an element to a list                     |
| `sys.getsizeof()`              | Check memory used by an object               |
| `yield`                        | Create a generator                           |
| `next()`                       | Get the next value from a generator          |
| `filter()`                     | Keep elements that satisfy a condition       |
| `lambda`                       | Anonymous one-line function                  |
| `list(filter(...))`            | Convert a filter object into a list          |
| Avoid naming a variable `list` | It hides Python's built-in `list()` function |

These notes cover everything visible in your screenshots up to the introduction of **Decorators, Lambda Functions, and Generators**.
