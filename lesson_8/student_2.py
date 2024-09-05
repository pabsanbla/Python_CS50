class Student:
    #method to get the attributes
    def __init__(self, name, house):
        self.name = name
        self.house = house
    #method to use print
    def __str__(self):
        return f"{self.name} from {self.house}"
    #class method to create an object
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) #constructor

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
