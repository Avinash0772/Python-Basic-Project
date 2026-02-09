"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, Paper, Scissor)
2- Computer Choice()

Cases: 
A. Rock 
Rock - Rock = Tie
Rock - Paper = Paper Win 
Rock - Scissor = Rock Win

B. Paper
Paper - Paper = Tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor Win

C. Scissor
Scissor - Scissor = Tie 
Scissor - Paper = Scissor Win
Scissor - Rock = Rock win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")    
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper cover Rock = You Win")
    else:
        print("Scissor cuts paper = Computer Win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor = Computer Win")
    else:
        print("Scissor cuts paper = You Win")


