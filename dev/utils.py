"""
The Utils of System 
"""

import time
import threading


def logger(msg):
    print(f"[{threading.currentThread().getName()}] \t {msg}")
