import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

freq = 50
pwm = GPIO.PWM(7,freq)

#send repeated pulses of an absolute duration between 0.75 and 2.5ms
#in duration

leftPosition = 0.75
rightPosition = 2.5
middlePosition = (rightPosition - leftPosition / 2 + leftPosition)

positionList = (leftPosition, middlePosition, rightPosition, middlePosition)

msPerCycle = 1000/freq

for i in range(3):
	for position in positionList:
		dutyCyclePercentage = position * 100 / msPerCycle
		print "Position: " + str(position)
		print "Duty Cycle: " + str(dutyCyclePercentage) + "-"
		print ""
		pwm.start(dutyCyclePercentage)
		time.sleep(.5)
pwm.stop()
GPIO.cleanup()
