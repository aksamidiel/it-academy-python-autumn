class Person:
    def __init__(self):
        self.name = str(input("Enter name: "))
        self.age = int(input("Enter age: "))
        self.sex = str(input("Enter sex: "))
        self.num = str(input("Input number of room: "))
        self.num_of_night = int(input("Enter night in hotel: "))
        self.person_info = {'name': self.name, 'age': self.age, 'sex': self.sex,
                            'num': self.num, 'num_of_night': self.num_of_night}

    def base_info(self):
        return self.person_info

class Sportsman(Person):
    def __init__(self):
        Person.__init__(self)
        self.name_command = str(input('name_command: '))
        self.kind_sport = str(input('kind_sport: '))
        self.rent_sport_places = str(input("Place of sport_place: "))
        self.inventory = str(input("Enter inventory: "))

        self.spec_sport_info = {'name_command': self.name_command, 'kind_sport': self.kind_sport,
                                'rent': self.rent_sport_places, 'inventory': self.inventory}

    def display_sportsman_info(self):
        return self.person_info

    def display_spec_sportsman_info(self):
        return self.spec_sport_info

s = Sportsman()
print(s.display_sportsman_info())
print(s.display_spec_sportsman_info())