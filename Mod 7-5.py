


def draw_square(kite, sz):
    for i in range(4):
        kite.forward(sz)
        kite.left(90)


wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")


def dumb_squares(kite, size):
    alex = turtle.Turtle()
    alex.color("blue")
    size = [40, 80, 120, 160, 200]

    for z in size:
        draw_square(alex, z)
        alex.penup()
        alex.backward(30)
        alex.right(70)
        alex.forward(30)
        alex.left(70)
        alex.pendown()


dumb_squares(10, 120)
wn.exitonclick()
