# Create simulator from real life.
# This can be booking room in hotel, visit to casino, visit to bar.
# Create 3-4 objects, that can describe situation.
# Objects should contain attributes and methods to simulate some use cases.
# Completed program should print object states, it actions (methods) and objects interaction.

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @staticmethod
    def changes_Person():
        stat = str(input("Enter status: "))
        num = int("Input number of room: ")
        num_of_night = int(input("Enter night in hotel: "))

        print("Status: {}, Number_of_room: {}, num_of_night: {}", stat, num, num_of_night)

    @staticmethod
    def special_offers():
        level_of_room = str(input("Level of comfort in room: "))
        print(level_of_room)

    def display_info(self):
        print("Some info about person: ", self.name, self.age, self.sex)


class Buisnesman(Person):
    def __init__(self, name, age, sex, company):
        Person.__init__(self, name, age, sex)
        self.company = company

    def display_info(self):
        Person.display_info(self)
        print("Company: ", self.company)

    def special_offers(self):
        Person.special_offers(self)
        spec_discount = int(input("Enter discount: "))
        meeting_at_arrival = str(input("Place of met: "))
        print("Discount: {}, Meet: {}", spec_discount, meeting_at_arrival)

    def changes_Person(self):
        Person.changes_Person(self)
        visit_purpose = str(input("Enter visit purpose: "))
        income = int(input("Enter money income of person($): "))
        print("Visit_purpose: {}, Income: {}", visit_purpose, income)
