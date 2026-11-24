import random

def guess_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=== Number Guessing Game ===")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print(f"Correct! You won in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_game()
