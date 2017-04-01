"""
[Function]
   1. Read signal from GPIO 17 and display whether the switch (connected to GPIO 17) is pushed or not.
   2. Switch on/off the LED (connected to GPIO 18).
[Input]
   GPIO 17 status  0:off  1:on
[Output]
   GPIO 17 status   0:off  1:on
   GPIO 18 voltage  0:0v   1:3.3v
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

while 1:
    switch=GPIO.input(17)
    if 1 == switch:
        print(1)
        GPIO.output(18,1)
    else:
        print(0)
        GPIO.output(18,0)
    time.sleep(1)
