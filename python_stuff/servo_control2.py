import RPi.GPIO as GPIO

#Use physical pin numbering, .BOARD instead of GPIO numbering, .BCM
GPIO.setmode(GPIO.BOARD)

#designated GPIO pins that sends PWM to Servo
firstServoPin=11
secondServoPin=7

#Left arm will be using pins 7 and 6. 7 for instructions and 6 for ground.
#Right arm will be using pins 9 and 11. 11 for instructions and 9 for ground.

#Designate pin as OUTPUT pins
#set the second pins pwm to 50 hz
GPIO.setup(firstServoPin, GPIO.OUT)
pwm=GPIO.PWM(firstServoPin,50)

#repeat with second pin
GPIO.setup(secondServoPin, GPIO.OUT)
pwm2=GPIO.PWM(secondServoPin,50)

#Start Sending signals, 
pwm.start(7)
#test 20 positions based on user input
for i in range(0,20):
	#fGet user input for desired position
	desiredPosition= input("Vilken position ska armen vara? 0-180 grader")
	DC=1./18.*(desiredPosition)+2
	pwm.ChangeDutyCycle(DC)
	pwm2.ChangeDutyCycle(DC)

#stop sending signals to servos
pwm.stop()
pwm2.stop()

#Unbind GPIO pin setups.
GPIO.cleanup()
