import RPi.GPIO as GPIO, time, pygame
from random import randint
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm=GPIO.PWM(7, 50)
pwm.start(7)

def FSRkram():
	reading = 0
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	time.sleep(0.5)

	GPIO.setup(13, GPIO.IN)

	while(GPIO.input(13) == GPIO.LOW):
		reading += 1
	return reading

def FSRpet ():
	reading = 0
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.LOW)
	time.sleep(1)
	GPIO.setup(29, GPIO.IN)
#	This takes about 1 millisecond per loop cycle
#	while (GPIO.input(29) == GPIO.LOW):
#		reading += 1
#		print reading
	return reading

def mainloop():
		temp = FSRkram()
		if temp <= 80:
			#byt till kramposition
			pwm.ChangeDutyCycle((1./18.*50)+2)
			print temp
			time.sleep(1)
#			DC=(1./18.*90)+2
			pwm.ChangeDutyCycle((1./18.*90)+2)
		temp = FSRpet()
		temp = 500
		if temp <= 100:
			pygame.mixer.init()
			pygame.mixer.music.load("Mamma.wav.wav")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
			print ("mamma" + str(temp))
			pygame.mixer.quit()

while True:
	try:
		mainloop()
	except KeyboardInterrupt:
		print "Interrupted"
