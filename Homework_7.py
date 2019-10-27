# Create simulator from real life.
# This can be booking room in hotel, visit to casino, visit to bar.
# Create 3-4 objects, that can describe situation.
# Objects should contain attributes and methods to simulate some use cases.
# Completed program should print object states, it actions (methods) and objects interaction.

def create_Person():
    name = str(input("Enter name of person: "))
    age = int(input("Enter age of person: "))
    sex = str(input("Enter sex of person: "))

    return name, age, sex


class Person(create_Person()):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @staticmethod
    def changes_Person():
        stat = str(input("Enter status: "))
        num = int("Input number of room: ")
        num_of_night = int(input("Enter night in hotel: "))
        income = int(input("Enter money income of person($): "))
        visit_purpose = str(input("Enter visit purpose: "))

        return stat, num, num_of_night, income, visit_purpose

    @staticmethod
    def special_offers():
        level_of_room = str(input("Level of comfort in room: "))
        spec_discount = int(input("Enter discount: "))

        return level_of_room, spec_discount

    print("Parameters of {} ".format())





class Buisnesman(Person):
    def __init__(self, ):


