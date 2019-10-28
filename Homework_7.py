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
    def changes_person():
        stat = str(input("Enter status: "))
        num = int("Input number of room: ")
        num_of_night = int(input("Enter night in hotel: "))
        change_person_info = {'stat': stat, 'num': num, 'num_of_night': num_of_night}
        print("Status: {}, Number_of_room: {}, num_of_night: {}", stat, num, num_of_night)
        return change_person_info

    @staticmethod
    def special_offers():
        level_of_room = str(input("Level of comfort in room: "))
        special_offers_info = {'level_of_room': level_of_room}
        print(level_of_room)
        return special_offers_info

    def display_info(self):
        person_info = {'name': Person.name, 'age': Person.age, 'sex': Person.sex}
        print("Some info about person: ", self.name, self.age, self.sex)
        return person_info


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
        special_offers_info = Person.special_offers().update({'spec_discount': spec_discount,
                                                              "meeting_at_arrival": meeting_at_arrival
                                                              })
        print("Discount: {}, Meet: {}", spec_discount, meeting_at_arrival)
        return special_offers_info

    def changes_person(self):
        Person.changes_Person(self)
        visit_purpose = str(input("Enter visit purpose: "))
        income = int(input("Enter money income of person($): "))
        change_person_info = Person.changes_person().update({"visit_purpose": visit_purpose,
                                                             "income": income})
        print("Visit_purpose: {}, Income: {}", visit_purpose, income)
        return change_person_info


class Sportsman(Person):
    def __init__(self, name, age, sex, name_command, sport):
        Person.__init__(self, name, age, sex)
        self.name_command = name_command
        self.sport = sport

    def display_info(self):
        Person.display_info(self)
        print("Command: ", self.name_command, self.sport)

    def special_offers(self):
        Person.special_offers(self)
        rent_sport_places = str(input("Place of sport_place: "))
        special_offers_info = Person.special_offers().update({"rent_sport_places": rent_sport_places})
        print("Rent: {}", rent_sport_places)
        return special_offers_info

    def changes_person(self):
        Person.changes_Person(self)
        inventory = str(input("Enter inventory: "))
        change_person_info = Person.changes_person().update({"inventory": inventory})
        print("Inventory by sport: {}", inventory)
        return change_person_info


class Hotel:
    def __init__(self, room, name_of_hotel, level, parking):
        self.room = room
        self.name_of_hotel = name_of_hotel
        self.level = level
        self.parking = parking

    prices_room = {"room_1": 100,
                   "room_2": 110,
                   "room_3": 150,
                   "room_4": 200}

    facilities_room = {"room_1": "hot_tube",
                       "room_2": "mini_bar",
                       "room_3": "mini_bar",
                       "room_4": "massage_room"
                       }

    @staticmethod
    def add_new_room(prices_room):
        name = str(input("Enter name of room: "))
        base_price = int(input("Enter price: "))
        new_room = {name: base_price}
        prices_room.update(new_room)
        print("New room: {}, price: {}", name, base_price)

    # change base price of room
    def change_base_price(self):
        room = str(input("Enter name of room: "))
        price = int(input("Enter new price: "))

        for key in self.prices_room.keys():
            if key[:] == room:
                self.prices_room.update({key: price})
        return self.prices_room

    # def rooms(self, number_of_room, vip_rooms, max_rent, ):

    def change_facilities(self):
        name = str(input("Enter name of room: "))
        facilities = int(input("Enter facilities: "))

        for key in self.facilities_room.keys():
            if key[:] == name:
                self.prices_room.update({key: facilities})
        return self.facilities_room

    def change_season_price(self):
        season = int(input("Enter a season: 1-summer, 2-autumn, 3-winter, 4-spring: "))

        def changes(seas):
            if seas == 1:
                for key in self.prices_room.keys():
                    self.prices_room.update({key: self.prices_room[key] * 1.4})
                return self.prices_room
            if seas == 2:
                for key in self.prices_room.keys():
                    self.prices_room.update({key: self.prices_room[key] * 1.3})
                return self.prices_room
            if seas == 3:
                for key in self.prices_room.keys():
                    self.prices_room.update({key: self.prices_room[key] * 1.2})
                return self.prices_room
            if seas == 4:
                for key in self.prices_room.keys():
                    self.prices_room.update({key: self.prices_room[key] * 1.1})
                return self.prices_room

        return changes(season)

    def display_info(self):
        hotel_info = {'Room': Hotel.room,
                      'name_of_hotel': Hotel.name_of_hotel,
                      'level': Hotel.level}

        print("Some info about person: ", self.room, self.name_of_hotel, self.level)
        return hotel_info


class Booking(Hotel, Person):

    @staticmethod
    def booking_room():
        facilities = Hotel.facilities_room["facilities_room"]
        # data_booking = Person.changes_person()
        nights = Person.changes_person['num_of_night']
        room = Person.changes_person["room"]

        for key in Hotel.prices_room.keys():
            if str(room) == key[:]:
                end_price = Hotel.prices_room[key] * nights
                print("Price: {}", end_price)
                return "Total: {end_price} $".format(end_price=end_price)

        for key in Hotel.facilities_room.keys():
            if str(facilities) == key[:]:
                fac = Hotel.facilities_room[key]
                print("Facilities: {}", fac)
                return "Facilities in room: {fac} $".format(fac=fac)

    @staticmethod
    def print_order():
        res = Booking.booking_room()
        result = "{} you order room: {} for " \
                 "{} nights with {} facilities.".format(Person.display_info['name'],
                                                        Hotel.display_info['room'],
                                                        Person.changes_person().change_person_info['num_of_night'])

        res += result
        return res


age = int(input("Enter age: "))
name = str(input("Enter name: "))
name_command = str(input("Enter name_command: "))
sex = str(input("Enter sex: "))
sport = str(input("Enter kind of sport: "))

s = Sportsman(age, name, name_command, sex, sport)
print(dir(s))

h = Hotel()
print(dir(h))

b = Booking()
print(dir(b))

n = int(input("Enter some var[1-4]: "))
print(h.change_season_price(n))
print(b.print_order())
