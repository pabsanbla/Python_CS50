#Conditionals
def main():
    difficulty = input("Difficult or casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike" )
        else:
            print("Enter a valid number of the users")
    elif difficulty == "Casual":
        if players == "Multiplayers":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of the users")
    else:
        print("Enter a valid difficulty")


def recommend(game):
    print("You might like", game)


main()

