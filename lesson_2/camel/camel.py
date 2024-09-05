def main():
    camel = input("camelCase: ")
    for letter in camel:
        if letter.islower():
            print(letter, end="")
        else:
            print("_" + letter.lower(), end="")

    print()

main()
