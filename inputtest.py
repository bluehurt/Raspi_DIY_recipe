""
[Overview] Read signal from GPIO 17 and display whether the switch ( connected to GPIO 17 ) is pushed or not.
[Input]    GPIO 17 status  0:off  1:on
[Output]   GPIO 17 status  0:off  1:on
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

while 1:
    print(GPIO.input(17))
    time.sleep(1)
