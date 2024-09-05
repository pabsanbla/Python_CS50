#Example of using and
score = int(input("Score: "))

#a way of using and
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#Reduced form
#Be careful, if you don´t use mutal exclusive questions it doesn´t work
if 90 >= score:
    print("Grade: A")
elif 80 >= score:
    print("Grade: B")
elif 70 >= score:
    print("Grade: C")
elif 60 >= score:
    print("Grade: D")
else:
    print("Grade: F")

