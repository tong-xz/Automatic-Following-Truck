"""
This file used to control basic movement

0 < velocity < 1
"""

from gpiozero import PWMLED
from time import sleep
from queue import Queue


# # all movement queue
# __q_a = Queue()
# __q_b = Queue()


# def aaa():
#     """
#     This function is used to move smoothly
#     """


# left wheel A
# right wheel B
__A_Power = PWMLED(4)
__A_Reverse = PWMLED(17)
__A_Park = PWMLED(27)
__B_Power = PWMLED(18)
__B_Reverse = PWMLED(23)
__B_Park = PWMLED(24)


def base_movement(p0, p1, r0=False, r1=False):
    """
    The base movement of controlling the two motor power
    - p0: power of 0 wheel 
    - p1: power of 1 wheel
    - r0: reverse of roll, the default is forward, False is backward
    - r1: reverse of roll, the default is forward, False is backward
    """
    # limitation the value between [0, 1]
    p0 = power_limitation(p0)
    p1 = power_limitation(p1)

    # the backward situation
    if r0:
        __A_Reverse.value = 0.0
    else:
        __A_Reverse.value = 1.0

    if r1:
        __B_Reverse.value = 1.0
    else:
        __B_Reverse.value = 0.0

    __A_Power.value = p0
    __B_Power.value = p1


def forward(velocity):
    velocity = power_limitation(velocity)
    __A_Reverse.value = 1.0
    __B_Reverse.value = 0.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def backward(velocity):
    velocity = power_limitation(velocity)
    __A_Reverse.value = 0.0
    __B_Reverse.value = 1.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def turn_right(velocity):
    velocity = power_limitation(velocity)
    __A_Reverse.value = 1.0
    __B_Reverse.value = 1.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def turn_left(velocity):
    velocity = power_limitation(velocity)
    __A_Reverse.value = 0.0
    __B_Reverse.value = 0.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def slide():
    """
    no power input and silde 
    """
    __A_Power.value = 0
    __B_Power.value = 0


def power_limitation(p):
    if p < 0:
        return 0
    if p > 1:
        return 1
    else:
        return p
