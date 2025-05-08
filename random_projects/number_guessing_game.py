from random import randint

# Constants for the number of turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    """Sets the difficulty level and returns the number of turns."""
    level = input("Choose your difficulty: 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(user_guess, actual_answer, turns):
    """Checks the user's guess against the actual answer and provides feedback."""
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"Your guess is correct! The number was {actual_answer}.")
        return 0  # Indicates the user has guessed correctly

def game():
    """Main function to run the number guessing game."""
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_answer = randint(1, 100)  # Generate a random number
    turns = set_difficulty()  # Determine the number of turns

    # Game loop
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        turns = check_answer(user_guess, actual_answer, turns)

        if turns == 0 and user_guess != actual_answer:
            print(f"You've run out of guesses. The correct number was {actual_answer}.")
        elif user_guess == actual_answer:
            break

# Start the game
game()
