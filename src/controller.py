import threading
import recv
import direct
import move
from utils import logger
from direct import MesureByLength


def _resume_distance() -> (float, float):
    """
    Resume the distance from uwb sensor
    """
    to_a = recv.q_to_a.get()
    to_b = recv.q_to_b.get()
    return (to_a, to_b)


def _control_velocity(distance):
    """
    control velocity 
    """
    # FIXME: here will have bugs
    if distance > 10:
        move.forward(1)
    elif distance > 2:
        move.forward(0.1*distance)
    elif distance > 1:
        move.forward(0)


def control_by_e_i_theta(to_a, to_b):
    # get distance between person and car
    distance = direct.get_distance(to_a, to_b)
    # get direction and degree of angle
    direction, degree = direct.get_direction_degree(to_a, to_b)

    logger(f"direction: {direction}, degree: {degree}")
    # FIXME: here repeatly control the power of wheel
    if direction == 0:
        move.turn_left(degree)
    else:
        move.turn_right(degree)
    # control velocity
    _control_velocity(distance)


def control():
    """
    The main controller manager
    """
    while (True):
        threading.Thread(target=recv.get_distance,
                         name="recv.get_distance").start()
        # get ripe data
        to_a, to_b = _resume_distance()
        m = MesureByLength()
        power_a, power_b = m.mesure()
        move.base_movement(power_a, power_b)
