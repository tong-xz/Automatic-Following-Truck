# This module is used to get the data of Avoiding obstacles components

from threading import main_thread
from gpiozero import DistanceSensor
from time import sleep

from gpiozero.input_devices import InputDevice

#1st echo , 2nd trigger
ultra_head_left = DistanceSensor(5,6)
ultra_head_right = DistanceSensor(8,7)

infra_head_left=InputDevice(12)
infra_head_right=InputDevice(16)
infra_bottom=InputDevice(20)

#获得车头 左右 两个超声波传感器的距离 
#单位 m
def get_ultra_distances() -> (list):
    distance_list = [ultra_head_left.distance, ultra_head_right.distance]
    return distance_list


#红外返回1/0 1-无障碍物 0-有障碍物
def get_infrared_info():
    list=[infra_head_left.value, infra_head_right.value, infra_bottom.value]
    return list


# 0-turn left
# 1-turn right
def turn_decision(distance_list) -> (int):
    if(distance_list[0] < 0.3 & distance_list[1] < 0.3):
        if(distance_list[0] > distance_list[1]):
            return 0
        else:
            return 1
