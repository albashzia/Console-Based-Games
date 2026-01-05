import random

# creating a list of choices holding three possible user choices
choices = ["rock","paper","scissors"]

# storing a random word from choices list in choice
choice = random.choice(choices)

# taking user's choice, removing extra spaces and turning it to lower case
user_choice = input("Enter your choice(rock,paper,scissors) : ").strip().lower()

# handling an invalid choice entered by user which is not present in choices list 
if user_choice not in choices:
    print("Invalid Choice")
    
# handling the case when user enters "paper"
elif user_choice == "paper":
    if choice == "scissors":
        print("You Lose")
    elif choice == "paper":
        print("It's a Tie")
    else:
        print("You Win")
        
# handling the case when user enters "rock"
elif user_choice == "rock":
    if choice == "paper":
        print("You Lose")
    elif choice == "rock":
        print("It's a Tie")
    else:
        print("You Win")
        
# handling the case when user enters "scissors"
elif user_choice == "scissors":
    if choice == "rock":
        print("You Lose")
    elif choice == "scissors":
        print("It's a Tie")
    else:
        print("You Win")
