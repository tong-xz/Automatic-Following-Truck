import threading
import recv
import direct
import move
from utils import logger


def __resume_distance() -> (float, float):
    """
    Resume the distance from uwb sensor
    """
    logger(f"resume")
    to_a = recv.q_to_a.get()
    to_b = recv.q_to_b.get()
    return (to_a, to_b)


def control():
    while (True):
        threading.Thread(target=recv.get_distance, name="recv.get_distance").start()
        to_a, to_b = __resume_distance()
        direction, degree = direct.get_direction_degree(to_a, to_b)
        logger("fdirection: {direction}, degree: {degree}")
        if direction == 0:
            move.turn_left(degree)
        else:
            move.turn_right(degree)
