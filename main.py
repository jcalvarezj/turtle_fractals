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
    (3) Koch's curve
    (4) Koch's triangular snowflake
    (5) Koch's square snowflake
    (6) Tree''',
    'What level of the chosen fractal would you like see? (min: 0, max: 10)'
]

class FractalType(Enum):
    """
    Enum that lists constants for fractal types
    """
    CCIRCLES = 1
    BCIRCLES = 2
    KOCH = 3
    SNOWFLAKE_T = 4
    SNOWFLAKE_S = 5
    TREE = 6
    SIERPINSKI = 7


def initial_setup():
    """
    Configures the Turtle and Screen parameters
    """
    my_turtle.speed(0)
    window.delay(0)
    window.colormode(255)
    window.setup(WIDTH + 4, HEIGHT + 8)
    window.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    my_turtle.penup()
    my_turtle.pensize(3)
    my_turtle.setposition(WIDTH/2, HEIGHT/2)


def get_random_rgb():
    """
    Computes a randomized tuple that represents and RGB color
    """
    return (randint(8, 255), randint(0, 250), randint(0, 205))


def draw_fractal(fract_type, level):
    """
    Draws a fractal according to the entered type and level
    """
    color = get_random_rgb()
    if fract_type == FractalType.CCIRCLES.value:
        draw_concentric_circles(400, 0.85, color, level)
    elif fract_type == FractalType.BCIRCLES.value:        
        draw_binary_circles(WIDTH/2, HEIGHT/2, 400, color, level)
    elif fract_type == FractalType.KOCH.value:
        draw_koch_curve(WIDTH/2 - 600, HEIGHT/2 - 150, 1200, level, color)
    elif fract_type == FractalType.SNOWFLAKE_T.value:
        draw_koch_triangular_snowflake(WIDTH/2 - 250, HEIGHT/2 + 100, 1200, level)
    elif fract_type == FractalType.SNOWFLAKE_S.value:
        draw_koch_square_snowflake(WIDTH/2 - 250, HEIGHT/2 + 200, 1200, level)
    else:
        draw_tree(WIDTH/2, HEIGHT/2 - 400, 400, level, color)


def draw_circle(x, y, radius, color):
    """
    Draws a simple circle with center (x, y) and the defined radius and fill color
    """
    my_turtle.penup()
    my_turtle.setposition(x, y - radius)
    my_turtle.pendown()

    my_turtle.fillcolor(color)
    my_turtle.begin_fill()

    my_turtle.circle(radius)

    my_turtle.end_fill()


def draw_concentric_circles(radius, decrease_ratio, color, level):
    """
    Draws the concentric circles fractal.
    This fractal's minimum problem is a simple circle, and the higher order
    problem is a circle with a group of smaller concentric circles
    """
    if (level == 0):        
        draw_circle(WIDTH/2, HEIGHT/2, radius, color)
    else:
        draw_circle(WIDTH/2, HEIGHT/2, radius, color)
        new_color = get_random_rgb()        

        draw_concentric_circles(radius * decrease_ratio, decrease_ratio,
                                new_color, level - 1)


def draw_binary_circles(x, y, radius, level_color, level):
    """
    Draws the binary lateral circles fractal.
    This fractal's minimum problem is a simple circle, and the higher order
    problem is a circle with left and right recursions (circles and groups)
    """
    if (level == 0):
        draw_circle(x, y, radius, level_color)
    else:
        draw_circle(x, y, radius, level_color)

        new_color = get_random_rgb()

        draw_binary_circles(x - radius / 2, y, radius / 2, new_color, level - 1)
        draw_binary_circles(x + radius / 2, y, radius / 2, new_color, level - 1)
    

def draw_line(x, y, length, color = (0, 0, 0)):
    """
    Draws a simple line starting from (x, y), with the entered length and
    color, that goes forward according to the turtle's head angle

    Returns the final position of the turtle after moving
    """
    my_turtle.setposition(x, y)
    my_turtle.pencolor(color)
    my_turtle.pendown()
    my_turtle.forward(length)
    return my_turtle.pos()


def draw_koch_curve(x, y, length, level, level_color = (0, 0, 0)):
    """
    Draws a Koch's curve fractal and returns the last position of a subproblem
    drawing.
    This fractal's minimum problem is a simple line, and the higher order
    problem is defined as follows:
    "i-1 level" drawing, turn 60° to the left, "i-1 level" drawing, turn 120°
    to the right, "i-1" level drawing, turn 60° to the left, "i-1 level" drawing
    
    The previous can be formally defined as a Lyndenmayer system as:    
    F = K+K--K+K

    For F as the general problem, K as a recursive subproblem of F, + as
    turning 60 degrees to the left, and - as turning 60 degrees to the right
    """
    if (level < 1):
        return draw_line(x, y, length, level_color)
    else:
        color1 = get_random_rgb()
        pos1 = draw_koch_curve(x, y, length/3, level - 1, color1)
        my_turtle.left(60)

        color2 = get_random_rgb()
        pos2 = draw_koch_curve(pos1[0], pos1[1], length/3, level - 1, color2)
        my_turtle.right(120)

        pos3 = draw_koch_curve(pos2[0], pos2[1], length/3, level - 1, color2)
        my_turtle.left(60)

        return draw_koch_curve(pos3[0], pos3[1], length/3, level - 1, color1)


def draw_koch_triangular_snowflake(x, y, length, level):
    """
    Draws a Koch's triangular snowflake fractal and returns the last position
    of a subproblem drawing.
    This fractal's minimum problem is a simple equilateral triangle, and the
    higher order problem is defined as follows:
    
        "i-1 level" Koch's curve, turn 120° to the right, "i-1 level" Koch's
        curve, turn 120° to the right, "i-1 level" Koch's curve
    
    The previous can be formally defined as a Lyndenmayer system as:    
    
        F = K-K-K

    For F as the general problem, K as a Koch curve, and - as turning 120
    degrees to the right
    """
    if (level < 1):
        return draw_line(x, y, length)
    else:
        pos1 = draw_koch_curve(x, y, length/3, level - 1)
        my_turtle.right(120)

        pos2 = draw_koch_curve(pos1[0], pos1[1], length/3, level - 1)
        my_turtle.right(120)

        return draw_koch_curve(pos2[0], pos2[1], length/3, level - 1)


def draw_koch_square_snowflake(x, y, length, level):
    """
    Draws a Koch's square snowflake fractal and returns the last position of a
    subproblem drawing.
    This fractal's minimum problem is a simple square, and the higher order
    problem is defined as follows:
    
        "i-1 level" Koch's curve, turn 120° to the right, "i-1 level" Koch's
        curve, turn 120° to the right, "i-1 level" Koch's curve
    
    The previous can be formally defined as a Lyndenmayer system as:    
    
        F = K-K-K-K

    For F as the general problem, K as a "i-1 level" Koch curve, and - as 
    turning 90 degrees to the right
    """    
    if (level < 1):
        return draw_line(x, y, length)
    else:
        pos1 = draw_koch_curve(x, y, length/3, level - 1)
        my_turtle.right(90)

        pos2 = draw_koch_curve(pos1[0], pos1[1], length/3, level - 1)
        my_turtle.right(90)

        pos3 = draw_koch_curve(pos2[0], pos2[1], length/3, level - 1)
        my_turtle.right(90)

        return draw_koch_curve(pos3[0], pos3[1], length/3, level - 1)


def draw_tree(x, y, length, level, color, angle = 90):
    if (level < 1):
        my_turtle.setheading(angle)
        draw_line(x, y, length, color)
    else:
        my_turtle.setheading(angle)
        pos1 = draw_line(x, y, length, color)

        new_color = get_random_rgb()        

        my_turtle.left(40)
        current_angle = my_turtle.heading()
        draw_tree(pos1[0], pos1[1], length * 0.45, level - 1, new_color, current_angle)

        my_turtle.setheading(angle)

        my_turtle.right(40)
        current_angle = my_turtle.heading()
        draw_tree(pos1[0], pos1[1], length * 0.45, level - 1, new_color, current_angle)
        
        my_turtle.penup()


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

    if (validate_option(fractal_option, 1, 6)):
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
    try:
        main_cli()
    except ValueError as e:
        print('\nSorry, only numbers are valid! Try again\n')