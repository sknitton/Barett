#import lots of stuff
#GPIO so we can use the GPIO pins
#Time so that we can use sleep
#pygame for audio
#math for modulo
import RPi.GPIO as GPIO, time, pygame, math
#configure board
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

#block is used in the input loops so that it cant get stuck waiting for input
#reac is the value that reading have to be or lower than for it to trigger
#expo is a big number that we multiply the angles with to get a smoother curve 
block = 20 
reac = 3*block/10
expo = 20

#The function for the hugsensor
def FSRkram():
	reading = 0
	#reset the pin
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.LOW)
	time.sleep(0.25)
	GPIO.setup(13, GPIO.IN)

	#Gather info to check if its pressed down
	#The harder you press the FSR the lower reading will be when it returns.
	while(GPIO.input(13) == GPIO.LOW):
	        reading += 1
#		print "Krams reading " + str(reading)
		time.sleep(0.01)
		#prevent clogging
        	if (reading >= block):
            		return reading
	return reading

def FSRpet ():
	reading = 0
	#reset the pin
	GPIO.setup(29, GPIO.OUT)
	GPIO.output(29, GPIO.LOW)
	time.sleep(.25)
	GPIO.setup(29, GPIO.IN)

	#Gather info to check if its pressed down
	#The harder you press the FSR the lower reading will be when it returns.
	while (GPIO.input(29) == GPIO.LOW):
		reading += 1
#		print "Pets reading: " + str(reading)
		time.sleep(0.01)
		#prevent blockings so that it cant clog the function
	        if (reading >= block+5):
        	    return reading
	return reading

def mainloop():
		temp = FSRkram()
		if temp <= reac:
			#Initiera motorerna och bereätta att vi fått en reaktion
			print "Kramen reagerade på värdet " + str(temp)
			#creating a PWM object on pin 7 with 50hz signal command
			pwm=GPIO.PWM(7, 50)
			pwm.start(7)
			#(1./18.*vinkel)+2 is the formula to get what value you want to sent into .ChangeDutyCycle() to change the positions.
			#reset the angle
			vinkel = 80
			pwm.ChangeDutyCycle((1./18.*80)+2)
			#g1 and g2 are the restrics 
			#they are multiplied with expo to get a bigger curve
			g1 = 30* expo 
			g2 = 60* expo
			gg2 = g2
			while g1<=g2:
				#is there so that it only prints once every degree
				if g2 % expo == 0:
					print "Vinkeln är "+ str(g2/expo)
					
					pwm.ChangeDutyCycle((1./18.*g2/expo)+2)	
				g2 -= 1
				#bigger .sleep = slower arm movement
				time.sleep(0.001)
			time.sleep(1)
			#Go back slowly so that it is smooth
				#basically just the same thing as above but the literal reverse
			while g2 <= gg2:
				if g2 % expo == 0:
					print "Vinkeln är " + str(g2/expo)
				pwm.ChangeDutyCycle((1./18.*g2/expo)+2)
				g2 += 1
				time.sleep(0.0005)
			time.sleep(.3)
			#Rest the engines
			pwm.stop()
		temp = FSRpet()
		if temp <= reac:
			#Print the reactionary value
			print "Pet reagerade på " + str(temp)
			#Initiate the audio player
			pygame.mixer.init()
			pygame.mixer.music.load("../Sounds/Pet_best.wav")
			pygame.mixer.music.play()
			#Keep on playing the file until its done
			while pygame.mixer.music.get_busy() == True:
				continue
			pygame.mixer.quit()

#Loopen
while True:
	try:
		mainloop()
		time.sleep(0.001)
	except KeyboardInterrupt:
		print "Interrupted"
