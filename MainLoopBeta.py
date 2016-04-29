#import lots of stuff
#GPIO so we can use the GPIO pins
#Time so that we can use sleep
#pygame for audio
import RPi.GPIO as GPIO, time, pygame
from random import randint
#configure board
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
#initiate servos
pwm=GPIO.PWM(7, 50)
pwm.start(7)

#The function for the hugsensor
def FSRkram():
	reading = 0
	#reset the pin
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	time.sleep(0.5)
	GPIO.setup(13, GPIO.IN)
	#Gather info to check if its pressed down
	#The harder you press the FSR the lower reading will be when it returns.
	while(GPIO.input(13) == GPIO.LOW):
		reading += 1
	return reading

def FSRpet ():
	reading = 0
	#reset the pin
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.LOW)
	time.sleep(1)
	GPIO.setup(29, GPIO.IN)
	#Gather info to check if its pressed down
	#The harder you press the FSR the lower reading will be when it returns.
#	while (GPIO.input(29) == GPIO.LOW):
#		reading += 1
#		print reading
	return reading

def mainloop():
		temp = FSRkram()
		if temp <= 80:
			#(1./18.*vinkel)+2 är formeln för att få reda på vad man vill stoppa in i .ChangeDutyCycle()
			#byt till kramposition
			pwm.ChangeDutyCycle((1./18.*50)+2)
			#skriv ut temp så att vi vet på vilket värde det var som den reagerade på
			print "Krams reading blev " +  str(temp)
			time.sleep(1)
			#gå tillbaks till neutral position
			pwm.ChangeDutyCycle((1./18.*90)+2)
		temp = FSRpet()
		#nu när FSRpet inte fungerar 
		temp = 500
		if temp <= 100:
			#initiera ljudspelaren och ladda in 
			pygame.mixer.init()
			pygame.mixer.music.load("Mamma.wav.wav")
			pygame.mixer.music.play()
			#fortsätt spela filen tills klar
			while pygame.mixer.music.get_busy() == True:
				continue
			print ("Pet fick readingen " + str(temp))
			pygame.mixer.quit()

#Loopen
while True:
	try:
		mainloop()
	except KeyboardInterrupt:
		print "Interrupted"
