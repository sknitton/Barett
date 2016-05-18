from smbus import SMBus
import time

address = 0x60 
CAP1188_SENINPUTSTATUS = 0x3 
CAP1188_SENLEDSTATUS = 0x4 
CAP1188_MTBLK = 0x2A 
CAP1188_PRODID = 0xFD 
CAP1188_MANUID = 0xFE 
CAP1188_STANDBYCFG = 0x41 
CAP1188_REV = 0xFF 
CAP1188_MAIN = 0x00 
CAP1188_MAIN_INT = 0x01 
CAP1188_LEDPOL = 0x73 
CAP1188_INTENABLE = 0x27 
CAP1188_REPRATE = 0x28 
CAP1188_LEDLINK = 0x72 
CAP1188_SENSITIVITY = 0x1f 
CAP1188_CALIBRATE = 0x26 

b = SMBus(1) 
b.write_byte_data(address, CAP1188_MTBLK, 0) 
b.write_byte_data(address, CAP1188_STANDBYCFG, 0x30) 
b.write_byte_data(address, CAP1188_INTENABLE, 0x05) 
b.write_byte_data(address, CAP1188_LEDLINK, 0xff) 
b.write_byte_data(address, CAP1188_SENSITIVITY, 0x6f) 
b.write_byte_data(address, CAP1188_CALIBRATE, 0xff)
 
while True:
	t1 = b.read_byte_data(address, CAP1188_SENINPUTSTATUS)
	print(str(t1)+","+'{0:08b}'.format(t1))
	time.sleep(0.05)
	b.write_byte_data(address, CAP1188_MAIN, 0x00)
