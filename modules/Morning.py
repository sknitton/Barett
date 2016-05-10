import random, re, pygame

WORDS = ["MORNING"]

def handle(text, mic, profile):
	
	""" Reponds to user-input, typically speech text, by relaying the
	meaning of life, 
	Arguements:
	text -- user-input, typically transcribed speech 
	mic -- used to interact with the user (for both input and output)
	profile -- contains information related to the user (e.g.,
	phone number)
	

	"""
	messages = ["Voice_007.wav", "Voice_008"]

	message = random.choice(messages)
	print "Mornings mening blev " + message
	pygame.mixer.init()
	pygame.mixer.music.load(message)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.mixer.quit()


def isValid(text):	
	return bool(re.search(r'\bmorning\b', text, re.IGNORECASE))
