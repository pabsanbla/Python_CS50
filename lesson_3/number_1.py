#Function version
def main():
    x = get_int()
    print(f"x is {x}")

#Improvemeent better for the user
def get_int():
    while True:
        try:
            x = int(input("What´s is x? "))
            return x
        except ValueError:
            print("x is not an integer")


main()
