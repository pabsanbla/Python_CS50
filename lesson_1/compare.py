#Example of using conditionals
x = int(input("What´s x? "))
y = int(input("What´s y? "))
#elif avoids processing the rest of the code, in a nutshell, faster
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
#elif x == y: we don´t need it, cuase there´s no other possibility
else:
    print("x is equal than y")
