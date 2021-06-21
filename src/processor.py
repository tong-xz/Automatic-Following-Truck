"""
Use two wheel power of Controller to movement 
"""


import threading
import receiver
import movement
import controller
from loguru import logger
import feedback


def _get_move_instruction():
    to_a = receiver.q_to_a.get()
    to_b = receiver.q_to_b.get()
    return to_a, to_b


def _get_feedback_instructions():
    # ultra_left = 1
    # ultra_right = 1
    # infra_left = 1
    # infra_right = 1
    # infra_bottom = 0
    ultra_left = feedback._ultra_head_right.distance
    ultra_right = feedback._ultra_head_left.distance
    infra_left = feedback._infra_left.value
    infra_bottom = feedback._infra_bottom.value
    infra_right = feedback._infra_right.value
    return ultra_left, ultra_right, infra_left, infra_bottom, infra_right


def _feedback_consume(power_a, power_b, ultra_left, ultra_right, infra_left, infra_bottom, infra_right):

    return power_a, power_b


def process():
    """
    The processor base on distance controller
    """
    logger.success(f"<START> Processor & controller manager.")
    manager = controller.ControlByLength()
    # Resume the distance from uwb sensor
    threading.Thread(target=receiver.put_distance,
                     name="get_distance_receiver").start()
    while (True):
        logger.success("="*70)

        # init
        to_a, to_b = _get_move_instruction()
        ultra_left, ultra_right, infra_left, infra_bottom, infra_right = _get_feedback_instructions()
        is_shut = False

        # get movement instructions
        power_a, power_b = manager.control(to_a, to_b)

        # add feedback effect
        # power_a, power_b = _feedback_consume(
        #     power_a, power_b, ultra_left, ultra_right, infra_left, infra_bottom, infra_right)
        logger.success(
            f"<ultra> [left] {ultra_left} === {ultra_right} [right]")
        logger.success(
            f"<infra> {infra_bottom} || {infra_left} || {infra_right}")
        # slow down
        if ultra_left < 0.5 or ultra_right < 0.5:
            logger.warning("----- slow down -----")
            power_a, power_b = 0, 0

        # shut down
        if infra_bottom > 0.05 or ultra_left < 0.3 or ultra_right < 0.3:
            logger.warning("----- shut down -----")
            is_shut = True

        # head avoid
        if infra_right < 0.1:
            logger.warning("----- infra_right -----")
            power_b = power_b*0.7
            # power_a = power_a*1.05

        if infra_left < 0.1:
            logger.warning("----- infra_left -----")
            # power_b = power_b*1.05
            power_a = power_a*0.7

        movement.base_movement(p0=power_a, p1=power_b, is_shut=is_shut)


def process_by_e_i_theta(self, to_a, to_b):
    """
    Use e i theta method to controll
    """
    c = controller.ControlByEi()
    # get distance between person and car
    distance = c.get_distance(to_a, to_b)
    # get direction and degree of angle
    direction, degree = c.get_direction_degree(to_a, to_b, distance)

    logger.success(f"direction: {direction}, degree: {degree}")
    if direction == 0:
        movement.turn_left(degree)
    else:
        movement.turn_right(degree)
    # control velocity


def back_up():
    # threading.Thread(target=feedback.put_distance,
    #                  name="get_distance_feedback").start()

    # infra_left = feedback.q_infra_left.get()
    # infra_bottom = feedback.q_infra_bottom.get()
    # infra_right = feedback.q_infra_right.get()
    # ultra_right = feedback.q_ultra_right.get(block=True, timeout=3.0)
    # ultra_left = feedback.q_ultra_left.get(block=True, timeout=3.0)
    pass
