import emoji

def main():
    message = input("Input: ")
    print("Output: " + emoji.emojize(message, language="alias"))


main()
