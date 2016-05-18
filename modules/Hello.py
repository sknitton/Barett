import random
import re
from client import jasperpath

WORDS = ["HELLO","HEY","SUP","HOLA"]

def handle(text,mic,profile):
	messages = ["Hello there!",
	"Sup bro?",
	"Good day, did you know that the bird is the word?",
	"Here comes that boy, ayy whaddup?"]
	
	message = random.choice(messages)
	print "The hello message was " + message
	mic.say(message)

def isValid(text):
	return bool(re.search(r'\bhello\b', text, re.IGNORECASE))
