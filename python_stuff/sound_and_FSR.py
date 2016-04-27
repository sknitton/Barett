import RPi.GPIO as GPIO
import time
import subprocess
import pygame
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
	return reading
	while True:
		try:
			print Force()
			sensorvalue = Force()
			if sensorvalue > 200:
				pygame.init()
				song = pygame.mixer.Sound('thesong.ogg')
				clock = pygame.time.Clock()
				song.play()
				while True:
    					clock.tick(60)
				pygame.quit()

		except KeyboardInterrupt:
                	GPIO.cleanup()
                	print 'Interrupted'

