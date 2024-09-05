def main():
    message = input("Input: ")
    vocales = "aeiouAEIOU"
    for letter in message:
        if letter in vocales:
            message = message.replace(letter, "")

    print(message)


main()
