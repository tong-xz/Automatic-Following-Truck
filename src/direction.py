# This file used to get uwb value
import gpiozero
from math import acos, atan, cos, sin, tan


# The distance between base station A and station B (unit: m)
to_C = 0.2


def get_raw_distance() -> (float, float):
    """
    Get the distance from uwb sensor
    """
    to_A = gpiozero.SmoothedInputDevice(pin=1)
    to_B = gpiozero.SmoothedInputDevice(pin=2)
    return (to_A, to_B)


def get_distance(to_A, to_B) -> float:
    """
    Get the distance from person to car 
    """
    # Degree between a and c
    degree_AC = acos((to_A**2+to_C**2-to_B**2) / 2*to_A*to_C)
    # degree_BC = acos((to_B**2+to_C**2-to_A**2) / 2*to_B*to_C)
    # degree = acos((to_A**2-to_C**2+to_B**2) / 2*to_A*to_B)
    distance = to_A*sin(degree_AC)
    return distance


def get_direction_degree(to_A, to_B, distance) -> (int, float):
    """
    Get the direction and the degree of turn direction
    diretion: 
        0 = left  
        1 = right
    degree:
        The cos of angle from the person to the midpoint of the car
    """
    # determin direction
    if to_A > to_B:
        direction = 0
    else:
        direction = 1
    x = (to_B**2 - distance**2)**0.5 - to_C
    degree = cos(atan(distance/(x + 0.5*to_C)))
    return (direction, degree)
