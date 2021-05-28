"""
[control algorithm]

Using all the information received, return the power of the two wheels
"""
import gpiozero
import math
import receiver


# The distance between base station A and station B (unit: m)
to_C = 0.2


class ControlByEi():
    """
    base on two points distance and angle 
    """

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

    def control(self):
        pass


class ControlByLength():
    """
    Base on the two distance of UWB
    """

    def _control_power(self, distance):
        """
        control power base on divide distance levels
        """
        if distance > 7:
            distance = 1
        elif distance > 2:
            distance = 0.2*distance
        elif distance > 1:
            distance = 0.1*distance
        return distance

    def control(self, to_a, to_b) -> (float, float):
        """
        use to_a and to_b distance to get power of wheel a and b
        """
        power_a = self._control_power(to_a)
        power_b = self._control_power(to_b)
        return power_a, power_b
