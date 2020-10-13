# Square move test

import turtle

# Setup screen
wn = turtle.Screen()
wn.title('Square move test')
wn.bgcolor('blue')
wn.setup(width=800, height=600)
wn.tracer(0)

# Square
square = turtle.Turtle()
square.speed(0)
square.shape('square')
square.color('purple')
square.shapesize(stretch_wid=3, stretch_len=3)
square.penup()
square.goto(0, 0)

# Jumping
def square_jump():
    y = square.ycor()
    for i in range(30):
        y += 1
        square.sety(y)
    
    for i in range(30):
        y -= 1
        square.sety(y)

# main loop
while True:
    wn.update()