import random


def main():
    questions = 10 #number of questions asked
    score = 0 #to know the score
    level = get_level()

    while questions != 0:
        x = generate_integer(level)
        y = generate_integer(level)
        attemps = 0 #Initialized before trying
        while attemps < 3:
            try:
                solution = int(input(f"{x} + {y} = "))
                if int(solution) != (x + y):
                    raise ValueError
                break
            except ValueError:
                attemps += 1
                print("EEE")
        #check
        if attemps == 3:
           print(f"{x} + {y} = {x + y}")
        else:
            score += 1
        #actualitation
        questions -= 1

    print(f"Score: {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: ")) #not a int
            #not in our range
            if level not in levels:
                raise ValueError
            return level
        except ValueError:
            continue


def generate_integer(level):
    #Generate a number
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10,99)
    else:
        integer = random.randint(100, 999)
    return integer


if __name__ == "__main__":
    main()
