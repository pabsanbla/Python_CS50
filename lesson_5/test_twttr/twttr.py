def main():
    print(shorten(input("Input: ")))


def shorten(word):
    vocales = "aeiouAEIOU"
    for letter in word:
        if letter in vocales:
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
