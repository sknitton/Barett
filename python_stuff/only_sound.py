import RPi.GPIO as GPIO
import time
import subprocess
import pyglet
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
			song = pyglet.media.load('python_stuff/Mamma.wav.wav')
			song.play()
			pyglet.app.run()
	except KeyboardInterrupt:
                GPIO.cleanup()
                print 'Interrupted'



