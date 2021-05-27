"""
This module is used to receive the data from sensor
"""


from queue import Queue
import struct
import threading
import random
import time
import init
from loguru import logger
from serial.serialutil import SerialException


# The global queue
# The uwb raw data
_q_uwb_a = Queue(32)
_q_uwb_b = Queue(32)

# The ripe data which have been get average and filter(TODO)
q_to_a = Queue()
q_to_b = Queue()

_p0, _p1 = init.serial_init_port()


def _get_uwb_distance(port0, port1):
    """
    Get UWB return distance value (unit: m) 
    """
    counter = 0
    while True:
        try:
            counter += 1
            rcv0 = port0.read(1)
            rcv1 = port1.read(1)
            d0 = int(str(rcv0)[4:-1], 16)/10
            d1 = int(str(rcv1)[4:-1], 16)/10
            if counter >= 10:
                logger.trace(f"to_a: {d0}, recv: {rcv0}")
                logger.trace(f"to_b: {d1}, recv: {rcv1}")
                counter = 0
            _q_uwb_a.put(d0)
            _q_uwb_b.put(d1)
        except:
            if rcv0 != b'':
                print("err0: ", rcv0)

            if rcv0 != b'':
                print("err1: ", rcv1)


def _get_uwb_distance_struct(port0, port1):
    """
    use struct to decode 
    """
    while True:
        try:
            rcv0 = port0.read(1)
            rcv1 = port1.read(1)

            # 避免空数据
            if rcv0 == b'' or rcv1 == b'':
                continue

            d0 = struct.unpack("@B", rcv0)[0]
            d1 = struct.unpack("@B", rcv1)[0]
            logger.trace(f"to_a: {d0}\t recv: {rcv0}\t bin: {bin(d0)}")
            logger.trace(f"to_b: {d1}\t recv: {rcv1}\t bin: {bin(d1)}")

            # 警告错数据
            if d0 > 200 or d1 > 200:
                logger.warning("距离太长")

            d0 /= 10
            d1 /= 10
            _q_uwb_a.put(d0)
            _q_uwb_b.put(d1)

        except SerialException as e:
            logger.error(f"Serial is repeat config: {e}")

        except Exception as e:
            logger.error("Exception: ", e)
            logger.error("err0: ", rcv0, "err1: ", rcv1)


def _calculate_avg():
    """
    Calculate right and left uwb distance data 
    """
    while (True):
        _avg_num(_q_uwb_a, q_to_a, "to_a", 16)
        _avg_num(_q_uwb_b, q_to_b, "to_b", 16)
        time.sleep(0.015)


def _avg_num(q_ori: Queue, q_dst: Queue, name: str, num: int):
    """
    calculate avg value and put it into queue
    """
    size = q_ori.qsize()
    total = 0
    if q_ori.qsize() >= num:
        for i in range(size):
            total += q_ori.get()
        logger.success(f"{name} avg: {total / size}")
        q_dst.put(total / size)
        time.sleep(0.015)


def put_distance():
    """
    是整个文件的入口, 把可用数据放到缓冲区(队列)中 
    put ripe value of the distance queue
    """
    # start recv data
    threading.Thread(target=_get_uwb_distance_struct, args=(
        _p0, _p1), name="put_distance").start()
    threading.Thread(target=_calculate_avg, name="calculate_avg").start()
