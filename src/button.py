from gpiozero import LED, Button
from signal import *

led = LED(19)
button = Button(26)

#button 一个口连26 一个连GND 

def work():
    print('work')
    # led.value=1

def sleep():
    print('sleep')
    led.value=0

print(button.value)
button.wait_for_press()
print(button.value)

button.when_pressed = work
print('hello')
button.wait_for_release()
button.when_released= sleep
    
print("end")