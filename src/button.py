from typing import Mapping
from gpiozero import LED, Button
from signal import *

led = LED(19)
button = Button(26, hold_time=1)

#button 一个口连26 一个连GND 

press_time=0
pi_status=False

#每一次按钮都会press 和 release
#整个过程结束之后 press time +1
def button_press_count(press_time):
    button.wait_for_press()
    button.when_held=led.on

    button.wait_for_release() 
    press_time+=1
    return press_time


#press_time -> 奇数 -> 开机
#press_time -> 偶数 -> 关机
def led_control(press_time):
    if(press_time%2==0):
        print('Shut down')
        led.value=0
        pi_status=False
    else:
        print('Turn on')
        led.value=1
        pi_status=True


while True:
    press_time=button_press_count(press_time)
    led_control(press_time)
    print(pi_status)



