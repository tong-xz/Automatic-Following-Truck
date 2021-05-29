"""
Use two wheel power of Controller to movement 
"""


import threading
import receiver
import movement
import controller
from loguru import logger
import feedback


def process():
    """
    The processor base on distance controller
    """
    logger.info(f"<start> Processor start")
    logger.info(f"<start> controller manager start")
    manager = controller.ControlByLength()
    # Resume the distance from uwb sensor
    threading.Thread(target=receiver.put_distance,
                        name="get_distance_receiver").start()
    threading.Thread(target=feedback.put_distance,
                        name="get_distance_feedback").start()
    while (True):
        to_a = receiver.q_to_a.get()
        to_b = receiver.q_to_b.get()

        # get instructions
        power_a, power_b = manager.control(to_a, to_b)

        # the feedback part
        # infra_left = feedback.q_infra_left.get(block=False)
        # infra_bottom = feedback.q_infra_bottom.get(block=False)
        # infra_right = feedback.q_infra_right.get(block=False)
        # ultra_left = feedback.q_ultra_left.get(block=False)
        # ultra_right = feedback.q_ultra_right.get(block=False)

        # logger.success("here2")
        # # slow down
        # if ultra_left < 0.5 or ultra_right < 0.5:
        #     logger.success("----- slow down -----")
        #     power_a, power_b = 0, 0

        # # shut down
        # if infra_bottom > 0.05 or ultra_left < 0.3 or ultra_right < 0.3:
        #     logger.success("----- shut down -----")
        #     is_shut = True
        is_shut = False
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
