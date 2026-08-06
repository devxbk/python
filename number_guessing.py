import random

random_num = random.randint(1, 100)
guess_count = 0

while guess_count < 3:
    guess = int(input("Guess a number: "))
    guess_count += 1

    if guess == random_num:
        print(f"Congralution!, You guessed the number in {guess_count} attempts.")
        break
    elif guess < random_num:
        print("Too low!")
    else:
        print("Too high!")

if guess != random_num:
    print(f"Sorry! You have used all 3 attempts. The nunmber was {random_num}. ")
