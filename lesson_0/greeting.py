def greet(input):
   #This is an example of a side effect
    if "hello" in input:
        print("hello,there")
    else:
        print("I´m not sure what you mean")
    #This is an example of a return value
    if "hello" in input:
        return "hello,there"
    else:
        return "I´m not sure what you mean"


greeting = greet("hello, computer")
print(greeting + " Pablo")
