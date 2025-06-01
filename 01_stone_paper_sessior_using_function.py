import random

def game():
    choices = ["stone", "paper", "scissor"]
    user = input("Enter your choice (stone/paper/scissor): ").lower()
    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a draw!")
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        print("You win!")
    elif user in choices:
        print("You lose!")
    else:
        print("Invalid input! Try again.")

# Run the game
game()
