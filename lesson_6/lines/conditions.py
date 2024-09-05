import sys

def main():
    conditions(".txt")

def conditions(archive):
    #reading conditions
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(archive):
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
