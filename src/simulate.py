"""
The simulation
"""

import random
from queue import Queue
import time
import threading
from utils import logger
import init


# The global queue
# The uwb raw data
_q_uwb_a = Queue(32)
_q_uwb_b = Queue(32)

# The ripe data which have been get average and filter(TODO)
q_to_a = Queue()
q_to_b = Queue()


def _generate_random_queue(q0, q1):
    """
    generate random data
    """
    counter = 0
    while (True):
        counter += 1
        r = random.Random()
        q0.put(r.random())
        q1.put(r.random())
        print(f"put {counter}")
        time.sleep(0.025)


def _resume_queue(q0, q1):
    while (True):
        to_a = q0.get()
        to_b = q1.get()
        print(f"(q0: {to_a}, q1:{to_b})")


def _avg():
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

        q_dst.put(total / size)


def store_uwb(recv, file_name):
    with open(file_name, mode="ab") as _f:
        _f.write(recv)


def simulate_random():
    """
    这个是用于模拟随机生成与计算
    """
    threading.Thread(target=_generate_random_queue,
                     args=(_q_uwb_a, _q_uwb_b)).start()

    threading.Thread(target=_avg).start()

    threading.Thread(target=_resume_queue,
                     args=(q_to_a, q_to_b)).start()
    print("hello")


if __name__ == "__main__":
    p0, p1 = init.serial_init_port()
    rcv0 = p0.read(1)
    rcv1 = p1.read(1)
    store_uwb(rcv0, "./uwb0.recv")
    store_uwb(rcv1, "./uwb1.recv")
