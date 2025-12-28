import random
print("Number Guessing Game")
print("Welcome to the Number Guessing Game")
attempts = 0
secret_number = random.randint(1,10)
while True:
    num = int(input("Enter a number between 1 and 10 : "))
    attempts = attempts + 1
    if num > secret_number:
        print("High")
    elif num<secret_number:
        print("Low")
    elif num == secret_number:
        print("You guessed it right in",attempts,"attempts")
        break
