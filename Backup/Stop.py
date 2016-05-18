import os, signal, time, psutil

WORDS = ["STOP"]

def handle(text, mic, profile):
	try:
		pids = psutil.pids()
		for pid in pids:
			if psutil.Process(pid).name() == "Beta.py":
				print pid
				os.kill(pid, signal.SIGINT)
	except NoSuchProcess:
		print "No process"
	print "It reacted on stop"
	print "pgrep -f Beta.py"
	
def isValid(text):
	return bool(re.search(r'\stop\b', text, re.IGNORECASE))
