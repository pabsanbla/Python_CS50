#If there´s an error it runs what´s in except, if there´s not it runs what in else
try:
    x = int(input("What´s is x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
