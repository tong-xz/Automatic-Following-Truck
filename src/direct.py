"""
Need to return motor power 
"""
# This file used to get uwb value
import gpiozero
import math
import recv
from utils import logger


# The distance between base station A and station B (unit: m)
to_C = 0.2


class MesureByEi():

    def get_distance(self, to_a, to_b) -> float:
        """
        Get the REALL distance from person to car 
        use cos
        """
        # Degree between a and c
        degree_ac = math.acos((to_a**2+to_C**2-to_b**2) / 2*to_a*to_C)
        # degree_BC = acos((to_b**2+to_C**2-to_a**2) / 2*to_b*to_C)
        # degree = acos((to_a**2-to_C**2+to_b**2) / 2*to_a*to_b)
        distance = to_a*math.sin(degree_ac)
        return distance

    def get_direction_degree(self, to_a, to_b, distance) -> (int, float):
        """
        Get the (direction, degree=cos(angle)) of turn direction.

        1. diretion: 
            - 0=left
            - 1=right
        2. degree: The cos of angle from the person to the midpoint of the car
        """
        # determin direction
        if to_a > to_b:
            direction = 0
        else:
            direction = 1
        x = (to_b**2 - distance**2)**0.5 - to_C
        degree = math.cos(math.atan(distance/(x + 0.5*to_C)))
        return (direction, degree)

    def mesure(self):
        pass


class MesureByLength():
    def _control_power(self, distance):
        """
        control velocity 
        """
        if distance > 7:
            distance = 1
        elif distance > 2:
            distance = 0.2*distance
        elif distance > 1:
            distance = 0.1*distance
        return distance

    def mesure(self, to_a, to_b) -> (float, float):
        """
        use to_a and to_b distance to get power of wheel a and b
        """
        power_a = _control_power(to_a)
        power_b = _control_power(to_b)
        logger(f"power_a: {power_a}, power_b: {power_b}")
        return power_a, power_b
