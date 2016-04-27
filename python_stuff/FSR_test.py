import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
def Force ():
	reading = 0
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	time.sleep(1)
         
	GPIO.setup(13, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(13) == GPIO.LOW):
        	reading += 1
		time.sleep(0.01)
        return reading
while True:
	try:
		print Force()
	except KeyboardInterrupt:
		GPIO.cleanup()
        	print 'Interrupted'
