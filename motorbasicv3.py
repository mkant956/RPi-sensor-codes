from time import sleep
import sys, tty, termios

#motor1 == rightmotor
#motor2 == leftmotor

#motorl == forward
#motorr == backward

import RPi.GPIO as GPIO # always needed with RPi.GPIO
# from time import sleep  # pull in the sleep function from time module

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
moto1l=18
moto1r=23
moto2l=24
moto2r=25

#power=1  #2/3 b
power=1.2
pwml=80.0
#factor=640.0/657.0 #2/3 battery
factor=(299.0/325.0)*(653.0/670.0) #full battery
pwmr=pwml*(factor**power)

GPIO.setup(moto1r, GPIO.OUT)# set GPIO 25 as output for white led
GPIO.setup(moto1l, GPIO.OUT)# set GPIO 24 as output for red led

GPIO.setup(moto2r, GPIO.OUT)# set GPIO 25 as output for white led
GPIO.setup(moto2l, GPIO.OUT)# set GPIO 24 as output for red led

motor1l = GPIO.PWM(18, 55)
motor1r = GPIO.PWM(23, 55)
motor2l = GPIO.PWM(24, 55)
motor2r = GPIO.PWM(25, 55) 

motor1l.start(100)
motor1r.start(100)
motor2l.start(100)
motor2r.start(100)

lvel=0
rvel=0
def forward(pwml,pwmr):
	print "forward"
	motor1l.ChangeDutyCycle(pwmr)
	motor1r.ChangeDutyCycle(0)
	motor2l.ChangeDutyCycle(pwml)
	motor2r.ChangeDutyCycle(0)

def backward(pwml,pwmr):
	print "backward"
	motor1l.ChangeDutyCycle(0)
	motor1r.ChangeDutyCycle(pwmr)
	motor2l.ChangeDutyCycle(0)
	motor2r.ChangeDutyCycle(pwml)

def left(pwml,pwmr):
	print "left"
	motor1l.ChangeDutyCycle(pwmr)
	motor1r.ChangeDutyCycle(0)
	motor2l.ChangeDutyCycle(0)
	motor2r.ChangeDutyCycle(pwml)

def right(pwml,pwmr):
	print "right"
	motor1l.ChangeDutyCycle(0)
	motor1r.ChangeDutyCycle(pwmr)
	motor2l.ChangeDutyCycle(pwml)
	motor2r.ChangeDutyCycle(0)

def stop():
	print "stop"
	motor1l.ChangeDutyCycle(0)
	motor1r.ChangeDutyCycle(0)
	motor2l.ChangeDutyCycle(0)
	motor2r.ChangeDutyCycle(0)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

try:
	stop()
	while True:
		# read=getch()
			#print(i)
		if(KeyboardInterrupt):
			read=raw_input()
			s1=read.find(' ')
			cmd=read[:s1]
			read=read[s1+1:]
			s2=read.find(' ')
			pwml=read[:s2]
			pwml=float(pwml)
			pwmr=read[s2+1:]
			pwmr=float(pwmr)
			if(cmd=='w'):
				forward(pwml,pwmr)
			elif(cmd=='s'):
				backward(pwml,pwmr)
			elif(cmd=='a'):
				left(pwml,pwmr)
			elif(cmd=='d'):
				right(pwml,pwmr)
			elif(cmd=='/'):
				GPIO.cleanup()
				exit()
			elif(cmd=='x'):
				stop()
			sleep(0.0001)
		# /break
        # Reset by pressing CTRL + C
except KeyboardInterrupt:
	print("Measurement stopped by client")
