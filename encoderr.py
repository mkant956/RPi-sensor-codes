from RPi import GPIO
from time import sleep

clk = 8
dt = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 1
clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                clkLastState = clkState
                sleep(0.0001)
finally:
        GPIO.cleanup()
