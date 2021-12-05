import csv
import json

list_room = []
with open('availability.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        list_room.append(r)


class Hotel:
    def __init__(self):
        self.room = []

    def insert(self, room):
        user_data = {
            room.room_no: {"name": room.name,
                           "room": room.room_no
                           }
        }
        try:
            with open("information.json", "r") as data_user:
                user = json.load(data_user)
        except FileNotFoundError:
            with open("information.json", "w") as data_user:
                json.dump(user_data, data_user, indent=4)
        else:
            user.update(user_data)
            with open("information.json", "w") as data_user:
                json.dump(user, data_user, indent=4)
        finally:
            self.room.append(room)

    def check(self, room):
        list_num = []
        list_reserved = []
        for i in list_room:
            list_num.append(i['number'])
        if not room in list_num:
            print(f'Room {room} is invalid.')
        for i in list_room:
            if room == i['number']:
                if i['status'] == 'yes':
                    print(f'You reserved room number {room}.')
                    list_reserved.append(i['number'])
                    return True
                else:
                    print(f'Room {room} is unavailable.')
