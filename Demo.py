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
#block is used in the input loops so that it cant get stuck waiting for input
block = 10000

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
        if (reading >= block):
            return reading
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
	while (GPIO.input(29) == GPIO.LOW):
		reading += 1
        #this is to prevent it from getting stuck in the loop
        if (reading >= block):
            return reading
	return reading

def mainloop():
		temp = FSRkram()
		if temp <= 80:
			#(1./18.*vinkel)+2 är formeln för att få reda på vad man vill stoppa in i .ChangeDutyCycle()
			#.ChangeDutyCycle ändrar armarnas position baserat på formeln över men egentligen beroende på en siffra mellan 2 och 12. 
			pwm.ChangeDutyCycle((1./18.*50)+2)
			#Write out temp so that we can know which value it reacted on
			print "Krams reading blev " +  str(temp)
			time.sleep(3)
			#Go back to the natural position
			pwm.ChangeDutyCycle((1./18.*90)+2)
            pygame.mixer.init()
			pygame.mixer.music.load("Mamma.wav.wav")
			pygame.mixer.music.play()
			#Keep on playing the file until its done
			while pygame.mixer.music.get_busy() == True:
				continue
			print ("Pet fick readingen " + str(temp))
			pygame.mixer.quit()
		temp = FSRpet()
		#We change it to a outside value so that it cant interrupt the program
		temp = 500
		if temp <= 100:
			#Initiate the audio player
			pygame.mixer.init()
			pygame.mixer.music.load("Mamma.wav.wav")
			pygame.mixer.music.play()
			#Keep on playing the file until its done
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
