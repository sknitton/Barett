import random, re
from client import jasperpath

WORDS = ["RUSE","JOKES","GAG","QUIRK","JEST"]

def handle(text, mic, profile):
    messages = ["I never wanted to believe that my Dad was stealing from his job as a road worker. But when I got home, all the signs were there.",
                "What happens to a frog's car when it breaks down? It gets toad away.",
                "If con is the opposite of pro, then is Congress the opposite of progress?",
                "Want to hear a Potassium joke? K.",
                "Yo mom is so dumb that she thought Dunking Donuts was a basketball team.",
                "I named my hard drive dat ass, so once a month my computer asks if I want to back dat ass up.",
                "I was wondering why the ball kept getting bigger and bigger, and then it hit me.",
                "I went to the bank the other day and asked the banker to check my balance, so she pushed me!",
                "A man got hit in the head with a can of Coke, but he was alright because it was a soft drink.",
                "Did you hear about the guy whose whole left side was cut off? He's all right now."]
    message = random.choice(messages)
    print message
    mic.say(message)
