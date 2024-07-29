#number guessing game

import random

def number_guess():
    lower_bound = 1
    upper_bound = 100
    
    playing_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    welcome_message = "Welcome to the Number Guessing Game!"
    print(welcome_message)
    confirm = input("Press 'Y' to start the game: ").strip()
    
    if confirm in ('y', 'Y'):
        print(f"I am guessing a number between {lower_bound} and {upper_bound}.")
        
        while True:
            try:
                user_guess = int(input("Enter your guess: "))
                attempts += 1
                
                if user_guess > playing_number:
                    print("It's Lower")
                elif user_guess < playing_number:
                    print("It's Higher")
                else:
                    print(f"Congrats, you WIN!!! The number was {playing_number}. You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("Game not started. Please run the program again and press 'Y' to start.")

# Start the game
number_guess()


#created by Silika 