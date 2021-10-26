"""Marching Rectangles Algorithm in Python
"""

from random import randint
from EasyDraw import EasyDraw
from EasyDraw.Vector import Vector

# You can change these variables to get a different result
WIDTH = 1000  # screen width
HEIGHT = 1000  # screen height
COUNT = 40  # count of points

# Constant Variables
binary = [0, 1]
DIST = WIDTH//(COUNT - 1)
HALF_DIST = DIST / 2



def binary_to_decimal(num_4: binary, num_3: binary, num_2: binary, num_1: binary) -> int:
    """convert binary to decimal
    examples:
        0101 -> 5
        1111 -> 15
        0000 -> 0

    Args:
        num_4 (binary): in 1234 -> 1
        num_3 (binary): in 1234 -> 2
        num_2 (binary): in 1234 -> 3
        num_1 (binary): in 1234 -> 4

    Returns:
        int: decimal from 0 to 15
    """
    return num_4*8 + num_3*4 + num_2*2 + num_1*1


def case_of_points(app, i, j):
    """calculate case value with i and j points(4 points) and convert binary to decimal
    """
    case = binary_to_decimal(app.points[i][j],
                             app.points[i+1][j],
                             app.points[i+1][j+1],
                             app.points[i][j+1])
    return case


def generate_vector(x_pos, y_pos):
    """generated vector with x and y position and DIST & HALF_DIST
    """
    half_a = Vector(x_pos + HALF_DIST,  y_pos)
    half_b = Vector(x_pos + DIST,       y_pos + HALF_DIST)
    half_c = Vector(x_pos + HALF_DIST,  y_pos + DIST)
    half_d = Vector(x_pos,              y_pos + HALF_DIST)
    return half_a, half_b, half_c, half_d


def generate_case(x_pos, y_pos):
    """generated case dict, position of lines with decimal numbers
    """
    half_a, half_b, half_c, half_d = generate_vector(
        x_pos, y_pos)

    case = {
        0: (),
        1: (half_c, half_d),
        2: (half_b, half_c),
        3: (half_b, half_d),
        4: (half_a, half_b),
        5: [(half_a, half_d),
            (half_b, half_c)],
        6: (half_a, half_c),
        7: (half_a, half_d),
        8: (half_a, half_d),
        9: (half_a, half_c),
        10: [(half_a, half_b),
             (half_d, half_c)],
        11: (half_a, half_b),
        12: (half_b, half_d),
        13: (half_b, half_c),
        14: (half_d, half_c),
        15: ()
    }
    return case


def setup(app):
    """setup function
    """
    app.points = []
    for _ in range(0, COUNT):
        app.points.append([randint(0, 1) for _ in range(0, COUNT)])


def draw(app):
    """draw function
    """
    app.canvas.stroke_width(2)
    app.canvas.stroke('white')

    for i in range(0, COUNT - 1):
        for j in range(0, COUNT - 1):
            x_position = i * DIST
            y_position = j * DIST

            case_dict = generate_case(x_position, y_position)

            value = case_of_points(app, i, j)
            case_line_points = case_dict[value]
            if isinstance(case_line_points, tuple) and case_line_points:
                app.canvas.line(case_line_points[0], case_line_points[1])
            if isinstance(case_line_points, list):
                for case_points in case_line_points:
                    app.canvas.line(case_points[0], case_points[1])


EasyDraw(width=WIDTH,
         height=HEIGHT,
         fps=30,
         title='Marching Rectangles',
         background='black',
         autoClear=True,
         setupFunc=setup,
         drawFunc=draw)
