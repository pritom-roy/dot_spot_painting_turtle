import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)
swa = Turtle()
screen = Screen()

color = [(188, 19, 46), (243, 232, 66), (251, 230, 236), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187), (87, 24, 56), (183, 185, 210), (115, 119, 152), (91, 24, 21)]

swa.penup()
b = -250
swa.setposition(-220, b)
swa.pendown()

swa.speed("fastest")
again = True
cnt = 0
swa.hideturtle()
while again:
    for key in range(10):
        swa.fillcolor(random.choice(color))

        swa.begin_fill()
        swa.circle(10)
        swa.penup()
        swa.forward(50)
        swa.pendown()
        swa.end_fill()
        cnt += 1
    if cnt == 100:
        break
    swa.penup()
    b += 50
    swa.setposition(-220, b)
    swa.penup()
























# rgb_color = []
# color = colorgram.extract("image.jpg", 142)
# for key in color:
#     r = key.rgb.r
#     g = key.rgb.g
#     b = key.rgb.b
#     r_color = (r, g, b)
#     rgb_color.append(r_color)
#
# print(rgb_color)

# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     color = (r, g, b)
#     return color
#
#
# swa.home()
# # swa.circle(100)
# # swa.left(5)
# # swa.circle(100)
# swa.speed("fastest")
# for _ in range(72):
#     swa.circle(100)
#     swa.left(5)
#     swa.color(random_color())

# # color = ["red", "yellow", "purple", "black", "green", "blue", "cyan", "yellow"]
# swa.shape("arrow")
# # swa.color("red")
# swa.hideturtle()
# swa.penup()
# swa.goto(-50, 50)
# swa.showturtle()
# swa.pendown()
#
# # swa.width(10)
# # swa.speed(100)
# # swa.forward(100)
#
# angle = [90, 180, 270, 360]
#
# for _ in range(100):
#     swa.width(10)
#     swa.speed("fastest")
#     swa.forward(30)
#     swa.left(random.choice(angle))
#     swa.color(random_color())

# for _ in range(3):
#     swa.forward(100)
#     swa.right(120)
# theColor = random.choice(color)
# swa.color(theColor)
#
# for _ in range(4):
#     swa.forward(100)
#     swa.right(90)
# theColor = random.choice(color)
# swa.color(theColor)
#
# for _ in range(5):
#     swa.forward(100)
#     swa.right(72)
# theColor = random.choice(color)
# swa.color(theColor)
#
# for _ in range(6):
#     swa.forward(100)
#     swa.right(60)
# theColor = random.choice(color)
# swa.color(theColor)
#
# for _ in range(7):
#     swa.forward(100)
#     swa.right(51.4285714286)
# theColor = random.choice(color)
# swa.color(theColor)
#
# for _ in range(8):
#     swa.forward(100)
#     swa.right(45)
# theColor = random.choice(color)
# swa.color(theColor)

screen.exitonclick()
