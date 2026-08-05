# ----------------------------------------------------------
# Example 1
# If file is not present,
# Python automatically creates it.
# ----------------------------------------------------------
f = open("sample.txt", "w")
f.write("heyy")
f.close()

# ==========================================================
# Writing Multiple Lines
# ==========================================================
f = open("sample.txt", "w")
f.write("heyyy")
f.write("hello")
f.write("how are you?")

f.close()

# ==========================================================
# Writing using newline
# ==========================================================

f = open("sample.txt", "w")
f.write("heyyy")
f.write("\nhello")
f.write("\nhow are you?")
f.close()

# ==========================================================
# Cannot write after closing file
# ==========================================================
f = open("sample.txt", "w")
f.write("heyyy")
f.write("\nhello")
f.write("\nhow are you?")
f.close()

# Raises ValueError
# f.write("heyyy raghav")

# ==========================================================
# Problem with 'w' Mode
# ==========================================================

"""
'w'

If file already exists,
all previous content is deleted.

Then new content is written.
"""
f = open("sample.txt","w")
f.write("python")
f.close()

# ==========================================================
# Solution -> Append Mode
# ==========================================================

"""
'a'

Append Mode

Adds new content
without deleting old content.
"""
f = open("sample.txt", "w")
f.write("\njava")
f.close()

# ==========================================================
# writelines()
# ==========================================================

languages = [
    "python",
    "\njava",
    "\nC",
    "\nsql"
]
f = open("sample.txt", "a")
f.writelines(languages)
f.close()

# ==========================================================
# writelines() using loop
# ==========================================================

languages = [
    "python",
    "java",
    "C",
    "sql"
]

f = open("sample.txt", "w")
for language in languages:
    f.writelines(language)
f.close()

"""
Output inside file

pythonjavaCsql
"""
# ==========================================================
# Read From File
# ==========================================================
f = open("sample.txt", "r")
print(f.read())
f.close()

# ==========================================================
# Read first n characters
# ==========================================================

f = open("sample.txt", "r")
print(f.read(5))
print(f.read(5))
f.close()

"""
Suppose file contains

pythonjavaCsql

Output

pytho
njava
"""

# ==========================================================
# 3. READ NEXT N CHARACTERS
# ==========================================================
f = open("sample.txt", "r")
print(f.read(5))
print(f.read(5))
print(f.read(5))
f.close()

# ==========================================================
# 4. READ ONE LINE
# ==========================================================
f = open("sample.txt", "r")

print(f.readline())
f.close()

# ==========================================================
# 5. READ MULTIPLE LINES
# ==========================================================
f = open("sample.txt", "r")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline())
f.close()

# ==========================================================
# 6. READ ENTIRE FILE USING read()
# ==========================================================
f = open("sample.txt", "r")

data = f.read()
for ch in data:
    print(ch, end=" ")
f.close()

# ==========================================================
# 7. READ USING readlines()
# ==========================================================
print("\n")
f = open("sample.txt", "r")

data = f.read()
print(data)
for ch in data:
    print(ch, end=" ")
f.close()

# ==========================================================
# 8. CONTEXT MANAGER (with)
# Automatically closes the file.
# ==========================================================
print("\n CONTEXT MANAGER (with)")
with open("sample.txt", "r") as f:
    print(f.read(5))
    print(f.read(5))
    print(f.read(5))

# ==========================================================
# 9. WRITING USING with
# 'w' mode overwrites existing content.
# ==========================================================
print("\n WRITING USING with")

with open("sample.txt", "w") as f:
    f.write("heyy this is new way to write into file")

# ==========================================================
# 10. WRITING MULTIPLE LINES
# ==========================================================
# lines = ["python\n" for _ in range(10)]
lines = ["python " for _ in range(100000)]

with open("sample.txt", "w") as f:
    for line in lines:
        f.write(line)
# ==========================================================
# SUMMARY
# ==========================================================
# open()      -> Opens a file
# read()      -> Reads entire file
# read(n)     -> Reads n characters
# readline()  -> Reads one line
# readlines() -> Reads all lines as a list
# write()     -> Writes data
# close()     -> Closes the file
# with        -> Automatically closes the file

# ==========================================================
# PYTHON FILE HANDLING - PART 2 (As per screenshots)
# ==========================================================

import time

# ==========================================================
# READING LARGE FILES USING CHUNKS
# ==========================================================

# with open("sample.txt", "r") as f:
#     chunk = 100

#     while len(f.read(chunk)) > 0:
#         print(f.read(chunk), end="**********")
#         time.sleep(0.5)
# ----------------------------------------------------------
# Why read 100 characters at a time?
# ----------------------------------------------------------
# * Uses less RAM
# * Best for large files
# * Faster for huge files
# * Common in log file processing

# ==========================================================
# tell() FUNCTION
# Returns current cursor position
# ==========================================================
with open("sample.txt", "r") as f:
    print(f.read(5))
    print(f.tell())
    print(f.read(5))
    print(f.tell())

# ==========================================================
# seek() FUNCTION
# Moves cursor to any position
# ==========================================================
print("\n seek")
with open("sample.txt", "r") as f:
    print(f.read(5))
    print(f.tell())

    f.seek(0)
    print(f.read(5))
print()

# ==========================================================
# seek() IN WRITE MODE
# ==========================================================

with open("sample.txt", "w") as f:
    f.write("python")
    f.seek(2)
    f.write("z")

# Output in file:
# pyzhon

# ==========================================================
# ERROR - WRITING A LIST
# ==========================================================

data = [2, 3, 4, 5, 6]

try:
    with open("sample.txt", "w") as f:
        f.write(data)
except TypeError as e:
    print(e)

# write() argument must be str, not list

# ==========================================================
# ERROR - WRITING FILE OBJECT
# ==========================================================

try:
    with open("iphone.jpg", "rb") as f:
        f.write(f)
except Exception as e:
    print(e)