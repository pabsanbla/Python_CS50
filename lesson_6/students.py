students = []
#Using CSV file
with open("names.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name" : name, "home": home}
        students.append(student)
#Using a nameless function "lambda"
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
