import random

def get_person2_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def determine_winner(user_choice, person2_choice):
    if user_choice == person2_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and person2_choice == 'scissors') or \
       (user_choice == 'scissors' and person2_choice == 'paper') or \
       (user_choice == 'paper' and person2_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_person2_choice()
        print(f"\nYou chose {user_choice}, and the person2 chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
