"""
This module is used to initialize the whole system 
"""


import serial


def serial_init_port():
    """
    Init port to serial
    The ports are:
    1. serial_port0: uwbA
    2. serial_port1: uwbB
    """
    serial_port1 = serial.Serial("/dev/ttyAMA3", baudrate=115200, timeout=3.0)
    serial_port0 = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
    return serial_port0, serial_port1
