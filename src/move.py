"""
This file used to control basic movement

0 < velocity < 1
"""

from gpiozero import PWMLED
from time import sleep


# left wheel A
# right wheel B
__A_Power = PWMLED(4)
__A_Reverse = PWMLED(17)
__A_Park = PWMLED(27)
__B_Power = PWMLED(18)
__B_Reverse = PWMLED(23)
__B_Park = PWMLED(24)


def forward(velocity):
    __A_Reverse.value = 1.0
    __B_Reverse.value = 0.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def backward(velocity):
    __A_Reverse.value = 0.0
    __B_Reverse.value = 1.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def turn_right(velocity):
    __A_Reverse.value = 1.0
    __B_Reverse.value = 1.0
    __A_Power.value = velocity
    __B_Power.value = velocity


def turn_left(velocity):
    __A_Reverse.value = 0.0
    __B_Reverse.value = 0.0
    __A_Power.value = velocity
    __B_Power.value = velocity
