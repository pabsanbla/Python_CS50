import sys
from conditions import conditions


def main():
    conditions(".py")
    #If it´s well written
    empty_string = ""
    lines_of_code = 0
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                #if it´s not a commentary or empty
                if line.lstrip().startswith("#") or line.lstrip() == empty_string:
                    pass
                else:
                    lines_of_code += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(lines_of_code)


if __name__ == "__main__":
    main()
