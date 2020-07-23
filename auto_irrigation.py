import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import math
import datetime
import picamera

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

thedate = datetime.datetime.now()
#camera = picamera.PiCamera()

def capture_image():
    camera.capture('/home/pi/stored_image/%simage.jpg' %(datetime.date.today()))
    
def lamp_on():
    print("lamp on")
    GPIO.output(channel1, 0) #turn on
    

def lamp_off():
    print("lamp off")
    GPIO.output(channel1, 1) #turn off


def motor_on():
    print("pump on")
    GPIO.output(channel2, 1) #turn on
    

def motor_off():
    print("pump off")
    GPIO.output(channel2, 0) #turn off

value = [0]*100



    
 
    
if __name__ == '__main__':
    try:
        print("the begining")
        while True:
            current_time = datetime.datetime.now()
            if((current_time.hour >= 10) and (current_time.hour <= 17)): #currently set to 7am to 6pm
                lamp_on()
            else:
                lamp_off()
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

