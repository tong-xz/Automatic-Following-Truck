# This file used to get uwb value
import gpiozero
import math
import recv


# The distance between base station A and station B (unit: m)
to_C = 0.2


def __get_distance(to_a, to_b) -> float:
    """
    Get the distance from person to car 
    用了余弦定理
    """
    # Degree between a and c
    degree_AC = math.acos((to_a**2+to_C**2-to_b**2) / 2*to_a*to_C)
    # degree_BC = acos((to_b**2+to_C**2-to_a**2) / 2*to_b*to_C)
    # degree = acos((to_a**2-to_C**2+to_b**2) / 2*to_a*to_b)
    distance = to_a*math.sin(degree_AC)
    return distance


def get_direction_degree(to_a, to_b) -> (int, float):
    """
    Get the (direction, degree) of turn direction

    diretion: 
        0 = left
        1 = right
    degree:
        The cos of angle from the person to the midpoint of the car
    """
    distance = __get_distance(to_a, to_b)
    # determin direction
    if to_a > to_b:
        direction = 0
    else:
        direction = 1
    x = (to_b**2 - distance**2)**0.5 - to_C
    degree = math.cos(math.atan(distance/(x + 0.5*to_C)))
    return (direction, degree)
