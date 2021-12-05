from turtle import Screen
import turtle
from stage import Stage

stage = Stage()
screen = Screen()
screen.setup(1300, 731)
screen.listen()

# image
screen = turtle.Screen()
picture = "firstpage.gif"
screen.addshape(picture)
stage.image()
screen.title("BookingLooking.com")

username = screen.textinput("welcome to Booking Looking", "Please enter your name")
print(f'Welcome! {username}')

screen.onclick(stage.check_click)
turtle.done()
