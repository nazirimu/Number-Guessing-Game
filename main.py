from art import logo
import random
from replit import clear

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def guess_checker(guessed_number, actual_number):
    if guessed_number < actual_number:
        print('Too low!')
        print('Guess again.')
        return False 
    elif guessed_number > actual_number:
        print('Too high!')
        print('Guess again.')
        return False
    elif  guessed_number == actual_number:
        print('Perfect')
        return True

def difficulty_picker():
    level = input("What level would you like to play? Type 'easy' for easy and 'hard' for hard. \n").lower()
    if level == "easy":
        return EASY_LEVEL_LIVES
    else:
        return HARD_LEVEL_LIVES
 

def game():
    clear()
    print(logo)
    print('Welcome to the number guessing game!')
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    selected_number = random.randint(1,101)
    
    lives = difficulty_picker()

    win = False 
    while lives > 0 and not win:
        print(f'You have {lives} lives remaining.')
        guess = int(input("Enter a guess: "))
        win = guess_checker(guess, selected_number)
        print('====================================')
        lives -= 1

start_game= True
while start_game:
    restart_game = input('Type "y" to play the game. Type "n" to exit ').lower()
    if restart_game == 'y':
        game()
    else:
        start_game = False
        print('Goodbye!')





