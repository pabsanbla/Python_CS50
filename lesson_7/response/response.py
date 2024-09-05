import validators

if validators.email(input("What´s your email address? ")):
    print("Valid")
else:
    print("Invalid")
