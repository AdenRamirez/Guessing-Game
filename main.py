#importing random files
from random import seed
from random import randint
guess = int(input("Guess a number 1-100: "))
amt = int(input("How many times do you want to play?"))
for i in range(amt):
    answer = randint(1, 100)
    while True:
        if answer==guess:
            print("Correct")
            break
        elif answer>guess:
            print("Try a higher number")
            guess = int(input("Guess a number 1-100: "))
        elif answer < guess:
            print("Try a lower number")
            guess = int(input("Guess a number 1-100: "))
