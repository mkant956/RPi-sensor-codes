#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 20
GPIO_ECHO1 = 21
GPIO_ECHO2 = 16
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_ECHO2,GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime1 = time.time()
    StopTime2 = time.time()
    # save StartTime

    #print "1ok\n"

    while GPIO.input(GPIO_ECHO1) == 0 and GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
    #print "1ok\n"
    # save time of arriva
    l1=0
    l2=0
    while True:
	if(GPIO.input(GPIO_ECHO1)==0 or GPIO.input(GPIO_ECHO2)==0):
		break
    	# temp_d1=StopTime1-StartTime
    	# temp_d=(temp_d * 34300) / 2
    	# if(temp_d>80):0
    	# 	break;
        if(GPIO.input(GPIO_ECHO1) == 1 and l1==0):    
		StopTime1 = time.time()
	else:
		l1=1

#	print "1ok\n"
        # temp_d=StopTime-StartTime
        # temp_d=(temp_d * 34300) / 2
        # if(temp_d>80):
        #     break;
        if(GPIO.input(GPIO_ECHO1) == 1 and l2==0):
		StopTime2 = time.time()
	else:
		l2=1
 
    # time difference between start and arrival
    TimeElapsed1 = StopTime1 - StartTime
    TimeElapsed2 = StopTime2 - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed1 * 34300) / 2
    distance2 = (TimeElapsed2 * 34300) / 2
    # if(distance>80):
    	# distance=80
 
    print ("%.1f" % distance1 ),
    print ("%.1f\n" % distance2)
    return 1
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            # print ("%.1f" % dist)
            time.sleep(0.1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
