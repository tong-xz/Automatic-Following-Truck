import threading
import recv
import direct
import move
from utils import logger


def __resume_distance() -> (float, float):
    """
    Resume the distance from uwb sensor
    """
    to_a = recv.q_to_a.get()
    to_b = recv.q_to_b.get()
    return (to_a, to_b)

def __control_velocity(distance):
    """
    control velocity 
    """
    # TODO: 这里需要一个变速
    if distance > 2:
        move.forward(1)
    else:
        move.forward(0)


def control():
    """
    The controller manager
    """
    while (True):
        threading.Thread(target=recv.get_distance, name="recv.get_distance").start()
        to_a, to_b = __resume_distance()
        distance = direct.get_distance(to_a, to_b)
        direction, degree = direct.get_direction_degree(to_a, to_b)
        logger(f"direction: {direction}, degree: {degree}")
        if direction == 0:
            move.turn_left(degree)
        else:
            move.turn_right(degree)
        # control velocity
        __control_velocity(distance)

        
