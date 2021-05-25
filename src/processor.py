"""
Use two wheel power of Controller to movement 
"""


import threading
import receiver
import movement
from loguru import logger


def process():
    """
    The processor base on distance controller
    """
    while (True):
        threading.Thread(target=receiver.get_distance,
                         name="receiver.get_distance").start()
        # Resume the distance from uwb sensor
        to_a = recv.q_to_a.get()
        to_b = recv.q_to_b.get()
        m = controller.
        power_a, power_b = m.mesure(to_a, to_b)
        move.base_movement(power_a, power_b)


def process_by_e_i_theta(self, to_a, to_b):
    """
    Use e i theta method to controll
    """
    # get distance between person and car
    distance = direct.get_distance(to_a, to_b)
    # get direction and degree of angle
    direction, degree = direct.get_direction_degree(to_a, to_b)

    logger.success(f"direction: {direction}, degree: {degree}")
    if direction == 0:
        move.turn_left(degree)
    else:
        move.turn_right(degree)
    # control velocity
    _control_velocity(distance)
