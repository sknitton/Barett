import RPi.GPIO as GPIO, time
from random import randint
GPIO.setmode(GPIO.BOARD)
servoPin = 7
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin, 50)
pwm.start(7)

def FSR():
	GPIO.setmode(GPIO.BOARD)
	reading = 0
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	time.sleep(0.5)
	
	GPIO.setup(13, GPIO.IN)
	
	while(GPIO.input(13) == GPIO.LOW):
		reading += 1	
	if reading <= 100:
		desiredPosition=randint(0, 180)
		DC=(1./18.*desiredPosition)+2	
		pwm.ChangeDutyCycle(DC)
		print "The desired position was: " + str(desiredPosition)
		print reading
	
while True:
	try:
		FSR()
	except KeyboardInterrupt:
		GPIO.cleanup()
		print "Interrupted"
