import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def pwm(pin, rate):
	GPIO.setup(pin, GPIO.OUT)
	if(rate>100):
		quit()
	
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.00005*rate)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.00005*(100-rate))

