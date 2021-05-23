# This module is used to get the data of Avoiding obstacles components

from gpiozero import DistanceSensor
from time import sleep

sensor_head_left = DistanceSensor()
sensor_head_right = DistanceSensor()
sensor_head_middle = DistanceSensor()
sensor_body_left = DistanceSensor()
snesor_body_right = DistanceSensor()


def get_distances() -> (list):
    while True:
        distance_list = []
        distance_list[0] = sensor_head_left
        distance_list[1] = sensor_head_right
        return distance_list


# 0-turn left
# 1-turn right
def turn_decision(distance_list) -> (int):
    if(distance_list[0] < 0.3 & distance_list[1] < 0.3):
        if(distance_list[0] > distance_list[1]):
            return 0
        else:
            return 1
