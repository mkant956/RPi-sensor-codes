# import RPi.GPIO as GPIO
# from time import sleep
 
# GPIO.setmode(GPIO.BOARD)
 
# Motor1A = 16
# Motor1B = 18
# Motor1E = 22
 
# GPIO.setup(Motor1A,GPIO.OUT)
# GPIO.setup(Motor1B,GPIO.OUT)
# GPIO.setup(Motor1E,GPIO.OUT)
 
# print "Going forwards"
# GPIO.output(Motor1A,GPIO.HIGH)
# GPIO.output(Motor1B,GPIO.LOW)
# GPIO.output(Motor1E,GPIO.HIGH)
 
# sleep(2)
 
# print "Going backwards"
# GPIO.output(Motor1A,GPIO.LOW)
# GPIO.output(Motor1B,GPIO.HIGH)
# GPIO.output(Motor1E,GPIO.HIGH)
 
# sleep(2)
 
# print "Now stop"
# GPIO.output(Motor1E,GPIO.LOW)
 
# GPIO.cleanup()

from time import sleep
import sys, tty, termios
lvel=0
rvel=0
def forward():
	print "forward"

def backward():
	print "backward"

def left():
	print "left"

def right():
	print "right"

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == '__main__':
	
	try:
		while True:
			read=getch()
			#print(i)
			if(read=='w'):
				forward()
			elif(read=='s'):
				backward()
			elif(read=='a'):
				left()
			elif(read=='d'):
				right()
			elif(read=='/'):
				exit()
			sleep(0.0001)
			# /break

        # Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by client")