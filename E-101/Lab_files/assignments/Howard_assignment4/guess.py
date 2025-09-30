# Matthew Howard
import random

def generate_random_number():
    """Generate and return a random number between 1 and 100."""
    return random.randint(1, 100)

def play_game(max_attempts):
    """Play the guessing game with the given number of attempts."""
    target = generate_random_number()
    attempts = 0

    while attempts < max_attempts:
        
        guess = int(input("Enter your guess (1-100): "))
  


        attempts += 1

        if guess == target:
            print(f" Correct! You guessed the number {target} in {attempts} attempts.")
            return
        elif guess < target:
            print("Too low Try again.")
        else:
            print("Too high Try again.")

    print(f" Out of attempts! The correct number was {target}.")

def main():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level: easy (20 attempts), medium (10 attempts), hard (5 attempts).")
    print("Type 'exit' to quit at any time.\n")

    while True:
        choice = input("Enter difficulty (easy/medium/hard) or 'exit': ").strip().lower()

        if choice == "exit":
            print(" Thanks for playing!")
            break
        elif choice == "easy":
            play_game(20)
        elif choice == "medium":
            play_game(10)
        elif choice == "hard":
            play_game(5)
        else:
            # edge cases
            print("Invalid choice! Please enter 'easy', 'medium', 'hard', or 'exit'.")


main()