import random 
choose = ["stone", "paper", "scissor"]
computer = random.choice(choose)
 
user = str(input("Choose stone/paper/scissor : ")).lower()


if user == "stone" or user == "paper" or user == "scissor":
  print(f"Computer chooses {computer}")


if user == computer:
    print("It's a draw!")
elif (user == "stone" and computer == "scissor") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissor" and computer == "paper"):
    print("You win!")
elif (user == "stone" and computer == "paper") or \
     (user == "paper" and computer == "scissor") or \
     (user == "scissor" and computer == "stone"):
    print("You lose!")
else:
    print("Invalid input! Please choose stone, paper, or scissor.")