prices = {
    "BAJA TACO": 4.25,
    "BURRITO": 7.50,
    "BOWL": 8.50,
    "NACHOS": 11.00,
    "QUESADILLA": 8.50,
    "SUPER BURRITO": 8.50,
    "SUPER QUESADILLA": 9.50,
    "TACO": 3.00,
    "TORTILLA SALAD": 8.00
}

def main():
    bill = 0
    while True:
        try:
            key = input("Item: ").upper()
            if key in prices:
                bill = bill + prices[key]
                print(f"Total: ${bill:.2f}")
        except KeyError:
            pass
        except EOFError:
            print()
            break


main()
