def main():
    my_list = {}
    while True:
        try:
            product = input().upper()
            my_list[product] += 1
        except KeyError:
            my_list[product] = 1
        except EOFError:
            ordered_list = {product: my_list[product] for product in sorted(my_list)}
            for product in ordered_list:
                print(ordered_list[product], product)
            break


main()

