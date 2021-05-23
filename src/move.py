# This file used to control basic movement

from gpiozero import PWMLED
from time import sleep


# left wheel A
# right wheel B
A_Power = PWMLED(4)
A_Reverse = PWMLED(17)
A_Park = PWMLED(27)
B_Power = PWMLED(18)
B_Reverse = PWMLED(23)
B_Park = PWMLED(24)


def forward(velocity):
    A_Reverse.value = 1.0
    B_Reverse.value = 0.0
    A_Power.value = velocity
    B_Power.value = velocity


def backward(velocity):
    A_Reverse.value = 0.0
    B_Reverse.value = 1.0
    A_Power.value = velocity
    B_Power.value = velocity


def turn_right(velocity_left, velocity_right):
    A_Reverse.value = 1.0
    B_Reverse.value = 1.0
    A_Power.value = velocity_left
    B_Power.value = velocity_right


def turn_left(velocity_left, velocity_right):
    A_Reverse.value = 0.0
    B_Reverse.value = 0.0
    A_Power.value = velocity_left
    B_Power.value = velocity_right
#停车
def stop(stop_time):
    A_Power=0
    B_Power=0
    sleep(stop_time)

#驻车
def park():
    A_Power=0
    B_Power=0
    A_Park=1
    B_Park=1
