import random

# TODO: Add a win counter


def get_number():
    return random.randint(1, 100)


def choose_difficulty(chances=0):
    difficulty = input("Enter you choice of difficulty: ").lower()
    if difficulty == "easy":
        chances = 10
    elif difficulty == "medium":
        chances = 5
    elif difficulty == "hard":
        chances = 3
    else:
        print("Please choose a difficulty")
        choose_difficulty()
    return chances


def main():
    print("\nWelcome to the Number Guessing Game!")
    print(
        "The game where a random number from 1 to 100 is chosen and you have to guess what that number is.\n"
    )

    game_playing = True

    while game_playing:

        print("\nPlease select the difficulty level:")
        print("Easy (10 chances)")
        print("Medium (5 chances)")
        print("Hard (3 chances)")

        chances = choose_difficulty()
        number = get_number()

        attempts = 0

        while chances > 0:
            try:
                guess = int(float(input("Enter your guess: ")))
            except ValueError:
                print("That's not a number. Try again")

            attempts += 1

            if guess == number:
                print(
                    f"Congratulations! you guessed the correct number in {attempts} attempts.\n"
                )
                break
            else:
                chances -= 1
                if guess > 100 or guess < 1:
                    print(
                        "Your guess is out of bounds. The number is between 0 and 100."
                    )
                elif guess > number:
                    print(f"The number is less than {guess}")
                elif guess < number:
                    print(f"The number is higher than {guess}")

        while True:
            keep_playing = input("Would you like to play again? yes or no: ").lower()
            if keep_playing == "yes":
                break
            elif keep_playing == "no":
                return
            else:
                print("\nPlease enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
