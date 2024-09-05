def main():
    number = get_number()
    meow(number)


def get_number():
    #Infinite loop if the answer is bad
    while True:
        n = int(input("What´s n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
