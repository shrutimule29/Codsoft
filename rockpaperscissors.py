import random

user_score = 0
computer_score = 0

while True:
    print("Enter your choice: rock, paper or scissors")
    user = input("Your choice: ").lower()
    comp = random.choice(["rock", "paper", "scissors"])

    print("Computer choice:", comp)

    if user == comp:
        print("It's a tie")
    elif user == "rock" and comp == "scissors":
        print("You win")
        user_score += 1
    elif user == "paper" and comp == "rock":
        print("You win")
        user_score += 1
    elif user == "scissors" and comp == "paper":
        print("You win")
        user_score += 1
    elif user in ["rock", "paper", "scissors"]:
        print("Computer wins")
        computer_score += 1
    else:
        print("Invalid input")

    print("Score -> You:", user_score, "Computer:", computer_score)

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break
