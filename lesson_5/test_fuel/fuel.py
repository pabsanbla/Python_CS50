import sys

def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))


def convert(fraction):
        x, y = fraction.split("/")
        percentage = (int(x) / int(y)) * 100
        return percentage

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()

