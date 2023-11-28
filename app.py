import random

options = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(options)

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    while user_choice not in options:
        user_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ")
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    return 'computer'

def play_again():
    play_again = input("Play again? (y/n): ")
    while play_again not in ['y', 'n']:
        play_again = input("Invalid choice. Play again? (y/n): ")
    return play_again == 'y'

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    if winner == 'user':
        user_score += 1
        print(f'User chose {user_choice}, computer chose {computer_choice}. User wins this round!')
    elif winner == 'computer':
        computer_score += 1
        print(f'User chose {user_choice}, computer chose {computer_choice}. Computer wins this round!')
    else:
        print(f'User chose {user_choice}, computer chose {computer_choice}. It\'s a tie!')
    print(f'Score: User - {user_score}, Computer - {computer_score}')
    if not play_again():
        break