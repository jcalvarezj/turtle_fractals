"""
This is a simple example of recursive fractal drawing using the turtle graphics
library 
"""
import turtle
from enum import Enum
from random import randint

class FractalType(Enum):
    """
    Enum that lists constants for fractal types
    """
    CIRCLES = 0
    SPIKES = 1
    TEETH = 2    
    SIERPINSKI = 3

WIDTH = 1200
HEIGHT = 800

my_turtle = turtle.Turtle()
window = turtle.Screen()


def initial_setup():
    my_turtle.speed(0)
    window.colormode(255)
    window.setup(WIDTH + 4, HEIGHT + 8)
    window.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    my_turtle.penup()
    my_turtle.setposition(WIDTH/2, HEIGHT/2)


def draw_fractal(fract_type):
    if fract_type == FractalType.CIRCLES.value:
        draw_concentric_circles(400, 0.85)
    elif fract_type == FractalType.SPIKES.value:
        colors = (randint(0, 255), randint(0, 255), randint(0, 255))
        draw_binary_circles(WIDTH/2, HEIGHT/2, 400, colors)
    else:
        pass


def draw_concentric_circles(radius, decrease_ratio):
    if (radius > 5):
        my_turtle.penup()
        my_turtle.right(90)
        my_turtle.forward(radius)
        my_turtle.left(90)
        my_turtle.pendown()

        my_turtle.fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        my_turtle.begin_fill()
        my_turtle.circle(radius)
        my_turtle.end_fill()

        my_turtle.penup()
        my_turtle.setposition(WIDTH/2, HEIGHT/2)

        draw_concentric_circles(radius * decrease_ratio, decrease_ratio)


def draw_circle(x, y, radius, colors):
    my_turtle.penup()
    my_turtle.setposition(x, y - radius)
    my_turtle.pendown()

    my_turtle.fillcolor(colors)
    my_turtle.begin_fill()

    my_turtle.circle(radius)

    my_turtle.end_fill()


def draw_binary_circles(x, y, radius, level_colors):
    if (radius > 10):            
            draw_circle(x, y, radius, level_colors)

            new_colors = (randint(0, 255), randint(0, 255), randint(0, 255))

            draw_binary_circles(x - radius / 2, y, radius / 2, new_colors)
            draw_binary_circles(x + radius / 2, y, radius / 2, new_colors)


if __name__ == "__main__":
    initial_setup()

    draw_fractal(0)
    
    window.mainloop()
