import random, re, pygame

WORDS = ["HELLO"]

def handle(text,mic,profile):
	messages = ["/home/pi/Sounds/Hello.wav", "/home/pi/Sounds/Good_day.wav"]
	
	message = random.choice(messages)
	print "The hello message was " + message

	pygame.mixer.init()
	pygame.mixer.music.load(message)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.mixer.quit()
	
#	mic.say(message)
	


def isValid(text):
	return bool(re.search(r'hello', text, re.IGNORECASE))
