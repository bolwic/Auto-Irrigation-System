import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import math

#this is to test the moisture sentor

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1


value = [0]*100
def read():
    while True:
        for i in range(100):
            value[i] = adc.read_adc(0,gain=GAIN)
        print(max(value))


if __name__ == '__main__':
    read()
