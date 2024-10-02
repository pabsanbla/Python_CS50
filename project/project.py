import sys
import re
import csv
from students import Student, Hat


def main():
    decision(command_line_input(sys.argv))


# this function just expect us to introduce one of the two possible arguments
# in other case it exits the program
def command_line_input(arg):
    options = ["add", "remove"]
    if len(arg) != 2:
        sys.exit("Introduce 'remove' or 'add' as an argument")
    elif arg[1] not in options:
        sys.exit("Invalid input")
    else:
        return arg[1]


# this function creates a students of howarts
def create_student(name):
    if re.fullmatch(r"^[A-Z][a-z]+(?: ([A-Z]\.? )?[A-Z][a-z]+)+$", name) != None:
        student = Student(name)  # create the student
        Hat.sort(student)  # assign house
        return student
    else:
        print("Please introduce a valid name")
        return None


# We read to know if the student it´s in the archive
def student_in_list(student):
    try:
        with open("archive.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == student.name:
                    return True
        return False
    except FileNotFoundError:
        # create the file if did not exists
        open("archive.csv", "w")
        return False


# this function adds the student in the database (.csv)
def add_to_list(student):
    dict_student = {"name": student.name, "house": student.house}
    with open("archive.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"])
        # write the header in case we have a empty file
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(dict_student)


# this function eliminates dthe student in the data base (.csv)
def eliminate_student(student):
    students = []
    # copy in a list
    with open("archive.csv", "r") as file:
        reader = csv.DictReader(file)
        students = [row for row in reader]
    # modify the list
    modified_students = [row for row in students if row["name"] != student.name]
    # write the new list
    with open("archive.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(modified_students)


# the activity that main does
def decision(action):
    student = None
    match action:
        case "add":
            while student == None:
                student = create_student(input("What´s the students name? ").strip())
            if not student_in_list(student):
                add_to_list(student)
            else:
                sys.exit("The student is already in the system")
        case "remove":
            while student == None:
                student = create_student(input("What´s the students name? ").strip())
            if student_in_list(student):
                eliminate_student(student)
            else:
                sys.exit("There´s not such a student in the system")


if __name__ == "__main__":
    main()
