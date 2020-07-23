import RPi.GPIO as GPIO
import time

channel = 13
channel2 = 7

#GPIO setup
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT, initial = 1)
    GPIO.setup(channel2, GPIO.OUT, initial = 0)


def motor_on(pin):
    GPIO.output(pin, 0) #turn on
    

def motor_off(pin):
    GPIO.output(pin, 1) #turn off
    
    
if __name__ == '__main__':
    try:
        setup()
        runner = True
        while(runner):
            uinput = input("Press 1 for on, 2 for off, or 0 to end: ")
            uinput = int(uinput)
            if uinput == 1:
                motor_on(channel)
                motor_on(channel2)
                print("on")
            elif uinput == 2:
                motor_off(channel)
                motor_on(channel2)
                print("off")
            elif uinput == 0:
                runner = False
            else:
                print("Your input was incorrect, please try again.")
        
        
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()