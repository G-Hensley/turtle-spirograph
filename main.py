from turtle import Turtle, Screen
from random import randint

# Create a turtle object and set its shape, color, speed, and pensize
tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed("fastest")
tim.pensize(1)

# Define a function to generate a random color
def random_color():
    tup = (randint(1, 255,), randint(1, 255), randint(1, 255))
    return tup


# Define a function to draw a spirograph
def spirograph(degree):
    for _ in range(int(360 / degree)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + degree)

# Create a screen object and set its color mode to 255
my_screen = Screen()
my_screen.colormode(255)

# Draw a spirograph with a degree of 5
spirograph(5)

# Exit the program when the user clicks on the screen
my_screen.exitonclick()
