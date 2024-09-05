def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if beggining(s) and number_of_characters(s) and end_numbers(s) and no_special_characters(s):
        return True
    else:
        return False


def beggining(s):
    for letter in s[0:2]:
        if letter.isdigit():
            return False
    return True


def number_of_characters(s):
    lenght = len(s)
    if lenght >= 2 and lenght <= 6:
        return True
    return False


def end_numbers(s):
        for zero in s:
            if zero.isdigit():
                if zero == "0":
                    return False
                else:
                    break
        i = len(s)
        if s[i-1].isdigit() and not s[i-2].isdigit():
            return False

        return True


def no_special_characters(s):
    for caracter in s:
        if not caracter.isalnum():
            return False
    return True


if __name__ == "__main__":
    main()
