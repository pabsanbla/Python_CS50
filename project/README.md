# Howarts archive file
## Video Demo:  <URL HERE>
## Description:
The program is responsible for automatically updating the Hogwarts student file. To do this, the modules `sys`, `re` and `csv` have been used, as well as a module called `students`, which contains the classes `Student` and `Hat`, which will be applied in the code. For the explanation, we will go step by step through the functions and then explain the general operation of the program after having deciphered its blocks:
- `command_line_input(arg)`: This function receives `sys.argv` as an argument and continues with the program if `project.py add` or `project.py remove` is entered on the command line. In any other case, the program does not continue and exits. If the command is entered correctly, the function returns the value of the second argument, that is, `add` or `remove`.
- `create_student(name)`: This function receives as an argument the name of the previously instantiated `Student` object and checks that the name entered is valid. If the name corresponds to any of the formats, a `Student` object is instantiated and `Hat.sorted(student)` is used to assign a value to the `house` attribute, and then return it. Otherwise, `None` is returned and a message is displayed that the name is not valid. It should be noted that the program is sensitive to font size, so names like `harry potter` are not valid. The formats included are the following:
> **First name last name**

> **First name initial middle name(.) last name** *The dot is optional*

- `student_in_list(student)`: This function checks that the student it receives as an argument (*Student object*) is not in the database, returning `True` if positive and `False` if negative. It also generates the `.csv` file in case it has not been created yet, returning `False` in this case as well.
- `add_to_list(student)`: This function adds the student received as argument (*Student Object*) in `file.csv`.
- `eliminate_student(student)`: This function removes the student received as argument (*Student Object*) from `file.csv`.
- `decision(action)`: This function adds or removes a student depending on the `action` (*add or remove*). In both cases, it asks for the student's name until a valid format is entered (`create_student(name)`) and once this is done, it checks if the student is on the list (`student_in_list(student)`) generating the following casuistry:
1. The student is there and wants to be added: The program exits, with the reason being displayed on the screen.
2. The student is there and wants to be deleted: The student is deleted from the file `archivo.csv`.
3. The student is not there and wants to be added: The student is added to the file `archivo.csv`.
4. The student is not there and wants to be deleted: The program exits, with the reason being displayed on the screen.
### students.py
- **Student Class**: This class it´s just use to create student´s objects that has two attributes, `name` and `house`. The first one is assign in the `__init__` method and the house is decided by the other class.
- **Hat Class**: This claas only has one method called `sorted` that decide to what house the sudent belong randomly between the four possible options.
In summary, the program works when the commands `add` or `remove` are entered, and then it asks for the student's name, which must be entered in a certain format; that will be added or deleted from the Hogwarts file as specified with the commands. If this cannot be done, as explained in the case study, you will be notified of the reason at the same time that you exit the program.

