import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
while True:
       i=GPIO.input(7)
       if i==0:
             print ("No intruders",i)
             time.sleep(0.1)
       elif i==1:
             print ("Intruder detected",i)
             os.system("raspistill -o detected.jpg")
             os.system("sudo python Mycam.py")
             time.sleep(0.1)
