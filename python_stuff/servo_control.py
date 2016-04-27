import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin=7
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(7)
while True:
	try:
		desiredPosition= input("Vilken position ska armen vara? 0-180 grader")
		DC=1./18.*(desiredPosition)+2
		pwm.ChangeDutyCycle(DC)
	except KeyboardInterrupt:
		pwm.stop()
		GPIO.cleanup()
