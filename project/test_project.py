from project import (
    create_student,
    student_in_list,
    command_line_input,
    add_to_list,
    eliminate_student,
    Student,
)
import pytest


def test_create():
    student = create_student("Harry Potter")
    # good
    # create an instance and has the value that we introduce it
    assert isinstance(student, Student)
    assert student.name == "Harry Potter"

    student = create_student("Bart J. Simpson")
    # create an instance and has the value that we introduce it
    assert isinstance(student, Student)
    assert student.name == "Bart J. Simpson"

    # bad
    assert create_student("Harry") == None
    assert create_student("1433") == None


# We suposss that the file is created
def test_student_in_list():
    student = create_student("Harry Potter")
    # bad
    assert student_in_list(student) == False  # didn´t add it before

    # good
    add_to_list(student)  # add before
    assert student_in_list(student) == True
    eliminate_student(student)


def test_command_line_input():
    # good
    assert command_line_input(["project.py", "add"]) == "add"
    assert command_line_input(["project.py", "remove"]) == "remove"

    # bad
    with pytest.raises(SystemExit):
        command_line_input(["project.py"])
        command_line_input(["project.py", "o"])
