import smbus
import time
bus = smbus.SMBus(1)
address = 0x28

def cap():
    return bus.read_byte_Data(address,1)

while True:
    print cap()
    time.sleep(1)

