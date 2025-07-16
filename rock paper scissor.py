import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    if choice in choices:
        return choice
    else:
        print("Invalid choice. Try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play()