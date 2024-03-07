import random

print("Guess the number 1 to 10")
guess = int(input("Write a number between 1 and 10: "))

if guess == random.randint(1, 10):
    print("You won")
else:
    print("You lost")




