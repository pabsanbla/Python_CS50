def main():
    percentage = get_percentage("Fraction: ")
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage:.0f}%")


def get_percentage(prompt):
    while True:
        try:
           x, y = input(prompt).split("/")
           return (int(x) / int(y)) * 100
        except (ValueError, ZeroDivisionError):
            pass


main()
