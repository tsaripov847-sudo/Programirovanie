import turtle

#Константы для солнца
COLOR_RAYS = "orange"
COLOR_SUN = "yellow"
SUN_RADIUS = 60
RAYS_WIDTH = 6
NUMBER_RAYS = 16
LENGTH_RAYS = 90
BEAM_ROTATION = 22.5
THICKNESS_SUN = 1
BEAM_X_COORDINATE = 21
BEAM_Y_COORDINATE = 59

#Константы для облаков
CLOUD_COLOR = "white"

#Константы для цветков
BARREL_COLOR = 'dark green'
STEM_THICKNESS = 5

# Настройки экрана
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

#  СОЛНЫШКО
def sun (x,y):
    t.color(COLOR_RAYS)
    t.width(RAYS_WIDTH)

    for i in range(NUMBER_RAYS):
        t.penup()
        t.goto(x + BEAM_X_COORDINATE, y + BEAM_Y_COORDINATE)
        t.pendown()
        t.setheading(i * BEAM_ROTATION)
        t.forward(LENGTH_RAYS)

    t.width(THICKNESS_SUN)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(COLOR_SUN)
    t.begin_fill()
    t.circle(SUN_RADIUS)
    t.end_fill()

#  ОБЛАКО
def cloud (x, y, radius):
    t.color(CLOUD_COLOR)

    coords = [
        (x, y, radius),
        (x - 30, y + 10, radius - 20),
        (x + 30, y + 10, radius - 15),
        (x - 50, y - 10, radius - 30),
        (x + 50, y - 10, radius - 15),
        (x, y - 15, radius - 5)
    ]

    for a, b, r in coords:
        t.penup()
        t.goto(a, b - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()


# ЦВЕТОК
def flower (x,y, colour = "pink"):
    t.color(BARREL_COLOR)
    t.width(STEM_THICKNESS)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.setheading(90)
    t.forward(120)
    t.width(1)
    t.color("pink")
    for i in range(8):
        t.penup()
        t.goto(0, -180)
        t.pendown()
        t.setheading(i * 45)
        t.begin_fill()
        t.circle(30, 180)
        t.circle(30, 180)
        t.end_fill()
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

#Выполнение функции для рисования цветка
flower(0,-180)


#Выполнения функции для рисования солнца
sun(300, 190)

#Выполнение функции для рисования облаков
cloud(-100, 290, 40)
cloud(90, 350, 44)
cloud(-310, 340, 42)

turtle.done()