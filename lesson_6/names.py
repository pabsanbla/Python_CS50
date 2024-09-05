name = input("What´s your name? ")
#Write in a file without overwritting
#Using "with" we close the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

