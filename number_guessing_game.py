import random


def number_guessing_game():
    random_num = random.randint(0, 9)
    guess_count = 3

    for i in range(guess_count):
        try:
            num = int(input("Guess a number between 0 to 9: "))
        except ValueError:
            print("Enter a valid number!")
            return

        if num == random_num:
            print("You won 🎉")
            return
        elif num > random_num:
            print("Guess is too high!")
        else:
            print("Guess is too low!")

    print("You lose ☹️")


number_guessing_game()
