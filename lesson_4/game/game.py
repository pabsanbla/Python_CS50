import random
import sys

def main():
    #level
    n = ask("Level: ")
    #create the random number
    number = random.randint(1, n)
    #guess
    while True:
        guess = ask("Guess: ")
        output(number, guess)


def ask(message):
    while True:
        try:
            number = int(input(message)) #not a int
            #not in our range
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            continue


def output(integer, guess):
    if guess < integer:
        print("Too small!")
    elif guess > integer:
        print("Too large!")
    else:
        sys.exit("Just right!")


main()

