'''
Guess my number game. Computer generates a random interger between 1 and 20. Users are given 5 attempts to guess this number.
'''


import random


def guess_my_number():
    print(" I am thinking of a number between 1 and 20. \n You have 5 attempts to guess my number. All the best!.")
    wrong_guess: int = 0
    r_number = random.randint(1, 20)
    while True:
        if wrong_guess >= 5:  # IF COUNT(incorrect) is 5 times
            print("You have run out out of 5 attempts! Better Luck next time.")
            break  # stop loop
        else:
            n = int(input("Take a Guess: "))
            if n < r_number:
                print("Number is Low")
            elif n > r_number:
                print("Number is High")
            else:
                # Tell user if they are correct or not
                if n == r_number:
                    print("Great! You Guessed my number in {0} attempts.".format(wrong_guess + 1))
                    return print("Hope you enjoyed this Number Guess game.")
            wrong_guess += 1


guess_my_number()
