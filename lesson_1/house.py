#Use of match = switch
name = input("What´s your name? ")
#You can use | as or
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
