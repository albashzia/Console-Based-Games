import random
choices = ["rock","paper","scissors"]
choice = random.choice(choices)
user_choice = input("Enter your choice(rock,paper,scissors) : ").strip().lower()

if user_choice not in choices:
    print("Invalid Choice")

elif user_choice == "paper":
    if choice == "scissors":
        print("You Lose")
    elif choice == "paper":
        print("It's a Tie")
    else:
        print("You Win")

elif user_choice == "rock":
    if choice == "paper":
        print("You Lose")
    elif choice == "rock":
        print("It's a Tie")
    else:
        print("You Win")

elif user_choice == "scissors":
    if choice == "rock":
        print("You Lose")
    elif choice == "scissors":
        print("It's a Tie")
    else:
        print("You Win")
