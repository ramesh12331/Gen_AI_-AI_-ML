"""
===========================================================
                 PYTHON WHILE LOOPS & FUNCTIONS
===========================================================

Topics Covered
1. While Loop
2. Infinite Loop
3. Nested While Loop
4. Bike Game
5. Functions
6. Arguments
7. *args
8. Guess Number Game
9. Password Validation

===========================================================
"""
# ===========================================================
# 1. While Loop
# ===========================================================

i = 1

while i <= 50:
    print(i, end=" ")
    i += 6
else:
    print("\nExecuted Successfully")
# ===========================================================
# 2. Reverse While Loop
# ===========================================================
i = 10

while i >= 1:
    print(i, end=" ")
    i -= 2

print("\n")
# ===========================================================
# 3. Infinite Loop
# ===========================================================

while True:
    command = input("Enter Command : ").lower()

    if command == "exit":
        print("Program Closed")
        break
    print("You Entered :", command)

# ===========================================================
# 4. Nested While Loop
# ===========================================================
i = 0

while i <= 3:
    j=0
    while j <= 4:
        print(i, j)
        j += 1
    i += 1

# ===========================================================
# 5. Continue Example
# ===========================================================
numbers = [10, 20, 30, 50, 80]

for num in numbers:
    if num == 20:
        continue
        # break
    print(num)

# ===========================================================
# 6. Bike Game
# ===========================================================
print("\n========== Bike Game ==========")

started = False

while True:
    command = input('Command > ').lower()
    if command == "help":
        print("""
                Available Commands
                start  -> Start Bike
                stop   -> Stop Bike
                exit   -> Exit Game
                help   -> Show Commands
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

