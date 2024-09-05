import sys
import csv


def main():
    conditions(".csv")
    students = []
    fields = ["first", "last", "house"]
    #read
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row["name"].rsplit(", ")
                students.append({"first": first_name,
                                 "last": last_name,
                                 "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    #write
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)


def conditions(archive):
    #reading conditions
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(archive):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
