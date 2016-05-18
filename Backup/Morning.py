import random, re, pygame

WORDS = ["MORNING"]

def handle(text, mic, profile):
       # messages = ["/home/pi/Sounds/Good_morning.wav"]

	#print "Mornings mening blev " + message

	#pygame.mixer.init()
	#pygame.mixer.music.load(message)
	#pygame.mixer.music.play()
	#while pygame.mixer.music.get_busy() == True:
	#	continue
	#pygame.mixer.quit()
	messages = ["good morning"]
	mic.say(message)

def isValid(text):	
    return bool(re.search(r'morning', text, re.IGNORECASE))

