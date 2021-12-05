class Room:
    def __init__(self, name, phone_num, room_no, amount):
        self.name = name
        self.phone_num = phone_num
        self.room_no = room_no
        self.amount = amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __repr__(self):
        return f"{self.room_no}:{self.name}"
