"""
This module is used to receive the data from sensor
"""


from queue import Queue
import struct
import threading
import random
import time
import dev
import utils
from utils import logger
import init

# The global queue
# The uwb raw data
_q_uwb_a = Queue(32)
_q_uwb_b = Queue(32)

# The ripe data which have been get average and filter(TODO)
q_to_a = Queue()
q_to_b = Queue()


def _get_uwb_distance(port0, port1):
    """
    Get UWB return distance value (unit: m) 
    """
    while True:
        try:
            rcv0 = port0.read(1)
            rcv1 = port1.read(1)
            # logger(f"to_a: {int(str(rcv0)[4:-1], 16)/10}")
            # logger(f"to_b: {int(str(rcv1)[4:-1], 16)/10}")
            _q_uwb_a.put(int(str(rcv0)[4:-1], 16)/10)
            _q_uwb_b.put(int(str(rcv1)[4:-1], 16)/10)
        except:
            print("err0: ", rcv0)
            print("err1: ", rcv1)


def _get_uwb_distance_1(port0, port1):
    """
    use struct to decode 
    """
    while True:
        # try:
        rcv0 = port0.read(1)
        rcv1 = port1.read(1)
        _q_uwb_a.put(struct.unpack("B", rcv0))
        _q_uwb_b.put(struct.unpack("B", rcv1))


def _calculate_avg():
    while (True):
        _avg_num(_q_uwb_a, q_to_a, 16)
        _avg_num(_q_uwb_b, q_to_b, 16)
        time.sleep(0.02)


def _avg_num(q_ori: Queue, q_dst: Queue, num: int):
    """
    calculate avg value and put it into queue
    """
    size = q_ori.qsize()
    total = 0
    if q_ori.qsize() >= num:
        for i in range(size):
            total += q_ori.get()
        logger(f"avg: {total}")
        q_dst.put(total / size)
        time.sleep(0.02)


def get_distance():
    """
    put ripe value of the distance queue
    """
    p0, p1 = init.serial_init_port()
    logger("get_uwb_distance")
    # start recv data
    threading.Thread(target=_get_uwb_distance, args=(
        p0, p1), name="get_uwb_distance").start()
    threading.Thread(target=_calculate_avg, name="calculate_avg").start()
