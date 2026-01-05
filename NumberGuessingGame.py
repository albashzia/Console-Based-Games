import random
# welcome statements
print("Number Guessing Game")
print("Welcome to the Number Guessing Game")

attempts = 0 # counter for number of attempts

secret_number = random.randint(1,10) # generating a random number between 1 and 10

while True: # running until the correct number is guessed
    num = int(input("Enter a number between 1 and 10 : "))
    attempts = attempts + 1 # incrementing number of attempts on each loop
    
    if num > secret_number:
        print("High")
        
    elif num<secret_number:
        print("Low")
        
    elif num == secret_number:
        print("You guessed it right in",attempts,"attempts")
        break # breaking once the correct number is guessed
