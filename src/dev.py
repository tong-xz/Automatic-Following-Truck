import random
from queue import Queue
import time
import threading
from utils import logger


def __generate_random_queue(q1: Queue, q2: Queue):
    while (True):
        q1.put(random.Random())
        q1.put(random.Random())
        logger("put random distance")
        time.sleep(0.025)


def generate_random_queue(q1: Queue, q2: Queue):
    logger("generate_random_queue")
    threading.Thread(target=__generate_random_queue, args=(
        q1, q2), name="generate_random_queue").start()
