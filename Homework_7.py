# Create simulator from real life.
# This can be booking room in hotel, visit to casino, visit to bar.
# Create 3-4 objects, that can describe situation.
# Objects should contain attributes and methods to simulate some use cases.
# Completed program should print object states, it actions (methods) and objects interaction.

class Person():
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


class Buisnesman(Person):
    def __init__(self):
        Person.__init__(self)

        self.company = str(input("Enter company: "))
        self.meeting_at_arrival = str(input("Place of met: "))
        self.special_requirements = str(input("Write special require: "))
        self.special_offers_info = {'company': self.company, 'met': self.meeting_at_arrival,
                                    'sp_req': self.special_requirements}

        self.visit_purpose = str(input("Enter visit purpose: "))
        self.income = int(input("Enter money income of person($): "))
        self.change_person_info = {'visit': self.visit_purpose, 'income': self.income}

    def display_buisnesman_info(self):
        return self.person_info

    def display_spec_info(self):
        return self.special_offers_info

    def display_change_info(self):
        return self.change_person_info


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


class Hotel:
    def __init__(self):
        self.name_of_hotel = str(input("Hotel name: "))
        self.room = str(input('Input number of room: '))
        self.level = int(input('Level of hotel: '))
      #  self.season = int(input("Enter a season: 1-summer, 2-autumn, 3-winter, 4-spring: "))

    prices_room = {"room_1": 100,
                   "room_2": 110,
                   "room_3": 150,
                   "room_4": 200}

    facilities_room = {"room_1": "hot_tube",
                       "room_2": "mini_bar",
                       "room_3": "mini_bar",
                       "room_4": "massage_room"
                       }

    def add_new_room(self, prices_room):
        name = str(input("Enter name of room: "))
        base_price = int(input("Enter price: "))
        new_room = {name: base_price}
        prices_room.update(new_room)
        print("New room: {}, price: {}", name, base_price)

    # change base price of room
    def update_base_price(self):
        room = str(input("Enter name of room: "))
        price = int(input("Enter new price: "))

        for key in self.prices_room.keys():
            if key[-3:] == room:
                self.prices_room.update({key: price})
        return self.prices_room

    def update_facilities(self):
        name = str(input("Enter name of room: "))
        facilities = int(input("Enter facilities: "))

        for key in self.facilities_room.keys():
            if key[-3:] == name:
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
                      'level': Hotel.level,
                      'parking': Hotel.parking
                      }

        # print("Some info about person: ", self.room, self.name_of_hotel, self.level, self.parking)
        return hotel_info


class Booking(Hotel, Person):

    def booking_room(self):
        facilities = self.get_info["facilities_room"]
        nights = self.get_info['num_of_night']
        room = self.get_info["room"]

        for key in Hotel.prices_room.keys():
            if str(room) == key[-3:]:
                end_price = Hotel.prices_room[key] * nights
                print("Price: {}", end_price)
                return "Total: {end_price} $".format(end_price=end_price)

        for key in Hotel.facilities_room.keys():
            if str(facilities) == key[-3:]:
                fac = Hotel.facilities_room[key]
                print("Facilities: {}", fac)
                return "Facilities in room: {fac} $".format(fac=fac)

    def print_order(self):
        res = Booking.booking_room(self)
        result = "{} you order room: {} with {} facilities".format(self.get_info['name'],
                                                                   self.get_info['room'],
                                                                   self.get_info['facilities'])

        res += result
        return res


s = Sportsman()
print(dir(s))
h = Hotel()
print(h.change_season_price())
b1 = Booking()

print(b1.print_order())
