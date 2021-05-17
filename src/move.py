from gpiozero import PWMLED
from time import sleep

    
#left wheel A
#left wheel B
A_Power=PWMLED(4)
A_Reverse=PWMLED(17)
A_Park=PWMLED(27)
B_Power=PWMLED(18)
B_Reverse=PWMLED(23)
B_Park=PWMLED(24)

def forward(velocity):
    A_Reverse.value = 1.0
    B_Reverse.value=0.0
    A_Power.value=velocity
    B_Power.value=velocity
    

def backward(velocity):
    A_Reverse.value=0.0
    B_Reverse.value = 1.0
    print('2')
    A_Power.value=velocity
    B_Power.value=velocity
    print('1')


def turn_right(velocity):
    A_Reverse.value = 1.0
    B_Reverse.value = 1.0
    A_Power.value=velocity
    B_Power.value=velocity
    
    
def turn_left(velocity):
    A_Reverse.value = 0.0
    B_Reverse.value = 0.0
    A_Power.value=velocity
    B_Power.value=velocity
    
    
        

def main():
    while True:    
        turn_left(0.2)
        sleep(4)
        turn_right(0.2)
        sleep(4)
        forward(0.2)
        sleep(4)
        backward(0.2)
        sleep(4)
        

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
    