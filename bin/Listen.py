import RPi.GPIO as GPIO
import os
from time import sleep
import time


GPIO.setmode(GPIO.BOARD)  #Set Pin Mode according to Board Layout

#-----------------------------------------------------------------------------
# GPIO Pins SETUP


# 5 Mins - turn off? 
THRESHOLD = 60 * 5

#Outputs in Pin Number for P1 Header.  For example, GPIO.setup(7, GPIO.OUT) is for P1-07 (GPIO 4)

GPIO.setup(21, GPIO.IN)   
GPIO.setup(7, GPIO.OUT)

changeTime = time.time()
currentState = True

while True:
    current_time = time.time();
    
    val = GPIO.input(21);
    print val;
    if val : 
        GPIO.output(7, GPIO.HIGH)
        changeTime = current_time;
        if (currentState == False) :
            currentState = True
            print "Starting Lifeberry PI"
            os.system("/root/lifeberrypi/bin/start.sh")
    else:
        GPIO.output(7, GPIO.LOW)
    sleep(.2);

    diff = current_time - changeTime;
    if ((diff > THRESHOLD) and (currentState == True)):
        currentState = False
        print "Suspending Lifeberry PI"
        os.system("/root/lifeberrypi/bin/suspend.sh")
        
        

    
