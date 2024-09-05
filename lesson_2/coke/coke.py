def main():
    total = 50
    amount = 0
    coin = 0
    while amount < total:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount = amount + coin
        if amount < total:
            print("Amount Due:", total - amount)

    print("Change Owed:",  amount - total)


main()
