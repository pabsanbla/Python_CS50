class Student:
    #method to get the attributes
    def __init__(self, name, house):
        self.name = name
        self.house = house
    #method to use print
    def __str__(self):
        return f"{self.name} from {self.house}"
    #To create protection
    #Getter
    @property
    def name(self):
        return self._name
    #Setter
    @name.setter
    def name(self, name):
        #You only neeed checking error here
        if not name:
            raise ValueError("Missing name")
        self._name = name
    #Getter
    @property
    def house(self):
        return self._house
    #Setter
    @house.setter
    def house(self, house):
        #You only neeed checking error here
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) #constructor


if __name__ == "__main__":
    main()
