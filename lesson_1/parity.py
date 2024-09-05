#Kind of numbers Even or odd
def main():
    x = int(input("What´s x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#Use the reminder operator and boolean values
def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    #reduced version use in python
    #return True if n % 2 == 0 else False
    #tightness version, return and actual boolean result
    return n % 2 == 0


main()
