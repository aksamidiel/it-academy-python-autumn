"""Create simulator from real life.
This can be booking room in hotel, visit to casino, visit to bar.
Create 3-4 objects, that can describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states,
it actions (methods) and objects interaction."""


class Person(object):
    def __init__(self):
        self.name = str(input("Enter name: "))
        self.age = int(input("Enter age: "))
        self.sex = str(input("Enter sex: "))

    def change_room(self):
        self.name_room = str(input("Input name of room: "))
        self.num_of_night = int(input("Enter night in hotel: "))

    def base_info(self):
        self.person_info = {'name': self.name,
                            'age': self.age, 'sex': self.sex,
                            'name_room': self.name_room,
                            'num_of_night': self.num_of_night}

        return self.person_info


class Buisnesman(Person):
    def __init__(self):
        Person.__init__(self)
        self.company = str(input("Enter company: "))
        self.meeting_at_arrival = str(input("Place of met: "))
        self.special_requirements = str(input("Write special require: "))
        self.special_offers_info = {'company': self.company,
                                    'met': self.meeting_at_arrival,
                                    'sp_req': self.special_requirements}
        Person.change_room(self)

    def get_spec_info(self):
        return self.special_offers_info

    def base_info(self):
        self.person_info = {'name': self.name,
                            'age': self.age,
                            'sex': self.sex,
                            'name_room': self.name_room,
                            'num_of_night': self.num_of_night}
        return self.person_info


class Sportsman(Person):
    def __init__(self):
        Person.__init__(self)
        self.rent_sport_places = str(input("Place of sport_place: "))
        self.inventory = str(input("Enter inventory: "))

        self.spec_offers_info = {'rent': self.rent_sport_places,
                                 'inventory': self.inventory}
        Person.change_room(self)

    def base_info(self):
        self.person_info = {'name': self.name,
                            'age': self.age,
                            'sex': self.sex,
                            'name_room': self.name_room,
                            'num_of_night': self.num_of_night}
        return self.person_info

    def get_spec_info(self):
        return self.spec_offers_info


class Hotel(object):
    def __init__(self):
        self.name = str(input("Enter name of hotel: "))
        self.rang = int(input("Enter stars of hotel: "))
        self.base_info = {'Name': self.name, 'Rang': self.rang}

    prices_room = {"room_1": 100,
                   "room_2": 110,
                   "room_3": 150,
                   "room_4": 200,
                   "room_5": 115,
                   "room_6": 110,
                   "room_7": 150,
                   "room_8": 140
                   }

    def info_room(self):
        return self.prices_room

    def select_room(self, prices_room):
        room = str(input("Select the room: "))
        select_room = prices_room.get(room, "Unknown_room")
        print("Select {}, price: {}".format(room, select_room))

    def add_new_room(self, prices_room):
        name = str(input("Enter name of room: "))
        base_price = int(input("Enter price: "))
        new_room = {name: base_price}
        prices_room.update(new_room)
        print("New room: {}, price: {}".format(name, base_price))
        return prices_room

    # change base price of room
    def update_base_price(self):
        room = str(input("Enter name of room: "))
        price = int(input("Enter new price: "))

        for key in self.prices_room.keys():
            if key == room:
                self.prices_room.update({key: price})
        return self.prices_room

    def change_season_price(self):
        season = int(input("Enter a season: 1-summer, "
                           "2-autumn, 3-winter, 4-spring: "))

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
        return self.base_info


def create_hotel():
    h = Hotel()
    sel = h.change_season_price()
    print(sel)
    op = str(input("1-create new room 2-update room"))

    def operation():
        if op == '1':
            res = h.add_new_room(h.info_room())
        elif op == '2':
            res = h.update_base_price()
        else:
            print("No operation")
            res = h.info_room()

        return res

    print(operation())
    return operation()


def create_lodger(lodger, hotel):
    if lodger == '1':
        b = Buisnesman()
        if b.base_info()['name_room'] in hotel.keys():
            our_cost = hotel.get(b.base_info()['name_room'],
                                 "None") * b.base_info()['num_of_night']

            print("Guest {} in {} cost {}".
                  format(b.base_info()['name'],
                         b.base_info()['name_room'],
                         our_cost))
        # print(b.get_spec_info())

    elif lodger == '2':
        b = Sportsman()
        if b.base_info()['name_room'] in hotel.keys():
            our_cost = hotel.get(b.base_info()['name_room'],
                                 "None") * b.base_info()['num_of_night']

            print("Guest {} in {} cost {}".
                  format(b.base_info()['name'],
                         b.base_info()['name_room'],
                         our_cost))
        # print(b.base_info())
        # print(b.get_spec_info())

    else:
        b = Person()
        print(b.base_info())


class Booking(object):
    print("Create Hotel: ")
    h = create_hotel()
    print("Create lodger: ")
    lodger = input("Enter lodger: 1->Businessman 2->Sportsman : ")
    create_lodger(lodger, h)


b = Booking()
