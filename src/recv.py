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
__q_uwb_a = Queue(16)
__q_uwb_b = Queue(16)

# The ripe data which have been get average and filter(TODO)
q_to_a = Queue()
q_to_b = Queue()


def __get_uwb_distance(port0, port1):
    """
    Get UWB return distance value (unit: m) 
    """
    while True:
        try:
            rcv0 = port0.read(1)
            rcv1 = port1.read(1)
            logger(f"to_a: {int(str(rcv0)[4:-1], 16)/10}")
            logger(f"to_b: {int(str(rcv1)[4:-1], 16)/10}")
            __q_uwb_a.put(int(str(rcv0)[4:-1], 16)/10)
            __q_uwb_b.put(int(str(rcv1)[4:-1], 16)/10)
        except:
            print("err0: ", rcv0)
            print("err1: ", rcv1)


def __get_uwb_distance_1(port0, port1):
    """TODO: 暂时还没有写好
    用 struct 来解码
    """
    while True:
        # try:
        rcv0 = port0.read(1)
        rcv1 = port1.read(1)
        __q_uwb_a.put(struct.unpack("I", rcv0))
        __q_uwb_b.put(struct.unpack("I", rcv1))


def get_distance():
    """
    put ripe value of the distance queue
    """
    p0, p1 = init.serial_init_port()
    logger("get_uwb_distance")
    # start recv data
    threading.Thread(target=__get_uwb_distance, args=(
        p0, p1), name="get_uwb_distance").start()
    threading.Thread(target=__calculate_avg, name="calculate_avg").start()


def __calculate_avg():
    while (True):
        if __q_uwb_a.full() or __q_uwb_b.full():
            to_a = 0
            to_b = 0
            # logger("HERE")
            for i in range(16):
                to_a += __q_uwb_a.get()
            for i in range(16):
                to_b += __q_uwb_b.get()

            logger(f"to_a: {to_a}")
            logger(f"to_b: {to_b}")

            q_to_a.put(to_a / 16)
            q_to_b.put(to_b / 16)
