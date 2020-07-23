import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import math

channel1 = 7 #sun lamp
channel2 = 13 #water pump

#GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel1, GPIO.OUT)
GPIO.output(channel1, GPIO.HIGH)
GPIO.setup(channel2, GPIO.OUT)
GPIO.output(channel2, GPIO.LOW)

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1




def motor_on():
    print("on")
    GPIO.output(channel1, 0) #turn on
    GPIO.output(channel2, 1) #turn on
    

def motor_off():
    print("off")
    GPIO.output(channel1, 1) #turn off
    GPIO.output(channel2, 0) #turn on

value = [0]*100



    
 
    
if __name__ == '__main__':
    try:
        print("the begining")
        while True:
            for i in range(100):
                try:
                    value[i] = adc.read_adc(0,gain=GAIN)
                except:
                    print("OSError")
            print(max(value))
            if(max(value) < 15300):
                print("wet")
                motor_off()
            else:
                print("dry")
                motor_on()

        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
