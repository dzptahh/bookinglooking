from turtle import Turtle, Screen
import sys
from hotel import Hotel
from room import Room


class Stage:
    def __init__(self):
        self.hotel = Hotel()
        self.painter = Turtle()
        self.painter_bg = Turtle()
        self.rooms = Turtle()
        self.screen = Screen()
        self.info = {}

    def image(self):
        self.painter.shape("firstpage.gif")

    # def title_background(self):
    #     self.painter_bg.hideturtle()
    #     self.painter_bg.penup()
    #     turtle.bgcolor("beige")
    #     self.painter_bg.goto(-800 / 3, 320)
    #     self.painter_bg.write("welcome to Booking Looking", font=("Times New Roman ", 45, "normal"))

    # def line_(self):
    #     self.painter_bg.hideturtle()
    #     self.painter_bg.speed(0)
    #     self.painter_bg.fillcolor("black")
    #     self.painter_bg.begin_fill()
    #     self.painter_bg.goto(-800, 300)
    #     self.painter_bg.pendown()
    #     self.painter_bg.goto(800, 300)

    def click(self, x, y):
        print(x, y)

    def check_click(self, x, y):
        if 119 <= x <= 354 and -168 <= y <= -110:
            self.painter_bg.clear()
            self.painter.hideturtle()
            self.page_2()
            self.screen.listen()
            self.screen.onclick(self.check_click2)

    def page_2(self):
        self.screen.setup(1300, 731)
        image = "nextpage.gif"
        self.screen.addshape(image)
        self.rooms.shape(image)

    def check_click2(self, x, y):
        self.painter_bg.hideturtle()
        self.painter_bg.speed(0)
        self.painter_bg.clear()
        if 117 <= x <= 479 and 189 >= y >= 133:
            name = self.screen.textinput('Information', 'Enter your name')
            self.info.update({"name": name})
        elif 115 <= x <= 478 and 55 <= y <= 117:
            phone = self.screen.textinput('Information', 'Enter your phone number')
            self.info.update({"phone": phone})
        elif 116 <= x <= 479 and -14 <= y <= 42:
            people = self.screen.textinput('Information', 'Enter amount of people')
            self.info.update({"people": people})
        elif 114 <= x <= 478 and -177 <= y <= -74:
            room = self.screen.textinput('Information', 'Enter room number')
            self.info.update({"room": room})
        elif -599 <= x <= -405 and -353 <= y <= -320:
            self.page_3()
            self.screen.listen()
            self.screen.onclick(self.end)
            self.show_info()
        self.combine()

    def page_3(self):
        self.painter.hideturtle()
        self.painter_bg.hideturtle()
        self.screen.setup(1300, 731)
        image = "lastpage.gif"
        self.screen.addshape(image)
        self.rooms.shape(image)

    def end(self, x, y):
        if -599 <= x <= -405 and -353 <= y <= -320:
            self.screen.exitonclick()

    def show_info(self):
        if len(self.hotel.room) != 0:
            self.painter_bg.penup()
            self.painter_bg.color('#7a72bd')
            self.painter_bg.goto(-479, 36)
            self.painter_bg.write(f"{self.hotel.room[0].name} reserved room(s): ", False, "left",
                                  ("Mali", 28, "normal"))
            for i in range(len(self.hotel.room)):
                if i <= 4:
                    self.painter_bg.goto(-479 + 100 * i, 1)
                    self.painter_bg.write(self.hotel.room[i].room_no, False, "left", ("Mali", 28, "normal"))
                elif i <= 7:
                    self.painter_bg.goto(-479 + 100 * i - 500, -50)
                    self.painter_bg.write(self.hotel.room[i].room_no, False, "left", ("Mali", 28, "normal"))

            self.painter_bg.goto(-479, -112)
            self.painter_bg.write("Information: ", False, "left", ("Mali", 28, "normal"))
            self.painter_bg.goto(-479, -180)
            self.painter_bg.write(
                f"phone number: {self.hotel.room[0].phone_num} \namount of people: {self.hotel.room[0].amount}", False,
                "left", ("Mali", 28, "normal"))
        else:
            sys.exit()

    def combine(self):
        try:
            if self.hotel.check(self.info["room"]):
                self.hotel.insert(
                    Room(self.info["name"], self.info["phone"], self.info["room"], self.info["people"]))
                print("successfully reserved")
                self.painter_bg.penup()
                self.painter_bg.color('#fee992')
                self.painter_bg.goto(180, -240)
                self.painter_bg.write("already  reserved", False, "left",
                                      ("Mali", 28, "normal"))
            else:
                self.painter_bg.penup()
                self.painter_bg.hideturtle()
                self.painter_bg.speed(0)
                self.painter_bg.color('red')
                self.painter_bg.goto(205, -240)
                self.painter_bg.write("Invalid room", False, "left",
                                      ("Mali", 28, "normal"))
        except KeyError:
            print(self.info)
        else:
            self.info.pop("room")
            print(self.hotel.room)
