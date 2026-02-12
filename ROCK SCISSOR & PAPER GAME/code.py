import random

# Choices available
ITEMS = ["Rock", "Paper", "Scissor"]


def get_user_choice():
    while True:
        user = input("Enter Rock, Paper or Scissor: ").strip().capitalize()
        if user in ITEMS:
            return user
        else:
            print("Invalid choice  Please try again.\n")


def decide_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissor") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissor" and computer == "Paper"):
        return "User"
    else:
        return "Computer"


def play_game():
    user_score = 0
    computer_score = 0
    rounds = 5

    print("\n Welcome to Rock Paper Scissors Game")
    print("------ Best of 5 Rounds ------\n")

    for round_num in range(1, rounds + 1):
        print(f"\n Round {round_num}")
        
        user_choice = get_user_choice()
        computer_choice = random.choice(ITEMS)

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "User":
            print("You Win this round!")
            user_score += 1
        elif result == "Computer":
            print("Computer Wins this round!")
            computer_score += 1
        else:
            print("It's a Tie!")

        print(f"Score ➝ You: {user_score} | Computer: {computer_score}")

    print("\nFinal Result")
    if user_score > computer_score:
        print("Congratulations! You Won the Game!")
    elif computer_score > user_score:
        print("Computer Won the Game!")
    else:
        print("The Game is a Tie!")


# Main loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! ")
        break


