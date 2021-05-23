# This module is used to get the data of Avoiding obstacles components

import gpiozero


def get_raw_avoid_data() -> ():
    # down sensor
    lineSensor_5 = gpiozero.LineSensor(3)

    # front sensors
    lineSensor_0 = gpiozero.LineSensor(5)
    lineSensor_1 = gpiozero.LineSensor(6)
    lineSensor_2 = gpiozero.LineSensor(7)

    # side sensors
    lineSensor_3 = gpiozero.LineSensor(8)
    lineSensor_4 = gpiozero.LineSensor(9)
    # lineSensor_5 = gpiozero.LineSensor(3)

    # # front sensors
    # lineSensor_0 = gpiozero.LineSensor(5)
    # lineSensor_1 = gpiozero.LineSensor(6)
    # lineSensor_2 = gpiozero.LineSensor(7)

    # # side sensors
    # lineSensor_3 = gpiozero.LineSensor(8)
    # lineSensor_4 = gpiozero.LineSensor(9)
    return (lineSensor_0, lineSensor_1, lineSensor_2, lineSensor_3, lineSensor_4, lineSensor_5)
