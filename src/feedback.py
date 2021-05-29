"""
This module is used to get the data of Avoiding obstacles components
"""

from threading import main_thread
from gpiozero import DistanceSensor
from time import sleep
from gpiozero.input_devices import InputDevice
import time
from loguru import logger
from queue import Queue
import threading

# 1st echo , 2nd trigger
_ultra_head_left = DistanceSensor(5, 6)
_ultra_head_right = DistanceSensor(8, 7)

_infra_left = InputDevice(12)
_infra_right = InputDevice(16)
_infra_bottom = InputDevice(20)

# the raw data from infra sensor
_q_infra_left_raw = Queue(100)
_q_infra_right_raw = Queue(100)
_q_infra_bottom_raw = Queue(100)

# the ripe data
q_infra_left = Queue()
q_infra_right = Queue()
q_infra_bottom = Queue()

# the raw data from ultra sensor
_q_ultra_left_raw = Queue(100)
_q_ultra_right_raw = Queue(100)

# the ripe data
q_ultra_left = Queue()
q_ultra_right = Queue()


def _get_ultra_distances():
    """
    获得左右车头两个超声波传感器的距离 (单位 m)
    """
    logger.info(
        f"ultra: [left]{_ultra_head_left.distance}, [right]{_ultra_head_right.distance}")
    _q_ultra_left_raw.put(_ultra_head_left.distance)
    _q_ultra_right_raw.put(_ultra_head_right.distance)


def _get_infrared_info():
    """
    红外返回1/0 1-无障碍物 0-有障碍物
    """
    logger.info(
        f"infra: [left] {_infra_left.value}, [right] {_infra_right.value}, [bottom] {_infra_bottom.value}")
    _q_infra_bottom_raw.put(_infra_bottom.value)
    _q_infra_left_raw.put(_infra_left.value)
    _q_infra_right_raw.put(_infra_right.value)


def put_distance():
    logger.info(f"<start> feedback put_distance")
    threading.Thread(target=_get_ultra_distances,
                     name="get_ultra_distances").start()
    threading.Thread(target=_get_infrared_info,
                     name="get_infrared_info").start()
    threading.Thread(target=_calculate_avg_feedback,
                     name="calculate_avg_feedback").start()


def _calculate_avg_feedback():
    """
    Calculate right and left uwb distance data 
    """
    logger.info(f"<start> calculate avg feedback")
    last_turn = 0
    # start = time.time()
    while (True):
        _avg_num(_q_infra_left_raw, q_infra_left, "infra0", 3)
        _avg_num(_q_infra_right_raw, q_infra_right, "infra1", 3)
        _avg_num(_q_infra_bottom_raw, q_infra_bottom, "infra2", 3)
        _avg_num(_q_ultra_left_raw, q_ultra_left, "ultra0", 3)
        _avg_num(_q_ultra_right_raw, q_ultra_right, "ultra1", 3)
        # now = time.time()
        # logger.success(f"feedback time: {now - start}")
        # start = time.time()


def _avg_num(q_ori: Queue, q_dst: Queue, name: str, num: int):
    """
    calculate avg value and put it into queue
    """
    size = q_ori.qsize()
    total = 0
    if size >= num:
        for i in range(size):
            total += q_ori.get()
        logger.success(f"<Avg> {name}: {total / size}")
        q_dst.put(total / size)
        # time.sleep(0.015)
