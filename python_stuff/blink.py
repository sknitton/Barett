import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
red=17
GPIO.setup(red,GPIO.OUT)
blink_num=input("How many times do u want to blink?")
for i in range(0, blink_num):
	GPIO.output(red, 1)
	time.sleep(1)
	GPIO.output(red,0)
	time.sleep(1)
GPIO.cleanup()
