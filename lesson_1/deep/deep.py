def main():
    value = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if value == "42" or value == "forty-two" or value == "forty two":
        print("Yes")
    else:
        print("No")


main()
