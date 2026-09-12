# ==========================================================
# PYTHON WHILE LOOP
# ==========================================================

# Three Major Rules:
# 1. Counter Variable
# 2. Proper Condition
# 3. Increment / Decrement


# ==========================================================
# Example 1 : Print "Hello User" 6 Times
# ==========================================================

i = 0

while i <= 5:
    print("Hello User!")
    i += 1


# Output:
# Hello User!
# Hello User!
# Hello User!
# Hello User!
# Hello User!
# Hello User!


# ==========================================================
# Example 2 : Print Numbers 0 to 5
# ==========================================================

i = 0

while i <= 5:
    print(i)
    i += 1


# Output:
# 0
# 1
# 2
# 3
# 4
# 5


# ==========================================================
# Example 3 : Increment First
# ==========================================================

i = 0

while i <= 5:
    i += 1
    print(i)


# Output:
# 1
# 2
# 3
# 4
# 5
# 6


# ==========================================================
# Example 4 : Print Even Numbers
# ==========================================================

i = 0

while i <= 10:
    print(i, end=" ")
    i += 2


# Output:
# 0 2 4 6 8 10


# ==========================================================
# Example 5 : Print Odd Numbers
# ==========================================================

i = 1

while i <= 10:
    print(i, end=" ")
    i += 2


# Output:
# 1 3 5 7 9


# ==========================================================
# Example 6 : Reverse Order
# ==========================================================

i = 10

while i >= 1:
    print(i, end=" ")
    i -= 1


# Output:
# 10 9 8 7 6 5 4 3 2 1


# ==========================================================
# Example 7 : Human Control
# ==========================================================

while True:

    command = input("Enter Command : ")

    if command == "Exit":
        break

print("Program Closed")


# ==========================================================
# Example 8 : Human Control (Ignore Case)
# ==========================================================

while True:

    command = input("Enter Command : ").lower()

    if command == "exit":
        break

print("Program Closed")


# ==========================================================
# Example 9 : Nested While Loop
# ==========================================================

i = 0

while i <= 3:

    j = 0

    while j <= 4:
        print(i, j)
        j += 1

    i += 1


# Output:
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 1 0
# ...
# 3 4


# ==========================================================
# Example 10 : Continue Statement
# ==========================================================

numbers = [10, 20, 30, 50, 80]

for num in numbers:

    if num == 80:
        continue

    print(num)


# Output:
# 10
# 20
# 30
# 50


# ==========================================================
# Example 11 : Infinite Loop (Press Ctrl + C to Stop)
# ==========================================================

# while True:
#     print("Running...")


# ==========================================================
# Example 12 : Bike Game
# ==========================================================

started = False

while True:

    command = input("Command > ").lower()

    if command == "help":

        print("""
-------------------------------
Available Commands
-------------------------------

start  -> Start Bike
stop   -> Stop Bike
exit   -> Exit Game
help   -> Show Commands

-------------------------------
""")

    elif command == "start":

        if started:
            print("Bike is already started.")

        else:
            started = True
            print("Bike Started.")

    elif command == "stop":

        if not started:
            print("Bike is already stopped.")

        else:
            started = False
            print("Bike Stopped.")

    elif command == "exit":

        print("Game Closed.")
        break

    else:

        print("Invalid Command")


# ==========================================================
# Example 13 : Print Multiples of 5
# ==========================================================

i = 5

while i <= 50:
    print(i, end=" ")
    i += 5


# Output:
# 5 10 15 20 25 30 35 40 45 50


# ==========================================================
# Example 14 : Countdown
# ==========================================================

count = 5

while count > 0:
    print(count)
    count -= 1

print("Time Up!")