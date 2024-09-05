class Student:
    #method to get the attributes
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    #method to use print
    def __str__(self):
        return f"{self.name} from {self.house}"
    #own function
    def charm(self):
        match self.patronus:
            case "Stag":
                return ":)"
            case "Otter":
                return ":<"
            case "jack Russell terrier":
                return ":("
            case _:
                return "/"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) #constructor


if __name__ == "__main__":
    main()
