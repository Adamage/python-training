print("Guessing game. You will attempt to guess the randomly generated number")

from random import randint

number_to_guess = randint(0,20)

guessed = False

while not guessed:
    user_guess = input("Guess the number between 1 and 20 \n")
    user_guess = int(user_guess)

    if user_guess == number_to_guess:
        guessed = True
        print("You guessed correctly!")
        continue

    if user_guess > number_to_guess:
        print("Try something lower")
        continue

    print("Try something higher")
