"""
This is a simple example of recursive fractal drawing using turtle graphics
"""
import turtle
from enum import Enum
from random import randint

WIDTH = 1200
HEIGHT = 800
MENU = [
    '''Please enter the desired option:
    (1) Concentric circles
    (2) Binary lateral circles
    (3) Koch curve''',
    'What level of the chosen fractal would you like see? (min: 0, max: 10)'
]

class FractalType(Enum):
    """
    Enum that lists constants for fractal types
    """
    CCIRCLES = 1
    BCIRCLES = 2
    KOCH = 3
    TEETH = 4
    SIERPINSKI = 5


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


def draw_fractal(fract_type, level):
    color = get_random_rgb()
    if fract_type == FractalType.CCIRCLES.value:
        draw_concentric_circles(400, 0.85, color, level)
    elif fract_type == FractalType.BCIRCLES.value:        
        draw_binary_circles(WIDTH/2, HEIGHT/2, 400, color, level)
    elif fract_type == FractalType.KOCH.value:
        draw_koch_curve(WIDTH/2 - 400, HEIGHT/2, 800, color, level)
    else:
        pass


def draw_circle(x, y, radius, color):
    my_turtle.penup()
    my_turtle.setposition(x, y - radius)
    my_turtle.pendown()

    my_turtle.fillcolor(color)
    my_turtle.begin_fill()

    my_turtle.circle(radius)

    my_turtle.end_fill()


def draw_concentric_circles(radius, decrease_ratio, color, level):
    if (level == 0):        
        draw_circle(WIDTH/2, HEIGHT/2, radius, color)
    else:
        draw_circle(WIDTH/2, HEIGHT/2, radius, color)
        new_color = get_random_rgb()        

        draw_concentric_circles(radius * decrease_ratio, decrease_ratio,
                                new_color, level - 1)


def draw_binary_circles(x, y, radius, level_color, level):
    if (level == 0):
        draw_circle(x, y, radius, level_color)
    else:
        draw_circle(x, y, radius, level_color)
        
        new_color = get_random_rgb()

        draw_binary_circles(x - radius / 2, y, radius / 2, new_color, level - 1)
        draw_binary_circles(x + radius / 2, y, radius / 2, new_color, level - 1)
    


def draw_line(x, y, length, color):
    my_turtle.setposition(x, y)
    my_turtle.pencolor(color)
    my_turtle.pendown()
    my_turtle.forward(length)
    return my_turtle.pos()


def draw_koch_curve(x, y, length, level_color, level):
    if (level < 1):
        return draw_line(x, y, length, level_color)
    else:
        color1 = get_random_rgb()
        pos = draw_koch_curve(x, y, length/3, color1, level - 2)
        my_turtle.left(60)

        color2 = get_random_rgb()
        pos2 = draw_koch_curve(pos[0], pos[1], length/3, color2, level - 1)
        my_turtle.right(120)

        pos3 = draw_koch_curve(pos2[0], pos2[1], length/3, color2, level - 1)
        my_turtle.left(60)

        return draw_koch_curve(pos3[0], pos3[1], length/3, color1, level - 2)


def validate_option(option, min_value, max_value):
    """
    Validates whether an option number is in the accepted interval (between
    min_value and max_value)
    """
    if (option >= min_value and option <= max_value):
        return True
    else:
        print("\nNot a valid option!")
        print(f'Only numbers between {min_value} and {max_value} are valid.\n')
        return False


def prompt_user(message_index):
    """
    Prompts the user with a message to input data and returns it
    """
    print(MENU[message_index])
    return input()


def main_cli():
    """
    Program entry point. Interactive CLI
    """    
    fractal_option = 0
    level_option = 0

    fractal_option = int(prompt_user(0))

    if (validate_option(fractal_option, 1, 3)):
        level_option = int(prompt_user(1))

        if (validate_option(level_option, 0, 10)):            
            global my_turtle
            global window

            my_turtle = turtle.Turtle()                            
            window = turtle.Screen()
            initial_setup()

            draw_fractal(fractal_option, level_option)

            window.mainloop()


if __name__ == "__main__":
    # my_turtle = turtle.Turtle()                            
    # window = turtle.Screen()
    # initial_setup()

    # draw_fractal(1, 5)

    # window.mainloop()
    try:
        main_cli()
    except ValueError as e:
        print('\nSorry, only numbers are valid! Try again\n')