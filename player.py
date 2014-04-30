#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

os.system('sudo rm /tmp/cmd')
os.system('mkfifo /tmp/cmd')
print 'Witam ;-)\n'
print 'Zapalam diode...\n'
os.system('/usr/local/bin/gpio mode 7 out')
os.system('/usr/local/bin/gpio write 7 1')
print 'Laduje pliki audio...\n'
os.system('/usr/bin/omxplayershuffle local /media/*/ < /tmp/cmd &')
#print 'Play >\n'
#os.system('echo -n p > /tmp/cmd &')

x=1

while True:
    if ( GPIO.input(23) == False ):
        if(x==1):
            os.system('echo -n p > /tmp/cmd &')
            print 'Play >\n'
            sleep(0.2);
        else:
            os.system('echo -n q > /tmp/cmd &')
            os.system('omxplayershuffle local /media/*/ < /tmp/cmd &')
            os.system('echo -n p > /tmp/cmd &')
            print 'Pauza ||\n'
            x=1
            sleep(0.2);
    if ( GPIO.input(24) == False ):
        os.system('echo -n q > /tmp/cmd &')
        os.system('omxplayershuffle local /media/*/ < /tmp/cmd &')
        os.system('echo -n p > /tmp/cmd &')
        print 'Shuffle\n'
        x=1
        sleep(0.2);
    if ( GPIO.input(25)== False ):
        os.system('sudo pkill omxplayer')
        print 'Stop\n'
        x=x-1
        sleep(0.2);
    if ( GPIO.input(22) == False ):
        os.system('echo -n i > /tmp/cmd &')
        print '<< Poprzednia\n'
        sleep(0.2);
    if ( GPIO.input(10) == False ):
        os.system('echo -n o > /tmp/cmd &')
        print 'Nastepna >>\n'
        sleep(0.2);
