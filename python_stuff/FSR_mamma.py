import RPi.GPIO as GPIO
import time
#import subprocess
import pygame

def Force ():
        reading = 0
	#The sequence below is used to set pin 13 to low
	#In order to detect incoming signals
	GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13, GPIO.OUT)
        GPIO.output(13, GPIO.LOW)
        time.sleep(1)

        GPIO.setup(13, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(13) == GPIO.LOW):
                reading += 1
		time.sleep(0.005)
	GPIO.cleanup()
	
        return reading

while True:
		        
	try:
                print Force()
                sensorvalue = Force()
		#print sensorvalue
                if sensorvalue < 90:
	     		pygame.mixer.init()
			pygame.mixer.music.load("Mamma.wav.wav")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
			print ("mamma")
			pygame.mixer.quit()
							
			#subprocess.Popen(["aplay", "python_stuff/Mamma.wav.wav"])        
			#subprocess.Popen(["aplay", "Barettrepo/Barett/Mamma.wma"])
			#GPIO.cleanup()
 	except KeyboardInterrupt:
                GPIO.cleanup()
                print 'Interrupted'
		
		

