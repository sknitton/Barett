import smbus
import time

bus = smbus.SMBus(1)
  # I2C address for MMA7660                                                     
addr = 0x28
try:
	bus.write_byte_data(addr, 0x07, 0x00)
	bus.write_byte_data(addr, 0x06, 0x10)
	bus.write_byte_data(addr, 0x08, 0x00)
	bus.write_byte_data(addr, 0x07, 0x01)
except IOError, err:
	print err

while True:
	try:
		x = bus.read_byte_data(addr,0x00)
		y = bus.read_byte_data(addr,0x01)
		z = bus.read_byte_data(addr,0x02)
		tr = bus.read_byte_data(addr,0x03)
		print x, y, z, tr
		time.sleep(0.25)
	except:
			print 'exiting...'
			break	
