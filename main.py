"""
This is a simple example of recursive fractal drawing using turtle graphics
"""
import turtle
from enum import Enum
from random import randint

WIDTH = 1200
HEIGHT = 800


class FractalType(Enum):
    """
    Enum that lists constants for fractal types
    """
    CCIRCLES = 0
    BCIRCLES = 1
    KOCH = 2
    TEETH = 3
    SIERPINSKI = 4


my_turtle = turtle.Turtle()
window = turtle.Screen()


def initial_setup():
    my_turtle.speed(0)
    window.delay(0)
    window.colormode(255)
    window.setup(WIDTH + 4, HEIGHT + 8)
    window.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    my_turtle.penup()
    my_turtle.pensize(3)
    my_turtle.setposition(WIDTH/2, HEIGHT/2)


def get_random_rgb():
    return (randint(8, 255), randint(0, 250), randint(0, 205))


def draw_fractal(fract_type):
    colors = get_random_rgb()
    if fract_type == FractalType.CCIRCLES.value:
        draw_concentric_circles(400, 0.85)
    elif fract_type == FractalType.BCIRCLES.value:        
        draw_binary_circles(WIDTH/2, HEIGHT/2, 400, colors)
    elif fract_type == FractalType.KOCH.value:
        draw_koch_curve(WIDTH/2 - 400, HEIGHT/2, 800, 5, colors)
    else:
        pass


def draw_circle(x, y, radius, colors):
    my_turtle.penup()
    my_turtle.setposition(x, y - radius)
    my_turtle.pendown()

    my_turtle.fillcolor(colors)
    my_turtle.begin_fill()

    my_turtle.circle(radius)

    my_turtle.end_fill()


def draw_concentric_circles(radius, decrease_ratio):
    if (radius > 5):
        color = get_random_rgb()
        draw_circle(WIDTH/2, HEIGHT/2, radius, color)
        my_turtle.end_fill()

        my_turtle.penup()
        my_turtle.setposition(WIDTH/2, HEIGHT/2)

        draw_concentric_circles(radius * decrease_ratio, decrease_ratio)


def draw_binary_circles(x, y, radius, level_color):
    if (radius >= 25):            
            draw_circle(x, y, radius, level_color)

            new_color = get_random_rgb()

            draw_binary_circles(x - radius / 2, y, radius / 2, new_color)
            draw_binary_circles(x + radius / 2, y, radius / 2, new_color)


def draw_line(x, y, length, color):
    my_turtle.setposition(x, y)
    my_turtle.pencolor(color)
    my_turtle.pendown()
    my_turtle.forward(length)
    return my_turtle.pos()


def draw_koch_curve(x, y, length, level, level_color):
    if (level < 1):
        return draw_line(x, y, length, level_color)
    else:
        color1 = get_random_rgb()
        pos = draw_koch_curve(x, y, length/3, level - 2, color1)
        my_turtle.left(60)
        color2 = get_random_rgb()
        pos2 = draw_koch_curve(pos[0], pos[1], length/3, level - 1, color2)
        my_turtle.right(120)        
        pos3 = draw_koch_curve(pos2[0], pos2[1], length/3, level - 1, color2)
        my_turtle.left(60)        
        return draw_koch_curve(pos3[0], pos3[1], length/3, level - 2, color1)


if __name__ == "__main__":
    initial_setup()

    draw_fractal(2)
    
    window.mainloop()
