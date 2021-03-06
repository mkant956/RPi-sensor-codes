import RPi.GPIO as GPIO
import time
import sys, tty, termios
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def glowLed(char):
	if(char=='a'):
		#print "LED on"
		GPIO.output(23,GPIO.HIGH)
	elif(char=='b'):	
		#print "LED off"
		GPIO.output(23,GPIO.LOW)
	elif(char=='x'):
		 print("Measurement stopped by User")
        	 GPIO.cleanup()
		 quit()

char='a'
if __name__ == '__main__':
    try:
        while True:
		char=getch()
		glowLed(char)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
	
