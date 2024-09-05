import random


class Student:
    # init method
    def __init__(self, name):
        self._name = name
        self._house = "Muggle"  # this never appears

    # method to use print
    def __str__(self):
        return f"{self.name} from {self.house}"

    # To create protection
    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        self._house = house


class Hat:
    # houses of Howarts
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, student):
        student.house = random.choice(cls.houses)
