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


# We suposse that the file is created in this test 
def test_student_in_list():
    student = create_student("Harry Potter")
    # good
    add_to_list(student)  # add before
    assert student_in_list(student) == True
    eliminate_student(student)
    # bad
    assert student_in_list(student) == False  # eliminate before



def test_command_line_input():
    # good
    assert command_line_input(["project.py", "add"]) == "add"
    assert command_line_input(["project.py", "remove"]) == "remove"

    # bad
    with pytest.raises(SystemExit):
        command_line_input(["project.py"])
        command_line_input(["project.py", "o"])
