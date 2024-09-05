def main():
    n = int(input("What´s n? "))
    for s in sheep(n):
        print(s)

#yield is useful due to the amount of data you have to manipulate
def sheep(n):
    for i in range(n):
        yield "s" * i


if __name__ == "__main__":
    main()
