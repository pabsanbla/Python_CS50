#Function version
def main():
    x = get_int("What´s x? ")
    print(f"x is {x}")

#Improvemeent better for the user
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass #use in case you don´t want any warning


main()
