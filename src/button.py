from gpiozero import LED, Button
from signal import *

led = LED(19)
button = Button(26)

#button 一个口连26 一个连GND

button.when_pressed = led.on
button.when_released = led.off

signal.pause()
print("end")