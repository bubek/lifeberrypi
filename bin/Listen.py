import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BOARD)  #Set Pin Mode according to Board Layout

#-----------------------------------------------------------------------------
# GPIO Pins SETUP

#Outputs in Pin Number for P1 Header.  For example, GPIO.setup(7, GPIO.OUT) is for P1-07 (GPIO 4)

GPIO.setup(21, GPIO.IN)   
GPIO.setup(7, GPIO.OUT)

while True:
    val = GPIO.input(21);
    print val;
    if val : 
        GPIO.output(7, GPIO.HIGH)
    else:
        GPIO.output(7, GPIO.LOW)
    sleep(.2);
