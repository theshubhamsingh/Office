import random

possible_actions = ["rock", "paper", "scissors"]

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    while user_action not in possible_actions:
        user_action = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    
    if user_action == computer_action:
        print(f"Oops, You both chose the same {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Is it interesting? Do you want to play it again? (yes/no): ").lower()
    if play_again != "yes":
        break
    