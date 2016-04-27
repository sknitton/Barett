import time
import os

try:
	while True:
		os.system("vcgencmd measure_temp")
		time.sleep(1)
except keyboardInterrupt:
	print("Done measuring")
