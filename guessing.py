import random

def number_guessing_game():
    print("Welcome to 'Guess the Number'!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 10
    
    # Track if the game is still ongoing
    game_over = False
    
    while not game_over and attempts > 0:
        try:
            # Get the player's guess
            guess = int(input(f"You have {attempts} attempts remaining. Make a guess: "))
            
            # Check if the guess is too high, too low, or correct
            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                game_over = True
            
            # Reduce the number of attempts
            attempts -= 1

            # If no attempts are left and the number hasn't been guessed
            if attempts == 0 and not game_over:
                print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        
        except ValueError:
            print("Please enter a valid integer.")
    
    print("Game Over. Thanks for playing!")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
