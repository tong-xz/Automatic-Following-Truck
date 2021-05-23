

import time
import threading


def logger(msg):
    print(f"<{threading.currentThread().getName()}|{time.time()}> {msg}")
