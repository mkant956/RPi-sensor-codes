import led1
import ultrasonic
import RPi.GPIO as GPIO
import time
import sys, tty, termios
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

char='a' 
if __name__ == '__main__':
    try:
        while True:
		dist=ultrasonic.distance()
		print ("%.1f cm" % dist)
		time.sleep(0.1)
		if(dist>10.0 and dist<20.0):
			char='a'
		elif(dist>20.0):
			char='b'
		else:
			char='x'
		led1.glowLed(char)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
