import sys
import csv
from tabulate import tabulate


def main():
    conditions(".csv")
    pizzas = []
    pizza_type = sys.argv[1].removesuffix(".csv").capitalize()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append({f"{pizza_type} Pizza": row[f"{pizza_type} Pizza"], "Small": row["Small"], "Large": row["Large"]})
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(pizzas, headers="keys", tablefmt="grid"))


def conditions(archive):
    #reading conditions
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(archive):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
