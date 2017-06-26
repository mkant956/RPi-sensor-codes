#!/usr/bin/python
import smbus
import time
import math

bus = smbus.SMBus(1)
address = 0x1e
minx=-482.0
maxx=427.0
miny=-462.0
maxy=506.0

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)

for i in range(0,1):
	write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
	write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
	write_byte(2, 0b00000000) # Continuous sampling

	scale = 0.92
while True:
	x_out = read_word_2c(3)
	y_out = read_word_2c(7)
	z_out = read_word_2c(5)
	x_out=(x_out+(minx+maxx)/2)/(maxx-minx)
	y_out=(y_out+450+(miny+maxy)/2)/(maxy-miny)
	bearing  = math.atan2(y_out, x_out) 
	if (bearing < 0):
	    bearing += 2 * math.pi

	print  math.degrees(bearing)
	#print , (y_out+450-miny)/(maxy-miny)
	time.sleep(0.1)


