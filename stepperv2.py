import RPi.GPIO as GPIO
import time

# Variables

delay = 2
steps = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enable GPIO pins for  ENA and ENB for stepper

#enable_a = 18
#enable_b = 22

# Enable pins for IN1-4 to control step sequence

coil_B_1_pin = 24
coil_B_2_pin = 25
coil_A_1_pin = 18
coil_A_2_pin = 23

# Set pin states

#GPIO.setup(enable_a, GPIO.OUT)
#GPIO.setup(enable_b, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Set ENA and ENB to high to enable stepper

#GPIO.output(enable_a, True)
#GPIO.output(enable_b, True)

# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

def setStepa(a,b):
	GPIO.output(coil_A_1_pin,a)
	GPIO.output(coil_A_2_pin,b)
# loop through step sequence based on number of steps
def setStepb(a,b):
	GPIO.output(coil_B_1_pin,a)
	GPIO.output(coil_B_2_pin,b)

# Reverse previous step sequence to reverse motor direction
for i in range(0,50):
	setStepb(1,0)
	time.sleep(delay)
	print("b10\n")
	setStepa(0,1)
	time.sleep(delay)
	print("a01\n")
	setStepb(0,1)
	time.sleep(delay)
	print("b01\n")
	setStepa(1,0)
	time.sleep(delay)
	print("a10\n")

#for i in range(0, steps):
    #setStep(1,0,0,1)
    #time.sleep(delay)
    #setStep(0,1,0,1)
    #time.sleep(delay)
    #setStep(0,1,1,0)
    #time.sleep(delay)
    #setStep(1,0,1,0)
    #time.sleep(delay)
