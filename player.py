#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

x=1

while True:
        if ( GPIO.input(23) == False ):
                os.system('omxplayershuffle local /media/*/ &')
		sleep(0.1);
        if ( GPIO.input(24) == False ):
		sleep(0.1);
		if(x==0):
			os.system('sudo pkill omxplayer')
			os.system('omxplayershuffle local /media/*/ &')
			x=x+1
		else:
			os.system('sudo pkill omxplayer')
			os.system('omxplayershuffle local /media/*/ &')
			x=x-1
        if ( GPIO.input(25)== False ):
                os.system('sudo pkill omxplayer')
        sleep(0.1);
