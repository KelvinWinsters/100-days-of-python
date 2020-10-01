import random


def guess_game():
    print("Number guessing game")
    count_number_of_tries = 1
    number_to_guess = random.randint(1, 10)
    guess = int(input("Enter a number between 1 and 10 : "))
    while number_to_guess != guess:
        print("Sorry wrong number")
        if count_number_of_tries == 4:
            break
        elif guess < number_to_guess:
            print("Your guess was lower than the number")
        else:
            print("Your guess was higher than the number")
        guess = int(input("Please Guess again "))
        count_number_of_tries += 1
    if number_to_guess == guess:
        print("Well done you won")
        print(f"You took {count_number_of_tries} guesses to complete the game")
    else:
        print("Sorry - you loose")
        print(f"The number you needed to guess was {number_to_guess}")

    print("Game over")


guess_game()
