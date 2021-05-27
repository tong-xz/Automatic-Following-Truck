"""
Use two wheel power of Controller to movement 
"""


import threading
import receiver
import movement
import controller
from loguru import logger


def process():
    """
    The processor base on distance controller
    """
    while (True):
        threading.Thread(target=receiver.put_distance,
                         name="get_distance").start()
        # Resume the distance from uwb sensor
        to_a = receiver.q_to_a.get()
        to_b = receiver.q_to_b.get()
        m = controller.ControlByLength()
        power_a, power_b = m.control(to_a, to_b)
        movement.base_movement(power_a, power_b)


def process_by_e_i_theta(self, to_a, to_b):
    """
    Use e i theta method to controll
    """
    c = controller.ControlByEi()
    # get distance between person and car
    distance = c.get_distance(to_a, to_b)
    # get direction and degree of angle
    direction, degree = c.get_direction_degree(to_a, to_b)

    logger.success(f"direction: {direction}, degree: {degree}")
    if direction == 0:
        movement.turn_left(degree)
    else:
        movement.turn_right(degree)
    # control velocity
