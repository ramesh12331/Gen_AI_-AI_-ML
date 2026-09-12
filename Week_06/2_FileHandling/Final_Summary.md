# 🏆 FINAL SUMMARY — PYTHON FILE HANDLING, BINARY & SERIALIZATION

Here is your **quick revision sheet** based on the chapter material we covered.

## 📂 1. File Handling

**Definition:** File handling means creating, opening, reading, writing, appending, and managing files using Python.

### ⚡ Modes Shortcut

| Mode | Meaning      | Shortcut     |
| ---- | ------------ | ------------ |
| `r`  | Read         | 📖 Read      |
| `w`  | Write        | ✍️ Write     |
| `a`  | Append       | ➕ Add at end |
| `x`  | Create       | 🆕 New file  |
| `rb` | Read Binary  | 📖💾         |
| `wb` | Write Binary | ✍️💾         |

### Basic Syntax

```python
with open("sample.txt", "r") as f:
    data = f.read()
```

🧠 **Remember:**

```text
open() → open file
read() → read data
write() → write data
close() → close file

with → automatically closes file
```

---

# 📖 2. Reading Files

```python
f.read()
```

➡️ Reads file content.

```python
f.readline()
```

➡️ Reads **one line**.

```python
f.readlines()
```

➡️ Reads lines into a **list**.

### ⚡ Shortcut

```text
read()      → ALL 📖
readline()  → ONE LINE 1️⃣
readlines() → LIST OF LINES 📋
```

---

# ✍️ 3. Writing vs Appending

### Write

```python
with open("sample.txt", "w") as f:
    f.write("Hello")
```

`w` can overwrite existing content.

### Append

```python
with open("sample.txt", "a") as f:
    f.write("Python")
```

`a` adds content at the end.

### ⚡ Shortcut

```text
w → WRITE / OVERWRITE ✍️
a → ADD AT END ➕
```

---

# 🎯 4. File Pointer

### `tell()`

Returns the current file-pointer position.

```python
print(f.tell())
```

### `seek()`

Moves the file pointer.

```python
f.seek(0)
```

### ⚡ Shortcut

```text
tell() → WHERE am I? 📍
seek() → GO there 🎯
```

---

# 📊 5. CSV

**CSV = Comma-Separated Values**

Used for table-like data.

```text
id,name,age
101,Rahul,25
102,Ajay,30
```

### Important Methods

```text
csv.writer()  → create writer ✍️
writerow()    → ONE row 1️⃣
writerows()   → MANY rows 🔢
csv.reader()  → read rows 📖
```

🧠 **Shortcut:**

> `writerow` = ROW = one
> `writerows` = ROWS = many

---

# 💾 6. Binary Files

Your notes distinguish text data from binary data: text uses characters, while binary data is handled as bytes. Examples given include images, audio, video, PDFs, and EXE files. 

```text
🔤 TEXT               💾 BINARY
   │                       │
Characters                 Bytes
   │                       │
 r / w                   rb / wb
```

### ⚡ Shortcut

```text
r  → Read Text
w  → Write Text

rb → Read Binary
wb → Write Binary
```

Example:

```python
with open("iphone.jpg", "rb") as f:
    data = f.read()
```

---

# 📦 7. Python Objects

Your notes mention these Python objects in the serialization section: 

```text
📋 List
📦 Tuple
🎯 Set
📖 Dictionary
```

A normal text `write()` cannot directly accept a list in the example from your notes:

```python
data = [2, 3, 4, 5, 6]

with open("sample.txt", "w") as f:
    f.write(data)
```

This results in a `TypeError` because the shown text `write()` expects a string. 

---

# 📦 8. Serialization

## Definition

**Serialization means converting a Python object into a format suitable for storage.**

Your notes show:

```text
Python Object
      │
      ▼
Serialization 📦
      │
      ▼
JSON / Text / Binary
```



### ⚡ Shortcut

> **Serialization = PACK 📦**

```text
🐍 Python Object
       ↓
Serialization
       ↓
💾 Stored Format
```

---

# 🔄 9. Deserialization

## Definition

**Deserialization means converting stored data back into a Python object.**

Your notes show the reverse direction: 

```text
JSON / Text / Binary
        │
        ▼
 Deserialization 🔄
        │
        ▼
 Python Object 🐍
```

### ⚡ Shortcut

> **Deserialization = UNPACK 📤**

---

# ⚖️ 10. Serialization vs Deserialization

| 📦 Serialization       | 🔄 Deserialization     |
| ---------------------- | ---------------------- |
| Python → Stored format | Stored format → Python |
| Saving direction       | Loading direction      |
| Pack                   | Unpack                 |
| Object goes out ➡️     | Object comes back ⬅️   |

### 🧠 Best Memory Trick

```text
Serialization
Python ➡️ Storage

Deserialization
Storage ➡️ Python
```

---

# 🗂️ 11. JSON & Pickle

Your notes mention:

```text
json module
pickle module
```

in connection with serialization/deserialization. 

For the supplied material, remember:

```text
             Serialization
                   │
             ┌─────┴─────┐
             ▼           ▼
           JSON        Pickle
```

📌 The supplied notes mention `pickle`, but they do **not** provide `pickle.dump()` / `pickle.load()` examples, so those are not included as source-derived syntax here.

---

# 🚀 MASTER SHORTCUT SHEET

```text
📂 open()
→ Open File

📖 read()
→ Read content

1️⃣ readline()
→ One line

📋 readlines()
→ Lines as list

✍️ write()
→ Write content

📖 r
→ Read

✍️ w
→ Write / overwrite

➕ a
→ Append

🆕 x
→ Create

📍 tell()
→ Current pointer position

🎯 seek()
→ Move pointer


📊 CSV
→ Table-like data

1️⃣ writerow()
→ One row

🔢 writerows()
→ Multiple rows

📖 csv.reader()
→ Read CSV


💾 rb
→ Read Binary

💾 wb
→ Write Binary

📦 Serialization
→ Python → Storage

🔄 Deserialization
→ Storage → Python

🗂️ json
→ Mentioned serialization module

🥒 pickle
→ Mentioned serialization module
```

# 🧠 ONE-MINUTE REVISION

```text
                 🐍 PYTHON FILE HANDLING
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
    🔤 TEXT             📊 CSV             💾 BINARY
       │                  │                  │
   r / w / a        reader/writer          rb / wb
       │                                     │
       ▼                                     ▼
 Characters                                Bytes

                 Python Objects 🐍
                        │
                        ▼
                Serialization 📦
                        │
                        ▼
                    Storage 💾
                        │
                        ▼
               Deserialization 🔄
                        │
                        ▼
                Python Objects 🐍
```

## 🏆 Most Important Interview Lines

> 📂 **File Handling:** Used to work with files in Python.
> 💾 **Binary File:** Data is handled as bytes.
> 📊 **CSV:** Comma-Separated Values; useful for tabular data.
> 📦 **Serialization:** Python Object → Stored Format.
> 🔄 **Deserialization:** Stored Format → Python Object.
> 🧠 **`tell()`** tells the current pointer position.
> 🎯 **`seek()`** moves the pointer.
> 📦 **Serialization = PACK; Deserialization = UNPACK.**
