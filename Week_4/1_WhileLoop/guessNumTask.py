import random

secret = random.randint(1,100)

attemts = 5

while attemts>0:
    guess = int(input("Guess (1-100): "))
    if guess == secret:
        print("Correct Guess.")
        break
    elif guess > secret:
        print("Too High.")
    else:
        print("Too Low.")

    attemts -= 1
    print("Attempts Left :", attemts)

else:
    print("You Lost.")
    print("Secret Number :", secret)